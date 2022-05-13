#Import the sockets library
import gameboard
import socket

#Define my socket address information
serverAddress = '127.0.0.1'
serverPort = 8000

#create a socket object on my server
connectionSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Attempt to connect to the server
connectionSocket.connect((serverAddress,serverPort))

#Wait for a message from my server
#serverData = connectionSocket.recv(4)
#print(serverData.decode('ascii'))
#serverData = connectionSocket.recv(4)
#print(serverData.decode('ascii'))

#Send data to server
name = input("Please type username: ")
name = name.encode('utf-8')
connectionSocket.send(name)

clientData = connectionSocket.recv(1024)
print("Connected with player:", clientData.decode('ascii'))

board = gameboard.BoardClass(name.decode('ascii'), "player1", 0, 0, 0, 0, connectionSocket)

#closing the connection when I am done
connectionSocket.close()
