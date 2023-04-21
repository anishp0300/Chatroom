import threading
import socket

#-----------
#FUNCTIONS
#-----------
def serving_client(client):
    done = False
    while not done:

        msg = receive_messages(client)
        if msg == 'QUIT':
            done = True
            client.close()
            print("Connection with {}:{} has been closed.".format(SERVER,PORT))
        else:
            print(msg)
            client.send(input("message: ").encode('utf-8'))

def receive_messages(client):
	return(client.recv(1024).decode('utf-8'))

PORT=1234
SERVER = "localhost"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((SERVER, PORT))

server.listen()
clients = []
numClients = 0

while True:
    client, addr = server.accept()

    print('Connection has been established with {}'.format(addr))

    client_thread = threading.Thread(target=serving_client, args=(client,))

    client_thread.start()

    #client_thread.join()

client.close()
server.close()
