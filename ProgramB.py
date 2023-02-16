from socket import *

alphabet=['\n',' ','!','$','%','&','(',')','*','+',',','-','.','/',':',';','<','=','>','?','@','^','_',',','~','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
              'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
size=26+26+24

serverPort = 8080

serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(("",serverPort))
serverSocket.listen(1)

print("How many keys do you wish to use to crack the encryption")
RailKEY_MAX_str=input("From 1 to (unknown), how many rail cipher keys do you want to try? : ")
CeasrKEY_MAX_str=input("From 1 to (unknown), how many ceasar cipher keys do you want to try? : ")
RailKEY_MAX=int(RailKEY_MAX_str)
CeasrKEY_MAX=int(CeasrKEY_MAX_str)

keyWords=["Rowley","murders","the"]

while 1:
    connectionSocket, addr = serverSocket.accept()
    CipherText = connectionSocket.recv(1600)

    
    print ("Received From Client: ", CipherText.decode("utf-8"))
    g = open("ServerRowley.dat", "w")
    g.writelines(CipherText.decode("utf-8"))
    g.close()
        
    g = open("ServerRowley.dat", "r")
    CipherText=g.read()
    g.close()
    
    #print(CipherText)
    #Ceaser Decryption
    RailCipherText=[]
    position=0
    placeholder="empty"
    for ceaserKey in range(1,CeasrKEY_MAX+1):
        #print(ceaserKey)
        for char in CipherText:
            position=alphabet.index(char)
            position=position-ceaserKey
            if(position<0):
                position=size+position
                RailCipherText.append(alphabet[position])
            else:
                RailCipherText.append(alphabet[position])
            
        #+print(RailCipherText)
        #Rail Fence Decryption
        for railKey in range(2,RailKEY_MAX+2):
            #railKey=2
            if railKey<2:
                continue
            #print(railKey)
            arr1 = [[placeholder for x in range(len(RailCipherText))]for y in range(railKey)]
            columns=len(RailCipherText)
            row=0
            down=True
            for col in range(columns):
                arr1[row][col]="here"
                if row==0:
                    down=True
                        
                if row==railKey-1:
                    down=False
                        
                if down==True:
                    row=row+1
                            
                if down==False:
                    row=row-1
            decryptedText=[]
            position=0
            row=0
            plainText=[]
            for row in range(railKey):
                for col in range(columns):
                    if arr1[row][col]=="here":
                        arr1[row][col]=RailCipherText[position]
                        position=position+1
                
            row=0
            col=0
            down=True
            for col in range(columns):
                if arr1[row][col]!=placeholder:
                    plainText.append(arr1[row][col])
                if row==0:
                    down=True
                        
                if row==railKey-1:
                    down=False
                        
                if down==True:
                    row=row+1
                            
                if down==False:
                    row=row-1
            #plainText=''.join(plainText)
            match=False
            #plainText=str(plainText)
            for char in plainText:
                for keyword in keyWords:
                    temp=char    
                    for letter in keyword:
                            if letter==temp:
                                match=True
                                temp=next(iter(plainText))
                            else:
                               # if temp==' ':
                                #    match=True
                                match=False
                    if match==True:
                        print()
                        print(plainText)
                if match==True:
                    break
            if match==True:
                break
            
                
   
    connectionSocket.close()