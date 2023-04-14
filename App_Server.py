#This is the code for server side for the chat 
import socket
import threading

PORT = 1234
SERVER = "localhost"

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((SERVER, PORT))
s.listen()   #incase of multiple connections, queue of 5

def start_server():
    print('Connection has been established on {}:{}'.format(SERVER, PORT))

    #listen for conenctions
    while True:
        clientsocket, address= s.accept()      #if anyone connects, accept
        
        print(f"Connection from {address} has been established!")
        clientsocket.send("Welcome to the chat room".encode( "utf-8"))
        
        break
        
        

        #new thread creation for client connections
        #c_thread = threading.Thread(target= handle_client, args=(c_socket, c_address))
        #c_thread.start()
        
    while True:
        inputBuffer = str(input())
        clientsocket.send(inputBuffer.encode("utf-8"))
        # try:
        #     msg = clientsocket.recv(1024)
        #     if msg: 
        #         print(msg.decode("utf-8"))
        
        # except:
        #     print("Error: Closing sockets.")
        #     clientsocket.close()
        #     break
        

def broadcast(message):
    clientsocket.send(message.encode("utf-8"))


#start the server
start_server()
