import json, hashlib, os
from copy import deepcopy

def load_json(path, default):
    if not os.path.exists(path): return deepcopy(default)
    with open(path,"r") as f: return json.load(f)

def save_json(path, obj):
    tmp = path + ".tmp"
    with open(tmp,"w") as f: json.dump(obj, f, indent=2, sort_keys=True)
    os.replace(tmp, path)

def canon(obj):
    return json.dumps(obj, sort_keys=True, separators=(",",":"), ensure_ascii=False).encode("utf-8")

def txid(tx):
    return hashlib.sha256(canon(tx)).hexdigest()

def utxo_key(prev_tx, index):
    return f"{prev_tx}:{index}"

def sum_outputs(tx):
    return sum(o["amount"] for o in tx["outputs"])

def apply_block(block, utxo):
    """Apply all txs; assumes already validated. Returns (new_utxo, undo)."""
    undo = {"spent": {}, "created": []}
    new = deepcopy(utxo)

    for tx in block["txs"]:
        tid = tx.get("txid") or txid(tx)

        # spend inputs
        for inp in tx.get("inputs", []):
            k = utxo_key(inp["prev_tx"], inp["index"])
            undo["spent"][k] = new[k]
            del new[k]

        # create outputs
        for i, out in enumerate(tx["outputs"]):
            k = utxo_key(tid, i)
            new[k] = out
            undo["created"].append(k)

    return new, undo

def revert_block(utxo, undo):
    new = deepcopy(utxo)
    for k in undo["created"]:
        if k in new: del new[k]
    for k, v in undo["spent"].items():
        new[k] = v
    return new
