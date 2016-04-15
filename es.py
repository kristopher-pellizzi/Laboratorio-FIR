from socket import *
server_name='localhost'
server_port=12001

client_sock=socket(AF_INET,SOCK_DGRAM)
client_sock.settimeout(3)

msg=raw_input('Inserisci una stringa: ')

try:
	client_sock.sendto(msg,(server_name,server_port))
	mod_msg,server_addr=client_sock.recvfrom(2048)
	print(mod_msg)

except error,v:
	fh=open('log.txt','a')
	fh.write('Errore\n')
	fh.close()

finally:
	client_sock.close()