def encrypt(data):
    from Crypto.Cipher import AES
    from Crypto.Random import get_random_bytes
    key = b'\x9f\xa0xl\x10\x1c\x18\x91H\xdef\xdb\xf5\x9c:\x81'
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data.encode("utf8"))
    file_out=b''
    for x in (cipher.nonce, tag, ciphertext):
        file_out+=x

    return file_out
data=encrypt('Hello world!')
print(data)
