
import socket                   # Import socket module

s = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)             # Create a socket object
host = "fde5:f421:b815:0:8a1d:65a0:e665:d527"  #Ip address that the TCPServer  is there
port = 50000                     # Reserve a port for your service every new transfer wants a new port or you must wait.

s.connect((host, port))
s.send("Hello server!")

with open('received_file', 'wb') as f:
    print 'file opened'
    while True:
        print('receiving data...')
        data = s.recv(1024)
        print('data=%s', (data))
        if not data:
            break
        # write data to a file
        f.write(data)

f.close()
print('Successfully get the file')
s.close()
print('connection closed')
