# Client Server Socket Programmings


### CN CSL317
Instructor Name: Dr. Anshul Agarwal
Summer 2021


Abhishek Kumar Yadav
BT18CSE106

---


## Requirements
Install python in your environment if not already installed:
```pip install python```


---

## How To Run 
* Each of the server files can be run using:
```python serverx.py "host" "port"```
* Client files can be run using:
```python client.py "host" "port"```


---

## Demo
### server1.py
![](https://i.imgur.com/HMlo7JB.png)
Left console: server1.py,
Right console: first client
Top console: second client, trying to connect.

I have used ```socket.listen(0)```(doesn't keep pending requests when already having a connection) to implement connection refusal when having a connection already.
If that does'nt work, there is timeout provided in client, which wait for 2 seconds and if it doesn't receive any response it terminates. Connection is closed when client closes the connection.

### server2.py
![](https://i.imgur.com/YN62i7U.png)

Top: server2.py
Left: concurrently connected, invalid input
Right: concurrently connected, valid input

Each connection spawns it's own thread and engages the client. Connection is closed when client closes the connection.

### server3.py
![](https://i.imgur.com/zVjpsuj.png)
Top: server2.py
Left: concurrently connected, valid input
Right: concurrently connected, invalid input

* Every socket is added to the buffer including server socket.
* Socket is selected using select function.
    * If socket is server
        * We accept the connection in it and append it to buffer.
    * If socket is client data is taken from the socket
        * If data is present, output is sent,
        * If data is not present then the socket is removed from buffer and connection is closed.

### server4.py
![](https://i.imgur.com/jprrYuf.png)

### Port already occupied
![](https://i.imgur.com/1ErbVoa.png)

### Server not started
![](https://i.imgur.com/PgTTEg9.png)

### Expression evaluation
For evaluating the mathematical expression the string is simply passed to ```eval()``` function available with python, so the server is capable to solving any type of equation.

---


## Acknowledgement
* https://www.positronx.io/create-socket-server-with-multiple-clients-in-python/
* https://steelkiwi.com/blog/working-tcp-sockets/
* https://yasoob.me/2013/08/06/python-socket-network-programming/
* https://docs.python.org/3/library/socket.html
* https://www.techbeamers.com/python-tutorial-write-multithreaded-python-server/
* https://docs.python.org/3/tutorial/errors.html
* https://docs.python.org/3/library/multiprocessing.html
* https://realpython.com/python-sockets/#echo-client-and-server