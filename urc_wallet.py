import nacl.signing, base58, hashlib

def genkey():
    sk = nacl.signing.SigningKey.generate()
    pk = sk.verify_key
    return sk, pk

def address(pk):
    h = hashlib.sha256(bytes(pk)).digest()
    return base58.b58encode(h).decode()

def sign(sk, msg):
    return sk.sign(msg).signature.hex()

def verify(pk_hex, msg, sig_hex):
    import nacl.signing, binascii
    pk = nacl.signing.VerifyKey(binascii.unhexlify(pk_hex))
    pk.verify(msg, binascii.unhexlify(sig_hex))
    return True

