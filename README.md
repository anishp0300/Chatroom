# Chatroom
*****************************************
Chat App Using Python Socket Programming
Developed by- Shoh and Anish
Developed in VSCode and Visual Studio
*****************************************

README

included:
All code files (.py, .sln, .pyproj)
this README:
Steps to execute the code files and testing whether the client-server connection and whether or not the server is able to handle multiple clients.
__________________________________________________________________________________________________________________________________________________________________________

*** After executing the code you will have a simple command line interface for both client and server side. ***

- To execute the code files, compile the App_Client.py and App_Server.py codes on your preferred IDE. Locate the files on your local machine and then run the client 
& server programs separately in command prompt on Windows, Terminal on MacOS or command line on Linux.

- Once you have the codes up and running on command prompt, on the client/s, you will need to type 'CONNECT' inorder to connect with the server. Once successful, you 
should be able to see a 'Connection has been established..' message on the server. As you connect more clients, you will see subsequent 'Connection has been established'
messages on the server.

- To start sending messages, on the client, type 'SEND', followed by your message in order to send a message. Once sent, the message will be broadcasted to all other 
connected clients. On different clients, you will see the client address and the socket number of the client sending messages for identification.


***** As part of Bonus Points for the Assignment!! *****
1) If you do not type the above keywords, you will be prompted with- 'ERROR: Please use the CONNECT, SEND <message>, and QUIT commands.'         
NOTE- THE KEYWORDS ARE CASE SENSITIVE!!
2) You will also see a message if the connection fails while connecting the client to the server after entering the 'CONNECT' keyword. The following message is displayed-
'ERROR: Connection Failed.'

- In order to close a client-server connection, type 'QUIT' on one of the clients. The client will gracefully be able to disconenct from the server upon this request,
while other clients still remain connected to the server, being able to interact with each other.
