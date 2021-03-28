from os import execve
import socket
import errno
import sys

if len(sys.argv) == 3:
    s = socket.socket
    host = sys.argv[1]
    port = int(sys.argv[2])
    # AF_INET for ipv4 and SOCK_STREAM for TCP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            # Associate the socket with a specific network interface and port number
            # Accepts a two-touple (host,port)
            # Host can be a hostname, IP address, or empty string
            # Port 1-65535 Unpriviledge ports >1024
            s.bind((host, port))
            print("Socket binded to port:", port)

            # listen() enables a server to accept() connections.
            # It makes it a “listening” socket
            # Backlog parameter as 0, max unaccepted connections before refusing
            s.listen(0)
            # This should refuse any second connection however it didnt

            while True:
                print("Listening at {}:{}".format(host, port))
                # returns a new socket object and a tuple holding the (host, port) of the client
                conn, addr = s.accept()

                with conn:
                    print("Connected to {}".format(addr))
                    # Receiving data

                    while True:
                        data = conn.recv(1024)
                        decodedData = data.decode()
                        if data:
                            print("Data received: {}".format(decodedData))
                        else:
                            break
                        # DO MATHS HERE
                        try:
                            toSend = str(eval(decodedData))
                        except:
                            toSend = "INVALID STATEMENT"
                        conn.sendall(toSend.encode())
                        print("Response sent to {} = {}".format(addr, toSend))
                # Closing the connection
                conn.close()

        except socket.error as e:
            if e.errno == errno.EADDRINUSE:
                print("Port {} is already in use".format(port))
            else:
                # something else raised the socket.error exception
                print(e)
    s.close()


else:
    print("Invalid Arguments: python server4.py 'address' 'port'")
