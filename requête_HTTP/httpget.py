#!/usr/bin/python3

import socket
import requests
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = sys.argv[1]
port = 80
s.connect((host, port))
request = "GET / HTTP /1.1\ r\n  Host : " + host + "\r\n  Connection : close \r\n\r\n"
s.sendall(request.encode("utf-8"))
data = s.recv(1024)
print(data)