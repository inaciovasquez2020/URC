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
