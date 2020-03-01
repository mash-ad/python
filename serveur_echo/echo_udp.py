#!/usr/bin/python3

import socket

s = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
s.bind(("", 7777))
while (1):
    data, addr = s.recvfrom(1500)
    if (data == 0):
        break
    s.sendto(data, addr)