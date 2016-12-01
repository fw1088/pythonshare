#!/usr/bin/env python
#-*- coding:utf-8 -*-

import socket
import sys
import threading
import time
HOST = '127.0.0.1'
PORT = 8888

def mtclient(name,test):
        counter = 0
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect((HOST,PORT))
	while True:
                #time.sleep(1)
                counter=counter+1
		cmd = 'crl'+str(counter)#raw_input("please input msg:")
		if len(cmd)==0:
			cmd='null'
		if cmd != 'exit':
			cmd = name+': '+cmd
		s.send(cmd)
	s.close()

if __name__ == '__main__':
	if len(sys.argv)>=2:
                for i in range(20):
                    handleThread = threading.Thread(target=mtclient,args=(sys.argv[1]))
                    handleThread.start()
