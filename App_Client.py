import socket
import threading

PORT = 1234
SERVER = "localhost"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 1234))

msg = s.recv(1024)   #Decide how much data we want to receive at a time (buffer)
print(msg.decode("utf-8"))   #sockets communicating in bytes

while True:
	inputBuffer = str(input())
	s.send(inputBuffer.encode("utf-8"))