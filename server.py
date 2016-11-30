#!/usr/bin/env python
# -*-coding:utf-8 -*-
import socket

hint = '''本例子演示了基本的socket操作
不过有个缺陷，为了保持长连接
只能处理一个客户端，如果要处理
多个客户端，需要使用多线程和多进程模型
或者使用epoll,select,poll模型
'''
HOST = '127.0.0.1'
PORT = 8001

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)
print '*********************************'
print hint
print '*********************************'
print 'Server start at: %s:%s' %(HOST, PORT)
print 'welcome to meituan'
print '---**MeiTuan**--'
print '----------------'
print 'wait for connection...'
result = 0
while True:
    result = 0
    conn, addr = s.accept()
    print 'Connected by ', addr
    while True:   
 	data = conn.recv(1024)
    	if data != "null":
            print data
	if data ==  "exit":
	    conn.send("exit")
	    break	
        try:
            conn.send("server received you message.")
        except socket.error, e:
	    result = 1
	    break
    if result == 1:
	continue
    else:
	print 'I will leave,bye'
	break
conn.close()
