from array import *
from socket import *

alphabet=['\n',' ','!','$','%','&','(',')','*','+',',','-','.','/',':',';','<','=','>','?','@','^','_',',','~','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
              'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
size=26+26+24
f = open("NoMoreMurders.dat", "r")

plainText=f.read()

# DoubleCipher Encryption
RailKey=input("Please enter a Rail Fence Cipher key: ")
CaesarKey=input("Please enter a Caesar Cipher key: ")
#Rail Fence Algorithm key
k1=int(RailKey)

#Caesar Cipher Algorithm key
k2=int(CaesarKey)
    

valid=plainText.isascii()
if(valid==True):
    columns=len(plainText)# length of string is the number of columns
    rows=k1# number of rows
    placeholder='empty'
        
    arr1 = [[placeholder for x in range(len(plainText))]for y in range(k1)]
             
        
    x=0
    row=0
    col=0
    down=True
    for col in range(columns):
        arr1[row][col]=plainText[col]
        if row==0:
            down=True
            
        if row==k1-1:
            down=False
            
        if down==True:
            row=row+1
                
        if down==False:
            row=row-1
        
    RailCipherText=[]
    for row in range(rows):
        for col in range(columns):
            if arr1[row][col]!=placeholder:
                RailCipherText.append(arr1[row][col])
    print(RailCipherText)
        
    #Caesar Cipher
    CaesarCipherText=[]
    for char in RailCipherText:
        position=alphabet.index(char)
        position=position+k2
        if(position>size):
            excess=position-size
            position=0
            position=position+excess
            CaesarCipherText.append(alphabet[position])
        else:
            CaesarCipherText.append(alphabet[position])
    print()
    print(CaesarCipherText)
    
    g = open("Rowley.dat", "w")
    g.writelines(CaesarCipherText)
    g.close()
    
    serverName = "localhost"
    serverPort=8080 
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName,serverPort))
    clientSocket.send(bytes(CaesarCipherText, encoding="utf-8"))
    
    clientSocket.close()
        
else:
    print("Invalid input")

f.close()


