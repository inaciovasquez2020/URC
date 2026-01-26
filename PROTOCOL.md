# Unified Rigidity Coin (URC) — Protocol Contract (Normative)

## Core Invariants
1. Cryptographic ownership:
   spend(u) valid => input.pubkey = UTXO.pubkey

2. Ed25519 authentication:
   Verify(pubkey, canon(tx with sig=""), sig) = true

3. No inflation:
   Σinputs.amount ≥ Σoutputs.amount

4. No double-spend:
   each UTXO key may be spent at most once (block + mempool)

5. Checkpoint safety:
   if height ∈ CHECKPOINTS then block.hash = CHECKPOINTS[height]

6. PoW validity:
   int(SHA256(canon(header)),16) < TARGET0

7. Fee-based mempool ordering:
   tx1 ≺ tx2 iff fee(tx1)/|canon(tx1)| > fee(tx2)/|canon(tx2)|
