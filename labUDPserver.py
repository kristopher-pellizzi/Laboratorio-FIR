from socket import *
port=12000

server_sock=socket(AF_INET,SOCK_DGRAM)
#il metodo bind riceve un parametro: una tupla contenete l'indirizzo IP e la porta.
server_sock.bind(('',port))

print('Server is up')

while 1:
	msg,client_addr=server_sock.recvfrom(2048)
	print(client_addr)
	msg_UC=msg.upper()
	server_sock.sendto(msg_UC,client_addr)
