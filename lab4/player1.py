import gameboard
#Import the sockets library
import socket

#Using the gethostname function
#print("Desktop Name:", socket.gethostname())

#using the loopback address as my server IP address
serverAddress = '127.0.0.1'

#define a port number for my server
port = 8000

#create a socket object on my server
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#bind my host with my port number
serverSocket.bind((serverAddress,port))

#setup my socket using listen function
#5 designates the max number of connections my socket
serverSocket.listen(5)

#A variable to keep track of the number of connections
connectionCounter = 0

#Boolean for while loop
contToRun = True
print("Server Address:", serverAddress, "Port:", port)
#While to keep my server running
while (contToRun):
   #begin accepting incoming connection requests
   clientSocket,clientAddress = serverSocket.accept()

   #Printing the client address
   print("Client connected from: ",clientAddress)

   #Wait for a message from my client
   clientData = clientSocket.recv(1024)
   oppenentName = clientData.decode('ascii')
   print("Connected with player:", oppenentName)
   connectionCounter += 1

   name = 'player1'
   name = name.encode('utf-8')
   clientSocket.send(name)

   board = gameboard.BoardClass("player1", oppenentName, 0, 0, 0, 0, clientSocket)
   #clientData = clientSocket.recv(1024)
   #move = clientData.decode('ascii')
   #print(move)
   if (connectionCounter == 10):
      contToRun = False
      serverSocket.close()
