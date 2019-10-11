from Crypto.Cipher import AES
from Crypto.Hash import MD5
from Crypto.Random import get_random_bytes
import socket

def encrypt (key, data, nonce):
    file_out = b''
    cipher = AES.new(key, AES.MODE_EAX, nonce)
    ciphertext, tag = cipher.encrypt_and_digest(data.encode("utf8"))
    file_out=b''
    for x in (key, cipher.nonce, tag, ciphertext):
        file_out+=x
    return file_out

def decrypt(data):
    import io
    file_in = io.BytesIO(data)
    key, nonce, tag, ciphertext = [ file_in.read(x) for x in (16, 16, 16, -1) ]
    #Since the key, nonce, and tag are the first 48 bytes, these are read first
    cipher2 = AES.new(key, AES.MODE_EAX,nonce)
    data = cipher2.decrypt_and_verify(ciphertext, tag)
    return (data.decode("utf8"), key, nonce)
    #the function also returns key and nonce, which is needed by the server

def encryptFile(fileseek, filedest, key, nonce):
    f = open(fileseek, 'rb')
    enf = open(filedest, 'wb')
    l = f.read(976)
    #overhead of 48, with key, nonce, and tag appended to the front
    while (l):
        enl = encrypt(key, l, nonce)
        enf.write(enl)
        l = f.read(976)
        
def decryptFile(fileseek, filedest):
    enf = open(fileseek, 'rb')
    f = open(filedest, 'wb')
    enl = enf.read(1024)
    while (enl):
        l, _, _ = decrypt(enl)
        f.write(l)
        enl = enf.read(1024)

port = 50000                    # Reserve a port for your service every new transfer wants a new port or you must wait.
s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)             # Create a socket object
host = "fd6f:889a:7d45:0:4284:29b5:9169:2c72"   # Get local machine name
s.bind((host, port))            # Bind to the port
s.listen(5)                     # Now wait for client connection.

print ('Server listening....')


while True:
    conn, addr = s.accept()     # Establish connection with client.
    print ('Got connection from ', addr)
    ciphermsg = conn.recv(1024)
    msg, key, nonce = decrypt(ciphermsg)
    print(msg)
    try:
        while (msg.upper().strip() != 'END'):
            print("Received")
            f = open(msg, 'rb')
            print("Opened")
            l = f.read(1024-48)
            cipher = encrypt(key, l, nonce)
            #overhead of 48 bytes
            print("Encrypted")
            conn.send(cipher)
            print("Sent")
            f.close()
            print("Closed")
            print("Listening")
            ciphermsg = conn.recv(1024)
            msg, key, nonce = decrypt(ciphermsg)
        else:
            break
    except Exception:
        print("Error, ending server session.")
        print(Exception)
        break
    s.close()
