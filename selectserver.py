import select
import socket
import Queue
import time
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setblocking(False)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server_address = ('127.0.0.1',8888)
server.bind(server_address)
server.listen(20)

inputs = [server]

outputs = []

message_queues = {}

timeout = 6000

while inputs:
    #print "waiting for next event"
    readable, writable, exceptional = select.select(inputs,outputs,inputs,timeout)
    if not (readable or writable or exceptional):
        print "Time out!"
        break
    for s in readable:
        if s is server:
            connection, client_address = s.accept()
            #print "connection from", client_address
            connection.setblocking(0)
            inputs.append(connection)
            message_queues[connection] = Queue.Queue()
        else:
            try:
                data = s.recv(1024)
                if data:
                    print data
                    message_queues[s].put(data)
                    if s not in outputs:
                        outputs.append(s)
            except socket.error,e:
                    if s in outputs:
                        outputs.remove(s)
                    if s in inputs:
                        inputs.remove(s)
                    s.close()
                #print "closing",client_address
                #if s in outputs:
                   # outputs.remove(s)
                #inputs.remove(s)
                #s.close()
                #del message_queues[s]
    for s in writable:
        if message_queues[s].empty() == False:
            next_msg = message_queues[s].get_nowait()
            #print "sending",next_msg,"to",s.getpeername()   
            try:
                s.send(next_msg)
            except socket.error,e:
                if s in outputs:
                    outputs.remove(s)
                if s in inputs:
                    inputs.remove(s)
                s.close()
    for s in exceptional:
        print "exception condition on",s.getpeername()
        inputs.remove(s)
        if s in outputs:
            outputs.remove(s)
        s.close()
	del message_queues[s]
