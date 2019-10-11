import socket                   # Import socket module
import time

s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)             # Create a socket object
host = "fde5:f421:b815:0:8a1d:65a0:e665:d527"  #Ip address that the TCPServer  is there
port = 50000                     # Reserve a port for your service every new transfer wants a new port or you must wait.

s.connect((host, port))
s.send(encrypt(listkey, filelist, listnonce))
time.wait(2)
#give the server a few seconds to begin encrypting files

while True:
    for i in len(filelist):
        if (filelist[i] == "!END!"):
            break
        f = open(filelist[i], 'wb')
        enl = conn.recv(1024)
        while (enl):
            l = decrypt(enl)
            f.write(l)
        f.close()
        conn.send("Next one, please.")
print('Successfully got the file(s)')
s.close()
print('connection closed')
