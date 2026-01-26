import json
from urc_wallet import address
from urc_ledger import txid

# Load snapshot
with open("snapshot.json") as f:
    snap = json.load(f)

# Use first UTXO
k, v = list(snap["utxo"].items())[0]
prev_tx, idx = k.split(":")
idx = int(idx)

tx = {
    "inputs": [{"prev_tx": prev_tx, "index": idx, "sig": "TEST"}],
    "outputs": [{"address": "DzsjV6SRAUpoNc6z724TaFrVpTQgtrmGKyB1tVQA3GPG", "amount": v["amount"]}]
}

print("TXID:", txid(tx))
print(json.dumps(tx, indent=2))
