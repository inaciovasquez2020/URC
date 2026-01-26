import json

def export_snapshot(chain, path="snapshot.json"):
    snap = {
        "tip": chain.best_tip(),
        "utxo": chain.utxo
    }
    with open(path,"w") as f:
        json.dump(snap, f, indent=2)

def import_snapshot(path="snapshot.json"):
    with open(path) as f:
        return json.load(f)
