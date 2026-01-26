# urc_validate.py
# Full validator for URC (transactions + blocks)

import hashlib

from urc_wallet import verify
from urc_ledger import canon
from urc_checkpoints import CHECKPOINTS


TARGET0 = 2**240


# ---------- helpers ----------

def header_hash(header):
    return hashlib.sha256(canon(header)).hexdigest()


def valid_pow(header):
    return int(header_hash(header), 16) < TARGET0


def utxo_key(prev_tx, index):
    return f"{prev_tx}:{index}"


def sum_outputs(tx):
    return sum(o["amount"] for o in tx["outputs"])


def fee(tx, utxo):
    if tx["inputs"] == []:
        return 0
    tin = sum(utxo[utxo_key(i["prev_tx"], i["index"])]["amount"]
              for i in tx["inputs"])
    tout = sum_outputs(tx)
    return tin - tout


# ---------- transaction validation ----------

def validate_tx(tx, utxo, allow_coinbase=False):
    """
    Enforces:
    - valid structure
    - ownership via pubkey
    - Ed25519 signature
    - conservation of value
    """

    ins = tx.get("inputs", [])
    outs = tx.get("outputs", [])

    assert isinstance(outs, list) and len(outs) >= 1

    # outputs must carry cryptographic ownership
    for o in outs:
        assert "pubkey" in o
        assert "address" in o
        assert "amount" in o

    # coinbase
    if len(ins) == 0:
        assert allow_coinbase
        return True

    seen = set()
    total_in = 0

    for inp in ins:
        k = utxo_key(inp["prev_tx"], inp["index"])
        assert k in utxo
        assert k not in seen
        seen.add(k)

        utxo_entry = utxo[k]
        total_in += utxo_entry["amount"]

        # ownership: pubkey must match UTXO
        pk_hex = inp["pubkey"]
        assert pk_hex == utxo_entry["pubkey"]

        # verify signature over tx with empty sig field
        tmp = dict(tx)
        tmp["inputs"] = [dict(i) for i in tx["inputs"]]
        tmp["inputs"][0]["sig"] = ""

        msg = canon(tmp)
        verify(pk_hex, msg, inp["sig"])

    total_out = sum_outputs(tx)
    assert total_in >= total_out

    return True


# ---------- block validation ----------

def validate_block(prev_block, block, utxo):
    """
    Enforces:
    - parent linkage
    - height monotonicity
    - PoW validity
    - checkpoints
    - transaction validity
    - no double-spend inside block
    """

    h = block["header"]

    # structural
    assert h["parent"] == prev_block["hash"]
    assert h["height"] == prev_block["header"]["height"] + 1
    assert h["time"] >= prev_block["header"]["time"]

    # proof of work
    assert valid_pow(h)

    # checkpoint enforcement
    if h["height"] in CHECKPOINTS:
        assert block["hash"] == CHECKPOINTS[h["height"]]

    spent_in_block = set()

    for idx, tx in enumerate(block["txs"]):
        allow_coinbase = (idx == 0)
        validate_tx(tx, utxo, allow_coinbase=allow_coinbase)

        for inp in tx.get("inputs", []):
            k = utxo_key(inp["prev_tx"], inp["index"])
            assert k not in spent_in_block
            spent_in_block.add(k)

    return True


# ---------- mempool policy ----------

def mempool_admit(tx, utxo, mempool):
    """
    Rejects:
    - invalid tx
    - double-spend against mempool
    """

    mem_spent = set()
    for t in mempool:
        for i in t.get("inputs", []):
            mem_spent.add(utxo_key(i["prev_tx"], i["index"]))

    for i in tx.get("inputs", []):
        assert utxo_key(i["prev_tx"], i["index"]) not in mem_spent

    validate_tx(tx, utxo, allow_coinbase=False)
    return True


def mempool_sort(mempool, utxo):
    """
    Order by fee per byte
    """
    return sorted(
        mempool,
        key=lambda tx: fee(tx, utxo) / max(1, len(canon(tx))),
        reverse=True
    )

