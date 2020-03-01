#!/usr/bin/python3

import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = sys.argv[1]
port = 80
try:
    s.connect((host, port))
except Exception as e:
    print(e)
    exit(-1)
request = "GET / HTTP/1.1\r\n"  \
    "Host: " + host + "\r\n"    \
    "Connection: close\r\n\r\n"
s.sendall(request.encode("utf-8"))
answer = s.recv(1024)
while (answer != b""):
    # affichage en byte array
    print(answer.decode("utf-8"), end="")
    answer = s.recv(1024)
