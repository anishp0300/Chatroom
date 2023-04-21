import socket

#-----------
#FUNCTIONS
#-----------
def receive_messages():
	msg = (client.recv(1024).decode('utf-8'))
	print("Server: " + msg)

SERVER= "localhost"
PORT = 1234

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

done = False
while not done:

	# Allows user to enter commands
	inputBuffer = input(">> ")
	if inputBuffer == "CONNECT":
		try: # Try connecting to the server when CONNECT is entered
			client.connect((SERVER, PORT))
			print("-Connection Established-")
		except: # Should the attempt fail, display an error so the program doesn't crash
			print("ERROR: Connection Failed.")

	# Tells server that the client wishes to quit the connection
	elif inputBuffer == "QUIT":
		client.send(inputBuffer.encode('utf-8'))
		done = True

	# Checks for SEND <message> with SEND and <message> separated by a space (' ')
	elif inputBuffer.split(' ')[0] == "SEND":
		client.send(inputBuffer[5:].encode('utf-8'))
		# After a message is sent, receive messages from the server
		receive_messages()
	
	# If the wrong command is entered display an error message
	else:
		print("ERROR: Please use the CONNECT, SEND <message>, and QUIT commands.")
	
	