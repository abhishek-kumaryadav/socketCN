import socket
from _thread import *
import threading
import sys
import errno

# print_lock = threading.Lock()


def threaded(c, addr):
    while True:
        data = c.recv(1024)
        decodedData = data.decode()
        # print(data)
        if data:
            print("Data received: {}".format(decodedData))
        else:
            # print_lock.release()
            break
        # DO MATHS HERE
        try:
            toSend = str(eval(decodedData))
        except:
            toSend = "INVALID STATEMENT"
        c.sendall(toSend.encode())
        print("Response sent to {} = {}".format(addr, toSend))

    # connection closed
    c.close()


def Main():
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
                print("{}:{} is listening".format(host, port))

                # a forever loop until client wants to exit
                while True:

                    # returns a new socket object and a tuple holding the (host, port) of the client
                    c, addr = s.accept()
                    print("Connected to {}".format(addr))
                    # Receiving data

                    # lock acquired by client
                    # print_lock.acquire()

                    # Start a new thread and return its identifier
                    # my python formatter does this
                    # start_new_thread(
                    #     threaded,
                    #     (c, addr),
                    # )
                    threading.Thread(target=threaded, args=(c, addr)).start()
            except socket.error as e:
                if e.errno == errno.EADDRINUSE:
                    print("Port {} is already in use".format(port))
                else:
                    # something else raised the socket.error exception
                    print(e)

        s.close()
    else:
        print("Invalid Arguments: python server4.py 'address' 'port'")


if __name__ == "__main__":
    Main()