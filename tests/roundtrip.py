import os, binascii, nacl.signing, urc_rs

msg = b"ci-roundtrip"

sk_bytes = os.urandom(32)
sk = nacl.signing.SigningKey(sk_bytes)
vk = sk.verify_key

sig = sk.sign(msg).signature

assert urc_rs.verify_ed25519(
    binascii.hexlify(bytes(vk)).decode(),
    msg,
    binascii.hexlify(sig).decode()
)

print("CI ROUNDTRIP OK")

