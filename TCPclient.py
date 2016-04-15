from socket import *
server_name='localhost'
server_port=12000
client_sock=socket(AF_INET,SOCK_STREAM)
client_sock.connect((server_name,server_port))

while 1:
	msg=raw_input('Inserisci una stringa: ')
	client_sock.send(msg)
	if (msg=='.'):
		break
	msg_UC=client_sock.recv(2048)
	print(msg_UC)
client_sock.close()