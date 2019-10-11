from Crypto.Cipher import AES
from Crypto.Hash import MD5
from Crypto.Random import get_random_bytes
import socket

filelist = ""
filecount = 0
listkey = get_random_bytes(16)
#print(key)
#printing key while in PuTTY occasionally closes the session
listnonce = get_random_bytes(16)
listtag = ""
while True:
    strinput = str(raw_input("Type file's full path. Otherwise, type !END! for file transfer. "))
    if (strinput == "!END!"):
        break
    filelist += strinput + "\n"
    filecount += 1
filelist = filelist + "!END!"

def encrypt (key, data, nonce):
    file_out = b''
    cipher = AES.new(key, AES.MODE_EAX, nonce)
    ciphertext, tag = cipher.encrypt_and_digest(data.encode("utf8"))
    file_out=b''
    for x in (key, cipher.nonce, tag, ciphertext):
        file_out+=x
    return file_out

print(filelist)
cipherfilelist = encrypt(listkey, filelist, listnonce)
print(cipherfilelist)

def decrypt(data):
    import io
    file_in = io.BytesIO(data)
    key, nonce, tag, ciphertext = [ file_in.read(x) for x in (16, 16, 16, -1) ]
    #Since the key, nonce, and tag are the first 48 bytes, these are read first
    cipher2 = AES.new(key, AES.MODE_EAX,nonce)
    data = cipher2.decrypt_and_verify(ciphertext, tag)
    return (data.decode("utf8"))

plainfilelist = decrypt(cipherfilelist)
print (plainfilelist)

def encryptFile(fileseek, filedest, key, nonce):
    f = open(fileseek, 'rb')
    enf = open(filedest, 'wb')
    l = f.read(976)
    #overhead of 48, with key, nonce, and tag appended to the front
    while (l):
        enl = encrypt(key, l, nonce)
        enf.write(enl)
        l = f.read(976)

target = encryptFile("target1", "target2", listkey, listnonce)
print(target)
        
def decryptFile(fileseek, filedest):
    enf = open(fileseek, 'rb')
    f = open(filedest, 'wb')
    enl = enf.read(1024)
    while (enl):
        l = decrypt(encl)
        f.write(l)
        enl = enf.read(1024)

decryptFile("target2", "target3")
#Success!!
#The key and nonce are randomly generated every time: At one point, the client and server
#Will need to communicate with each other the key and nonce
#That means any easedropper can decrypt these messages, the point is that
#These messages are encrypted
