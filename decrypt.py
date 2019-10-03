def decrypt(data):
    from Crypto.Cipher import AES
    import io
    file_in = io.BytesIO(data)
    nonce, tag, ciphertext = [ file_in.read(x) for x in (16, 16, -1) ]
    key = b'\x9f\xa0xl\x10\x1c\x18\x91H\xdef\xdb\xf5\x9c:\x81'
    cipher2 = AES.new(key, AES.MODE_EAX,nonce)
    data = cipher2.decrypt_and_verify(ciphertext, tag)
    print(data.decode("utf8"))

decrypt(b'\xe2\xb1\xf6G\xe6\x8b\xaa9Xc[\xc6\xd47\x8b\xcc\xf2\x92\xde\x94\xfe\x88\xb7c\xff\x10\xb2\x13\xda\xf7\x1e\xb4\xfd\xa1\xde\xfdQ\xa7\x9f\x99\x98hV\xc8')
