import threading
import socket

#-----------#
#FUNCTIONS#
#-----------#

def serving_client(client, addr):
    done = False
    while not done:
        msg = receive_messages(client)
	
	# Close the client connection if this keyword is entered
        if msg == 'QUIT':
            done = True
            client.close()
            print("Connection with {} has been closed.".format(addr))
	
	
        else:  # If a connection is not closed, broadcast the message to all active threads/ clients
            print("{}: {}".format(addr,msg))
            broadcast_clients(msg, activeClients, client_threads, client, addr)
    
    activeClients.remove(client)
    return

# Function to receive messages upto 1024 bytes
def receive_messages(client):
	return(client.recv(1024).decode('utf-8'))

# Fucntion to broadcast a message to all connected clients except the sending client
def broadcast_clients(msg, activeClients, client_threads, sendingClient, sendingAddr):
    for i in range(len(activeClients)):
        if activeClients[i] is not sendingClient:  # The message on the sending client is not broadcasted to itself. It broadcasts to all other active clients
            activeClients[i].send(   
                "{}: {}".format(sendingAddr,msg).encode('utf-8')
                )


PORT=1234
SERVER = "localhost"

# starting the server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((SERVER, PORT))

server.listen()
# Keep track of active clients and the threads that handle their messages
activeClients = []   
client_threads = []

while True:
    client, addr = server.accept()  # The server accepts incoming client connections
    activeClients.insert(0, client)

    print('Connection has been established with {}'.format(addr))
    
    # Start a new thread to handle messages from the client
    client_threads.insert(0, threading.Thread(target=serving_client, args=(client,addr)))

    client_threads[0].start()

    for thread in client_threads:  
        if not thread.is_alive(): # If a thread is inactive and client not connected to the server 
            client_threads.remove(thread)  # Remove the thread since that client is not active

# Server is closed
server.close()
