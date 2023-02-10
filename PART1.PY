#REYHAN MAHARAJ 816026196
#CHE DICKENSON

from array import *
print(len("hello class"))

def DoubleCipherEncryption():
    #32-47 range for special characters
    #58=126 range for upper, lower case letters and other special symbols
    #alphabet=[" ","!",","#",$,%,&,',(,),*,+]
    alphabet=[' ','!','$','%','&','(',')','*','+',',','-','.','/',':',';','<','=','>','?','@','^','_',',','~','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
              'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    size=26+26
    
    #Rail Fence Algorithm key
    k1=2

    #Caesar Cipher Algorithm key
    k2=1
    
    line=input("Please enter a sentence: ")
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
            CaesarCipherText.append(alphabet[position])
        print()
        print(CaesarCipherText)
                
    else:
        print("Invalid input")


def DoubleCipherDencryption():
    pass

sentence=DoubleCipherEncryption()
#print(sentence)



