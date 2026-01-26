# URC Security Analysis

## Threat Model
Adversary controls the network and may have arbitrary compute power.

## Attack Surfaces
1. 51% hash attack → reorg/censorship.
2. Eclipse → isolate node, censor mempool.
3. Long-range → no historical binding once power drops.
4. Cartelization → economic capture.

## Invariants
1. Signature validity:
   verify(pubkey, canon(tx with sig=""), sig) must hold.
2. Ownership:
   input.pubkey must equal UTXO.pubkey.
3. Conservation:
   Σinputs ≥ Σoutputs (fee = difference).
4. Fork choice:
   maximize cumulative difficulty.
5. Declared limitation:
   no asymptotic security accumulation.

## Non-Claims
URC does NOT claim compounding security, permanent decentralization, or state-resistance.
