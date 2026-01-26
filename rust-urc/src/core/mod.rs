use ed25519_dalek::{SigningKey, VerifyingKey, Signature, Signer};
use hex::{decode, encode};

pub fn sign_msg(sk_hex: &str, msg: &[u8]) -> String {
    let sk_bytes = decode(sk_hex).unwrap();
    let sk = SigningKey::from_bytes(&sk_bytes.try_into().unwrap());
    let sig: Signature = sk.sign(msg);
    encode(sig.to_bytes())
}

pub fn verify_sig(pubkey_hex: &str, msg: &[u8], sig_hex: &str) -> bool {
    let pk_bytes = decode(pubkey_hex).unwrap();
    let sig_bytes = decode(sig_hex).unwrap();

    let pk = VerifyingKey::from_bytes(&pk_bytes.try_into().unwrap()).unwrap();
    let sig = Signature::from_bytes(&sig_bytes.try_into().unwrap());

    pk.verify_strict(msg, &sig).is_ok()
}

