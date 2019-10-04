def encrypt(plaintext):
    from Crypto.Cipher import AES
    from Crypto.Hash import MD5
    import os
    nonce = os.urandom(16)
    key = b'\x9f\xa0xl\x10\x1c\x18\x91H\xdef\xdb\xf5\x9c:\x81'
    cipher = AES.new(key, AES.MODE_CFB, nonce)
    h = MD5.new()
    print(plaintext)
    ciphertext = cipher.encrypt(plaintext)
    h.update(plaintext)
    tag = h.digest()
    return (ciphertext, tag, nonce)
print(encrypt("Attack at dawn."))
