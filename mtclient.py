#!/usr/bin/env python
#-*- coding:utf-8 -*-

import socket
import sys

HOST = '127.0.0.1'
PORT = 8001

def mtclient(name):
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect((HOST,PORT))
	while True:
		cmd = raw_input("please input msg:")
		if len(cmd)==0:
			cmd='null'
		if cmd != 'exit':
			cmd = name+': '+cmd
		s.send(cmd)
		data = s.recv(1024)
		if data == "exit":
			break
		print data
	s.close()

if __name__ == '__main__':
	if len(sys.argv)>=2:
		mtclient(sys.argv[1])
