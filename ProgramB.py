from socket import *

serverPort = 8080

serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(("",serverPort))
serverSocket.listen(1)

while 1:
    connectionSocket, addr = serverSocket.accept()
    CipherText = connectionSocket.recv(1024)

    
    print ("Received From Client: ", CipherText)
	 
    # send back modified sentence over the TCP connection
    #connectionSocket.send(capitalizedSentence)

    # output to console the sentence sent back to the client 
    #print ("Sent back to Client: ", capitalizedSentence)
	 
    # close the TCP connection; the welcoming socket continues
    connectionSocket.close()