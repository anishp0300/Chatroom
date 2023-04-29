import threading
import socket

#-----------
#FUNCTIONS
#-----------
def serving_client(client, addr):
    done = False
    while not done:
        msg = receive_messages(client)
        if msg == 'QUIT':
            done = True
            client.close()
            print("Connection with {} has been closed.".format(addr))
        else:
            print("{}: {}".format(addr,msg))
            broadcast_clients(msg, activeClients, client_threads, client, addr)
    
    activeClients.remove(client)
    return

def receive_messages(client):
	return(client.recv(1024).decode('utf-8'))

def broadcast_clients(msg, activeClients, client_threads, sendingClient, sendingAddr):
    for i in range(len(activeClients)):
        if activeClients[i] is not sendingClient:
            activeClients[i].send(
                "{}: {}".format(sendingAddr,msg).encode('utf-8')
                )


PORT=1234
SERVER = "localhost"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((SERVER, PORT))

server.listen()
activeClients = []
client_threads = []

while True:
    client, addr = server.accept()
    activeClients.insert(0, client)

    print('Connection has been established with {}'.format(addr))

    client_threads.insert(0, threading.Thread(target=serving_client, args=(client,addr)))

    client_threads[0].start()

    for thread in client_threads:
        if not thread.is_alive():
            client_threads.remove(thread)

server.close()
