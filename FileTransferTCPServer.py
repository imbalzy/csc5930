import socket                   # Import socket module

port = 50000                    # Reserve a port for your service every new transfer wants a new port or you must wait.
s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)             # Create a socket object
host = "fde5:f421:b815:0:8a1d:65a0:e665:d527"   # Get local machine name
s.bind((host, port))            # Bind to the port
s.listen(5)                     # Now wait for client connection.

print 'Server listening....'


while True:
    conn, addr = s.accept()     # Establish connection with client.
    print 'Got connection from', addr
    data = conn.recv(1024)
    print('Server received', repr(data))
    _, listkey, listnonce = decrypt(data)
    filelist, _, _ = decrypt(data).split('/n')

    for i in len(filelist):
        if (filelist[i] == "!END!"):
            break
        encryptFile(filelist[i], "en"+filelist[i], key, nonce)
        enf = open("en"+filelist[i], 'rb')
        enl = enf.read(1024)
        while (enl):
            conn.send(enl)
            enl = enf.read(1024)
        enf.close()
        while (!conn.recv(1024)):
            #wait for client to say send more
            pass

    print('Done sending')
    conn.send('Thank you for connecting')
    conn.close()

