#REYHAN MAHARAJ 816026196
#CHE DICKENSON

from array import *
print(len("hello class"))

def DoubleCipherEncryption():
    #32-47 range for special characters
    #58=126 range for upper, lower case letters and other special symbols
    #alphabet=[" ","!",","#",$,%,&,',(,),*,+]
    
    #Rail Fence Algorithm key
    k1=2

    #Caesar Cipher Algorithm key
    k2=1
    
    line=input("Please enter a sentence: ")
    valid=line.isascii()
    if(valid==True):
        arr1=[[]]
        columns=len(line)# length of string is the number of columns
        rows=k1# number of rows
        #encryptTable=[[0]*col]*rows
        #print(encryptTable)
        for row in range(rows):
            x=row
            y=0
            for column in range(columns):
                for char in line:
                    if y%k1==0:
                    #arr1.insert(x,char)
                        arr1[x][y]=char
                        y=y+1
            x=x+1
            for char in line:
                if y%k1==1:
                    arr1[x][y]=char
        print(arr1)

        pass
    else:
        print("Invalid input")


def DoubleCipherDencryption():
    pass

sentence=DoubleCipherEncryption()
#print(sentence)



