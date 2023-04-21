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
            # client.send(input("message: ").encode('utf-8'))

def receive_messages(client):
	return(client.recv(1024).decode('utf-8'))

PORT=1234
SERVER = "localhost"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((SERVER, PORT))

server.listen()
numClients = 0

client_threads = []

while True:
    client, addr = server.accept()
    
    print('Connection has been established with {}'.format(addr))

    client_threads.insert(0, threading.Thread(target=serving_client, args=(client,addr)))

    client_threads[0].start()

    #client_thread.join()

    # if input() == "QUIT":
    #     break

client.close()
server.close()
