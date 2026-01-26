import sys, os, json
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from urc_chain import Chain
from urc_snapshot import export_snapshot
from urc_node import mine_header
from urc_validate import validate_block

# load base chain
with open("chain_0_10.json") as f:
    chain_data = json.load(f)

# load signed tx
with open("signed_tx.json") as f:
    tx = json.load(f)

genesis = chain_data[0]
c = Chain(genesis)
for b in chain_data[1:]:
    c.add_block(b)

prev = c.blocks[c.best_tip()]

header = {
    "name":"Unified Rigidity Coin",
    "ticker":"URC",
    "seed":"",
    "height": prev["header"]["height"]+1,
    "time": prev["header"]["time"]+600,
    "difficulty":2,
    "nonce":0,
    "parent": prev["hash"]
}

header, h = mine_header(header)
block = {"header":header,"hash":h,"txs":[tx]}

validate_block(prev, block, c.utxo)
c.add_block(block)
export_snapshot(c)

print("INTEGRATION TEST PASSED")
