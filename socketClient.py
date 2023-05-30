# echo-client.py
# https://realpython.com/python-sockets/#:~:text=Sockets%20and%20the%20socket%20API,own%20connections%20to%20other%20networks.

import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    s.sendall(b"Hello, world")
    data = s.recv(1024)
    print(f"Received {data!r}")
    s.sendall(b"Hello, world 2")
    data = s.recv(1024)
    print(f"Received {data!r}")
 
