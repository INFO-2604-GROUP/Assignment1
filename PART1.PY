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
        cols=len(line)# length of string is the number of columns
        rows=k1# number of rows
        #encryptTable=[[0]*col]*rows
        #print(encryptTable)
        for char in line:
            for row in rows:
                x=0
                for cols in row:
                    arr1.insert(x,char)
                    x=x+1
        print(arr1)

        pass
    else:
        print("Invalid input")


def DoubleCipherDencryption():
    pass

sentence=DoubleCipherEncryption()
print(sentence)



