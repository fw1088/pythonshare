#http://www.cnblogs.com/coser/archive/2012/01/06/2315216.html
import select
import socket
import Queue

server = socket.socket(sock.AF_INET,sock.SOCK_STREAM)
server.setblocking(False)
server.setsockopt(socket.SOL_SOCKET,sock.SO_REUSEADDR,1)
server_address = ('127.0.0.1',8888)
server.bind(server_adddress)
server.listen(10)

inputs = [server]

outputs = []

message_queues = []

timeout = 20

while inputs:
	print "waiting for next event"
	readable, writable, exceptional = select.select(inputs, outputs, inputs,timeout)
	
	if not (readable or writable or exceptional):
		print "Time out !"
		break
	for s in readable:
		if s is server:
			connection, client_address = s.accept()
			print "connection from", client_address
			connection.setblocking(0)
			inputs.append(connection)
			message_queues[connection] = Queue.Queue()
		else:
			data = s.recv(1024)
			if data:
				print "received ",data,"from",s.getpeername()
				message_queues[s].put(data)
			if s not in outputs:
				outputs.append(s)
			
