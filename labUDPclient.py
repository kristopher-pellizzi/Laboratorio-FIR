from socket import *
server_name='localhost'
server_port=12000
#AF=address_family INET= INET DGRAM=pacchetto UDP
client_sock=socket(AF_INET, SOCK_DGRAM)
#settimeout prende come parametro i secondi di timeout da impostare
client_sock.settimeout(3)

msg=raw_input('Inserisci una stringa: ')
#sendto prende due parametri: il messaggio e una tupla che contiene, rispettivamente, nome del server o ip e porta del server
try:
	client_sock.sendto(msg,(server_name,server_port))
#recv prende un parametrO. il numero di byte massimi che si possono ricevere e ritorna il messaggio modificato e informazioni sul'indirizzo del server remoto
	mod_msg,serv_addr=client_sock.recvfrom(2048)

	print(mod_msg)
#error e un tipo di eccezione all'interno della libreria socket--> error==socket.error
#v e una stringa che contiene la versione testuale dell'eccezione
except error,v:
	print (error,v)

finally:
	client_sock.close()