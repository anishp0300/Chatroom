import socket
import threading

#~~~~~~~~~~~#
# FUNCTIONS #
#~~~~~~~~~~~#
def receive_messages():
    # while True:
        msg = serversocket.recv(1024).decode("utf-8")
        if msg:
            print(msg)

def connect_to_server():
	serversocket.connect(('localhost', 1234))
	print("-Connection established-")
	msg = serversocket.recv(1024)   #Decide how much data we want to receive at a time (buffer)
	print(msg.decode("utf-8"))   #sockets communicating in bytes

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
PORT = 1234
SERVER = "localhost"

#~~~~~~~~~~~#
# MAIN LOOP #
#~~~~~~~~~~~#
while True:
	inputBuffer = str(input())
	if(inputBuffer == "CONNECT"):
		connect_to_server()
	elif(inputBuffer == "QUIT"):
		print("Closing program...")
		break
	elif(inputBuffer == "RECEIVE"):
		receive_messages()

	# serversocket.send(inputBuffer.encode("utf-8"))
	# receive_messages()