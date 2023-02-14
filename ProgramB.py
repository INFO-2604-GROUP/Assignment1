from socket import *

alphabet=['\n',' ','!','$','%','&','(',')','*','+',',','-','.','/',':',';','<','=','>','?','@','^','_',',','~','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
              'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
size=26+26+24

serverPort = 8080

serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(("",serverPort))
serverSocket.listen(1)

print("How many keys do you wish to use to crack the encryption")
RailKEY_MAX=input("From 1 to (unknown), how many rail cipher keys do you want to try? : ")
CeasrKEY_MAX=input("From 1 to (unknown), how many ceasar cipher keys do you want to try? : ")
while 1:
    connectionSocket, addr = serverSocket.accept()
    CipherText = connectionSocket.recv(1024)

    
    print ("Received From Client: ", CipherText)
    g = open("ServerRowley.dat", "w")
    g.writelines(CipherText.decode("utf-8"))
    g.close()
	 
    
    #connectionSocket.send(capitalizedSentence)

   
    #print ("Sent back to Client: ", capitalizedSentence)
	 
    # close the TCP connection; the welcoming socket continues
    connectionSocket.close()