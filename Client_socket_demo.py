#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016-11-02 22:40
# @Author  : Steve.Yang
# @File    : Client_socket_demo.py
# @Software: PyCharm Community Edition
import socket
import time
import sys
#RPi's IP
SERVER_IP = "192.168.1.1"
SERVER_PORT = 8888

print("Starting socket: TCP...")
server_addr = (SERVER_IP, SERVER_PORT)
socket_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

while True:
    try:
        print("Connecting to server @ %s:%d..." %(SERVER_IP, SERVER_PORT))
        socket_tcp.connect(server_addr)
        break
    except Exception:
        print("Can't connect to server,try it latter!")
        time.sleep(1)
        continue

print("Please input commands:")
while True:
    try:
        data = socket_tcp.recv(1024)
        if len(data)>0:
            print(data)
            command = input().encode('utf-8')
            socket_tcp.send(command)
            time.sleep(1)
        continue
    except Exception:
        socket_tcp.close()
        socket_tcp=None
        sys.exit(1)