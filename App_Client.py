import socket


SERVER= "localhost"
PORT = 1234

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((SERVER, PORT))

done = False
while not done:


    print("-Connection Established-")
    client.send(input("message: ").encode('utf-8'))
    msg = (client.recv(1024).decode('utf-8'))
    if msg == 'quit':
        done = True
    else:
        print(msg)

client.close()


#~~~~~~~~~~~~~~~~~#
   # MAIN LOOP #
#~~~~~~~~~~~~~~~~~#




