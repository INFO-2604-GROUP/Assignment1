#REYHAN MAHARAJ 816026196
#CHE DICKENSON

from array import *

alphabet=[' ','!','$','%','&','(',')','*','+',',','-','.','/',':',';','<','=','>','?','@','^','_',',','~','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
              'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

size=26+26+24
line=input("Please enter a sentence: ")
RailKey=input("Please enter a Rail Fence Cipher key: ")
CaesarKey=input("Please enter a Caesar Cipher key: ")

def DoubleCipherEncryption(line,RailKey,CaesarKey):
    #32-47 range for special characters
    #58=126 range for upper, lower case letters and other special symbols
    
    #Rail Fence Algorithm key
    k1=int(RailKey)

    #Caesar Cipher Algorithm key
    k2=int(CaesarKey)
    
    valid=line.isascii()
    if(valid==True):
        columns=len(line)# length of string is the number of columns
        rows=k1# number of rows
        placeholder='empty'
        
        arr1 = [[placeholder for x in range(len(line))]for y in range(k1)]
        #arr1=[columns[rows]]         
        
        x=0
        row=0
        col=0
        down=True
        for col in range(columns):
            arr1[row][col]=line[col]
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
        return CaesarCipherText
    else:
        print("Invalid input")


def DoubleCipherDencryption(CipherText,RailKey,CaesarKey):
    caesarKey=int(CaesarKey)
    RailCipherText=[]
    for char in CipherText:
        position=alphabet.index(char)
        position=position-caesarKey
        if(position<0):
            position=size+position
            RailCipherText.append(alphabet[position])
        else:
            RailCipherText.append(alphabet[position])
    print(RailCipherText)
    
    placeholder="empty"
    railKey=int(RailKey)
    arr1 = [[placeholder for x in range(len(RailCipherText))]for y in range(railKey)]
    columns=len(RailCipherText)
    rows=railKey
    #row=0
    position=0
    for row in range(rows):
        for col in range(columns):
            if col%railKey==0:
                arr1[row][col]=RailCipherText[position]
                print("here")
                position=position+1
        #position=0    
        #if col==columns:
         #   row=row+1
    
    print()
    print(arr1)
    decryptedText=[]
    position=0
    row=0
    for col in range(columns):
        for row in range(rows):
            if arr1[row][col]!=placeholder:
                decryptedText.append(arr1[row][position])
    print()
    print(decryptedText)
            
        
        
            

sentence=DoubleCipherEncryption(line,RailKey,CaesarKey)
DoubleCipherDencryption(sentence,RailKey,CaesarKey)
#print(sentence)



