def decrypt(ciphertext, tag, nonce):
    from Crypto.Cipher import AES
    from Crypto.Hash import MD5
    key = b'\x9f\xa0xl\x10\x1c\x18\x91H\xdef\xdb\xf5\x9c:\x81'
    cipher = AES.new(key, AES.MODE_CFB, nonce)
    h = MD5.new()
    plaintext = cipher.decrypt(ciphertext)
    h.update(plaintext)
    if (h.digest()==tag):
        print("Message verified")
    else:
        print("Wrong key or message corrupted")
    return plaintext

print(decrypt(')*IO\x91\xa3\xefMZ\xbd\x15H\xb9(\xd2', ';,\xf5\x04\x12\\\xf0o\xa5-p\xe9\x95{A\xd5', '\xde\xde\x18U\xc5\xb5\xe2\x18\x14a2\xac\x17W$\xfa'))
