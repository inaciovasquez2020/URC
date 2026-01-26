use ed25519_dalek::{SigningKey, VerifyingKey};
use sha2::{Digest, Sha256};
use base58::ToBase58;
use hex::encode;
use rand_core::OsRng;

pub fn keygen() -> (String, String) {
    let mut csprng = OsRng;
    let sk = SigningKey::generate(&mut csprng);
    let vk: VerifyingKey = sk.verifying_key();
    let pk_bytes = vk.to_bytes();

    let pk_hex = encode(pk_bytes);

    let h = Sha256::digest(pk_bytes);
    let addr = h.to_vec().to_base58();

    (pk_hex, addr)
}

