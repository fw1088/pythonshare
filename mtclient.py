#!/usr/bin/env python
#-*- coding:utf-8 -*-

import socket
import sys
import threading
import time
HOST = '127.0.0.1'
PORT = 8888

def mtclient(name,test):
    counter = 1800
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((HOST,PORT))
    while True:
        time.sleep(1)
        counter=counter+1
        cmd = 'test'+str(counter)+'\n\r'
        s.send(cmd)
        if counter == 2000:
            break
        cmd=0
        result=s.recv(1024)
        if result == 'exit':
            break
    s.close()

if __name__ == '__main__':
	if len(sys.argv)>=2:
                for i in range(60):
                    handleThread = threading.Thread(target=mtclient,args=(sys.argv[1]))
                    handleThread.start()
