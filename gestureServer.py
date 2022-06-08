from socket import *

#Prepare a server socket
serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort = 9879

serverSocket.bind(('', serverPort))

while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try:
        #Recover message from client
        message = connectionSocket.recv(1024)
        print("Received message: " + message)
    except IOError:
        connectionSocket.close()

serverSocket.close()
sys.exit()