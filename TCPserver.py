from socket import *
import thread

def handler(client_sock):
	while 1:
		msg=client_sock.recv(2048)
		if(msg=='.'):
			break
		msg_UC=msg.upper()
		client_sock.send(msg_UC)
	print('Disconnected host: '+str(client_addr[0])+':'+str(client_addr[1]))
	client_sock.close()

port=12000
server_sock=socket(AF_INET,SOCK_STREAM)
server_sock.bind(('',12000))
server_sock.listen(1)
print("Server is up")
while 1:
	client_sock,client_addr=server_sock.accept()
	print('Connected host: '+str(client_addr[0])+':'+str(client_addr[1]))
	thread.start_new_thread(handler,(client_sock,))