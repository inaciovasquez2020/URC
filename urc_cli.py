import sys, json
from urc_wallet import genkey, address
from urc_snapshot import import_snapshot

cmd = sys.argv[1]

if cmd=="keygen":
    sk, pk = genkey()
    print("ADDRESS:", address(pk))

elif cmd=="balance":
    addr = sys.argv[2]
    snap = import_snapshot()
    bal = sum(v["amount"] for v in snap["utxo"].values() if v["address"]==addr)
    print("BALANCE:", bal)

elif cmd=="peers":
    from urc_peers import initial_peers
    print("PEERS:", initial_peers())
