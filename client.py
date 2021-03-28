import socket
import sys

if len(sys.argv) == 3:
    s = socket.socket
    host = sys.argv[1]
    port = int(sys.argv[2])

    # Creating an IPv4 TCP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        # Client times out if connection is not accepted within 2 seconds
        s.settimeout(2)

        # Take a touple (host, port) as input
        s.connect((host, port))
        print("Connected to {}:{}".format(host, port))

        while True:
            data = input("Enter Equation")

            # Data is encoded before sending so it in bytes format
            s.sendall(data.encode())
            print("Sending {} to {}:{}".format(data, host, port))

            # recv() takes buffersize as argument
            retData = s.recv(1024).decode()
            print("Received : {} from {}:{}".format(repr(retData), host, port))

        s.close()
        print("Connection closed to {}:{}".format(host, port))

else:
    print("Invalid Arguments: python client.py 'host' 'port' 'equation'")