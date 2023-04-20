
import socket

PORT=1234
SERVER = "localhost"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((SERVER, PORT))

server.listen()
clients = []
numClients = 0

while True:
    client, addr = server.accept()

    print('Connection has been established on {}:{}'.format(SERVER, PORT))

    done = False
    while not done:

        msg = (client.recv(1024).decode('utf-8'))
        if msg == 'QUIT':
            done = True
            client.close()
            print("Connection with {}:{} has been closed.".format(SERVER,PORT))
        else:
            print(msg)
            client.send(input("message: ").encode('utf-8'))

client.close()
server.close()
