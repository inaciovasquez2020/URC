import sys, os, json
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from urc_wallet import verify
from urc_ledger import canon

with open("signed_tx.json") as f:
    tx = json.load(f)

sig = tx["inputs"][0]["sig"]
pk  = input("Paste public key hex: ").strip()

# remove signature before verifying
tx["inputs"][0]["sig"] = ""

msg = canon(tx)
verify(pk, msg, sig)

print("SIGNATURE VALID")

