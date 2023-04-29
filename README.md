# Chatroom
*****************************************
Chat App Using Python Socket Programming
Developed by- Anish Puranik and Shoh Sewell
Developed in VSCodium and Visual Studio
*****************************************

README

included:
All code files (.py, .sln, .pyproj)
This README:
Steps to execute the code files and testing whether the client-server connection and whether or not the server is able to handle multiple clients.
__________________________________________________________________________________________________________________________________________________________________________

*** After executing the code you will have a simple command line interface for both client and server side. ***

- To execute the code files, make sure the latest version of Python 3 is installed, locate the App_Client.py and App_Server.py files on your local machine and then run the client and server programs in separate windows of the command prompt on Windows, or Terminal on Unix based machines using the 'python3' command (e.g. python3 App_Server.py).

- Once you have the server and client programs running in separate windows, on the client window, you will need to type and enter the 'CONNECT' command in order to connect with the server. Once successful, you should be able to see a 'Connection has been established with...' message on the server. As you connect more clients, you will see subsequent 'Connection has been established with...' messages on the server.

- To start sending messages on the client, type and enter 'SEND' followed by your message separated by a space in order to send a message (e.g. SEND Hello, Server!). Once sent, the message will be broadcast to all other connected clients via the server. On different clients, you will see the client address and the socket number of the client sending messages for identification.


***** As part of Bonus Points for the Assignment!! *****
1) If you do not type the above keywords, you will be prompted with- 'ERROR: Please use the CONNECT, SEND <message>, and QUIT commands.'
NOTE- THE KEYWORDS ARE CASE SENSITIVE!!
2) You will also see a message if the connection fails while connecting the client to the server after entering the 'CONNECT' keyword. The following message is displayed-
'ERROR: Connection Failed.'

- In order to close a client-server connection, type 'QUIT' on one of the clients. The client will gracefully be able to disconenct from the server upon this request, while other clients still remain connected to the server, being able to interact with each other.
