import sys, os, json, binascii
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from urc_wallet import genkey, address, sign
from urc_ledger import canon

with open("unsigned_tx.json") as f:
    tx = json.load(f)

# ensure empty signature before signing
tx["inputs"][0]["sig"] = ""

sk, pk = genkey()
addr = address(pk)

msg = canon(tx)
sig = sign(sk, msg)

tx["inputs"][0]["sig"] = sig

with open("signed_tx.json","w") as f:
    json.dump(tx, f, indent=2)

print("ADDRESS:", addr)
print("PUBLIC KEY HEX:", binascii.hexlify(bytes(pk)).decode())
print("SIGNED TX saved to signed_tx.json")

