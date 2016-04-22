from socket import *

port=12000
server_sock=socket(AF_INET,SOCK_STREAM)
server_sock.bind(('',port))
server_sock.listen(1)
print("server is up")
while 1:
	client_sock,client_addr=server_sock.accept()
	i=0
	while 1:
		msg=client_sock.recv(1024)
		i=i+1
		if(msg=='.'):
			break
		print(str(i)+"-->"+msg)
	print("End Of Stream\n")
	client_sock.close()