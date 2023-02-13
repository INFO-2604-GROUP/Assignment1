"""  TCPClient.py """

from socket import *

serverName = "localhost"
serverPort=12009

clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect((serverName,serverPort))

sentence = input("Input lowercase sentence: ")


clientSocket.send(bytes(sentence, "utf-8"))

print ("Sent to Make Upper Case Server: ", sentence)

modifiedSentence = clientSocket.recv(1024)

print ("Received from Make Upper Case Server: ", modifiedSentence)

clientSocket.close()
