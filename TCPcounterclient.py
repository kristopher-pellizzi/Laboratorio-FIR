from socket import *
from time import *

server_name='localhost'
server_port=12000
client_sock=socket(AF_INET,SOCK_STREAM)
client_sock.connect((server_name,server_port))
for i in range(100):
	client_sock.send('A')
	sleep(0.002)
sleep(1)
client_sock.send('.')
client_sock.close()