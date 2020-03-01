#!/usr/bin/python3

import socket

s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM, 0)
s.bind(("", 7777))
s.listen(1)
c, addr = s.accept()
while (1):
    data = c.recv(1500)
    if (data == 0):
        break
    c.send(data)
    c.close()