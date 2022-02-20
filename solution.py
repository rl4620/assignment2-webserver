# import socket module
from socket import *
# In order to terminate the program
import sys


def webServer(port=13331):
  serverSocket = socket(AF_INET, SOCK_STREAM)
  #Prepare a server socket
  serverSocket.bind(("", port))
  #Fill in start
  serverSocket.listen(1)
  #Fill in end

  while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept() 
    try:

      try:
        message = connectionSocket.recv(1024).decode()
        #print('Received message: ' + message)
        filename = message.split()[1][1:]
        print("file:" + filename)
        f = open(filename)
        outputdata = f.readlines()
        
        #Send one HTTP header line into socket.
        #Fill in start
        connectionSocket.send("HTTP/1.0 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: text/plain".encode())
        #Fill in end

        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
          print("sending: " + outputdata[i])
          connectionSocket.send(outputdata[i].encode())

        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
      except IOError:
        # Send response message for file not found (404)
        #Fill in start
        connectionSocket.send("HTTP/1.0 404 Not Found\r\n".encode())
        #Fill in end


        #Close client socket
        #Fill in start
        connectionSocket.close()
        #Fill in end

    except (ConnectionResetError, BrokenPipeError):
      pass

  serverSocket.close()
  sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
  webServer(13331)