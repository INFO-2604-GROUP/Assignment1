from array import *
from socket import *

alphabet=['\n',' ','!','$','%','&','(',')','*','+',',','-','.','/',':',';','<','=','>','?','@','^','_',',','~','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
              'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
size=26+26+24
#plainText='Dear Dr. Keith Rowley I am writing this letter to express the fact of the unhealthy and Ludacris number of murders that have plagued this country for decades. The increase in murders has been prevalent during the nineteen nineties , particularly after the coup. In nineteen ninety four was the genesis of our peaceful downfall with approximately one hundred and forty three deaths for that year. Between nineteen ninety five and nineteen ninety nine there was slow but noticeable decrease of the murders exciting the one hundreds and into the nineties. However by the time the new millennium came into being, between the years two thousand to two thousand and twenty two the homicide rate jumped from one hundred and eighteen to an astronomical figure of six hundred and five, with two thousand and twenty two being the highest and no argument the deadliest year that this nation has ever experienced during its sixty years of independence. Mr. Prime Minister, the good citizens of Trinidad and Tobago are figuratively and literally screaming for help. Our young men are dropping like flies. Our Young ladies are being kidnapped and killed also dropping like flies. Up to this day there have been murders that have not been solved. Simultaneously, there are people who are missing to this day who are most likely gone from this world. I urge you to do better.'

f = open("NoMoreMurders.dat", "r")
#f=open("test.txt",'r')
plainText=f.read()

f.close()
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
    #print(RailCipherText)
        
    #Caesar Cipher
    CaesarCipherText=[]
    for char in RailCipherText:
        position=alphabet.index(char)
        position=position+k2
        if(position>=size):
            excess=position-size
            position=0
            position=position+excess
            CaesarCipherText.append(alphabet[position])
        else:
            CaesarCipherText.append(alphabet[position])
    print()
    print(CaesarCipherText)
    
    g = open("Rowley.dat", "w")
    #g.write("".join(CaesarCipherText))
    g.writelines(''.join(CaesarCipherText))
    g.close()
    
    
    serverName = "localhost"
    serverPort=8080 
   
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName,serverPort))
    clientSocket.send(bytes(''.join(CaesarCipherText), "utf-8"))
    
    clientSocket.close()
        
else:
    print("Invalid input")




