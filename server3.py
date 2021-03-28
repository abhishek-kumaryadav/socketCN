import socket
import errno
import sys
import select
import threading

if len(sys.argv) == 3:
    s = socket.socket
    host = sys.argv[1]
    port = int(sys.argv[2])
    selectBuffer = []
    # AF_INET for ipv4 and SOCK_STREAM for TCP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # s.setblocking(0)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            # Associate the socket with a specific network interface and port number
            # Accepts a two-touple (host,port)
            # Host can be a hostname, IP address, or empty string
            # Port 1-65535 Unpriviledge ports >1024
            s.bind((host, port))
            print("Socket binded to port:", port)

            selectBuffer.append(s)

            # listen() enables a server to accept() connections.
            # It makes it a “listening” socket
            # Backlog parameter as 0, max unaccepted connections before refusing
            s.listen(1)
            print("Listening at {}:{}".format(host, port))

            while True:
                # Select from selectBuffer
                # try:

                # except:
                #     pass
                # print(selectBuffer)

                r_sockets, w_sockets, e_sockets = select.select(selectBuffer, [], [])

                for soc in r_sockets:

                    if soc is s:
                        conn, addr = soc.accept()
                        # conn.setblocking(0)
                        print("Received request from {}".format(addr))
                        # conn.settimeout(30)
                        selectBuffer.append(conn)
                    elif soc != -1:

                        data = soc.recv(1024)
                        decodedData = data.decode()
                        # print(data)
                        if data:
                            print("Data received: {}".format(decodedData))
                        else:
                            selectBuffer.remove(soc)
                            soc.close()
                            break
                        # DO MATHS HERE
                        try:
                            toSend = str(eval(decodedData))
                        except:
                            toSend = "INVALID INPUT"
                        # send back string to client
                        soc.send(toSend.encode())
                        print("Response sent = {}".format(toSend))

                    # connection closed

        except socket.error as e:
            if e.errno == errno.EADDRINUSE:
                print("Port {} is already in use".format(port))
            else:
                # something else raised the socket.error exception
                print(e)

    s.close()


else:
    print("Invalid Arguments: python server4.py 'address' 'port'")
