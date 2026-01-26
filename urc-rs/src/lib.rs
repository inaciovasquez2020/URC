use pyo3::prelude::*;
use ed25519_dalek::{VerifyingKey, SigningKey, Signature, Signer};
use hex::{decode, encode};

#[pyfunction]
fn verify_ed25519(pubkey_hex: &str, msg: &[u8], sig_hex: &str) -> PyResult<bool> {
    let pk_bytes = decode(pubkey_hex)
        .map_err(|e| PyErr::new::<pyo3::exceptions::PyValueError, _>(format!("{e}")))?;
    let sig_bytes = decode(sig_hex)
        .map_err(|e| PyErr::new::<pyo3::exceptions::PyValueError, _>(format!("{e}")))?;

    let pk = VerifyingKey::from_bytes(&pk_bytes.try_into().unwrap())
        .map_err(|e| PyErr::new::<pyo3::exceptions::PyValueError, _>(format!("{e}")))?;
    let sig = Signature::from_bytes(&sig_bytes.try_into().unwrap());

    Ok(pk.verify_strict(msg, &sig).is_ok())
}

#[pyfunction]
fn sign_ed25519(seckey_hex: &str, msg: &[u8]) -> PyResult<String> {
    let sk_bytes = decode(seckey_hex)
        .map_err(|e| PyErr::new::<pyo3::exceptions::PyValueError, _>(format!("{e}")))?;
    let sk = SigningKey::from_bytes(&sk_bytes.try_into().unwrap());
    let sig = sk.sign(msg);
    Ok(encode(sig.to_bytes()))
}

#[pymodule]
fn urc_rs(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(verify_ed25519, m)?)?;
    m.add_function(wrap_pyfunction!(sign_ed25519, m)?)?;
    Ok(())
}

