import json, hashlib, os

TARGET0 = 2**240

def canon(obj):
    return json.dumps(
        obj,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False
    ).encode("utf-8")

def sha256_hex(obj):
    return hashlib.sha256(canon(obj)).hexdigest()

def valid_pow(header):
    return int(sha256_hex(header), 16) < TARGET0

def mine_header(header):
    while not valid_pow(header):
        header["nonce"] += 1
    return header, sha256_hex(header)

def coinbase_tx(height, address="MINER", amount=50):
    return {"inputs": [], "outputs": [{"address": address, "amount": amount}]}

def write_json(path, obj):
    with open(path, "w") as f:
        json.dump(obj, f, indent=2, sort_keys=True)

def write_sha256_file(path, hexhash):
    with open(path + ".sha256", "w") as f:
        f.write(f"{hexhash}  {os.path.basename(path)}\n")

def main():
    genesis = {
        "name": "Unified Rigidity Coin",
        "ticker": "URC",
        "seed": "URC::GENESIS::2026-01-26::V1",
        "height": 0,
        "time": 1706250000,
        "difficulty": 2,
        "nonce": 0,
        "parent": "0"*64
    }
    genesis, gh = mine_header(genesis)

    chain = []
    chain.append({"header": genesis, "hash": gh, "txs": [coinbase_tx(0, "GENESIS")]})

    prev = chain[-1]
    for _ in range(10):  # mine blocks 1..10
        header = {
            "name": "Unified Rigidity Coin",
            "ticker": "URC",
            "seed": "",
            "height": prev["header"]["height"] + 1,
            "time": prev["header"]["time"] + 600,
            "difficulty": 2,
            "nonce": 0,
            "parent": prev["hash"]
        }
        header, hh = mine_header(header)
        blk = {"header": header, "hash": hh, "txs": [coinbase_tx(header["height"])]}
        chain.append(blk)
        prev = blk

    write_json("genesis.json", chain[0])
    write_sha256_file("genesis.json", chain[0]["hash"])
    write_json("chain_0_10.json", chain)

    print("genesis nonce:", chain[0]["header"]["nonce"])
    print("genesis hash :", chain[0]["hash"])
    print("tip height   :", chain[-1]["header"]["height"])
    print("tip hash     :", chain[-1]["hash"])

if __name__ == "__main__":
    main()
