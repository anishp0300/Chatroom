#This is the code for server side for the chat 
import socket
import threading

PORT = 1234
SERVER = "localhost"

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((SERVER, PORT))
s.listen(5)   #incase of multiple connections, queue of 5

def start_server():
    print('Connection has been established on {}:{}'.format(SERVER, PORT))

    #listen for conenctions
    while True:
        clientsocket, address= s.accept()      #if anyone connects, accept
        print(f"Connection from {address} has been established!")
        clientsocket.send(bytes("Welcome to the chat room", "utf-8"))

        #new thread creation for client connections
        #c_thread = threading.Thread(target= handle_client, args=(c_socket, c_address))
        #c_thread.start()

#start the server
start_server()

#test github push