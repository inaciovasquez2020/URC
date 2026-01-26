# Unified Rigidity Coin (URC) — Protocol Specification v0.1

## 1. Ledger Model
- Permissionless PoW
- UTXO-based accounting
- Longest-chain fork choice

## 2. Genesis
Hash: 0000ccee654c8a6076b287006bfb73e21230c66e655a4f4db9c58be56990a48d

## 3. Consensus
Target-based PoW with retarget every N=2016 blocks.

## 4. Transactions
Validity:
Σinputs ≥ Σoutputs  
Fee = Σinputs − Σoutputs

## 5. Networking
Unstructured gossip (TCP, JSON lines).
Message types: tx, block.

## 6. Security Theorem (Declared)
No asymptotic security accumulation:
A(t)=Θ(P(t)), independent of ∫P(s)ds.

## 7. Threat Model
- 51% attack
- Cartelization
- No long-range resistance
