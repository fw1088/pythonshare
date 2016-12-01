#client
#!/usr/bin/env python
#-*- coding:utf-8 -*-
import socket
HOST = '127.0.0.1'
PORT = 8888

while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    while True:
	cmd = raw_input("Please input msg:")
        if len(cmd)==0:
	    cmd="null"
        s.send(cmd)
        data = s.recv(1024)
        if data == "exit":
	    break
	print data
    break
s.close()
