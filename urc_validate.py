import json, hashlib
from urc_ledger import canon, txid, utxo_key, sum_outputs

TARGET0 = 2**240

def header_hash(header):
    return hashlib.sha256(canon(header)).hexdigest()

def valid_pow(header):
    return int(header_hash(header),16) < TARGET0

def validate_header(prev_block, block):
    h = block["header"]
    ph = prev_block["hash"]

    assert h["parent"] == ph
    assert h["height"] == prev_block["header"]["height"] + 1
    assert h["time"] >= prev_block["header"]["time"]
    assert valid_pow(h)

def validate_tx(tx, utxo, allow_coinbase=False):
    ins = tx.get("inputs", [])
    outs = tx.get("outputs", [])
    assert isinstance(outs, list) and len(outs) >= 1

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
        total_in += utxo[k]["amount"]

    total_out = sum_outputs(tx)
    assert total_in >= total_out  # fee >= 0
    return True

def validate_block(prev_block, block, utxo):
    validate_header(prev_block, block)

    spent_in_block = set()
    for j, tx in enumerate(block["txs"]):
        allow_coinbase = (j == 0)
        validate_tx(tx, utxo, allow_coinbase=allow_coinbase)

        # enforce no double-spend inside block
        for inp in tx.get("inputs", []):
            k = utxo_key(inp["prev_tx"], inp["index"])
            assert k not in spent_in_block
            spent_in_block.add(k)

    return True

def mempool_admit(tx, utxo, mempool):
    # reject if any input already spent by a mempool tx
    mem_spent = set()
    for t in mempool:
        for inp in t.get("inputs", []):
            mem_spent.add(utxo_key(inp["prev_tx"], inp["index"]))

    for inp in tx.get("inputs", []):
        k = utxo_key(inp["prev_tx"], inp["index"])
        assert k not in mem_spent

    validate_tx(tx, utxo, allow_coinbase=False)
    return True

def fee(tx, utxo):
    if tx["inputs"]==[]: return 0
    tin = sum(utxo[f'{i["prev_tx"]}:{i["index"]}']["amount"] for i in tx["inputs"])
    tout = sum(o["amount"] for o in tx["outputs"])
    return tin - tout

def mempool_sort(mempool, utxo):
    return sorted(mempool, key=lambda tx: fee(tx,utxo)/len(canon(tx)), reverse=True)
