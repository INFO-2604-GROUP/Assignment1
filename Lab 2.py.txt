# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 11:48:32 2022

@author: neil_
"""
"""
f = open("poem.txt", "r")

print(f.read(3)) # read the first 3 characters
'The'

print(f.read()) # read the remaining characters in the file.
' caged bird sings\nwith a fearful trill\nof things unknown\nbut longed for still\n'

print(f.read()) # End of the file (EOF) is reached
''

f.close()

"""
"""
f = open("poem.txt", "r")

f.read(4) # read first 4 characters
'The '

print(f.readline()) # read until the end of the line is reached
'caged bird sings\n'

print(f.readline()) # read the second line
'with a fearful trill\n'

print(f.readline()) # read the third line
'of things unknown\n'

print(f.readline()) # read the fourth line
'but longed for still'

f.readline() # EOF reached
''

f.close()
"""
"""
f = open("poem.txt", "r")

print(f.readlines())
#['The caged bird sings\n', 'with a fearful trill\n', 'of things unknown\n', 'but longed for still\n']

f.readlines() # EOF reached
'[]'

f.close()
"""

"""
f = open("poem.txt", "r")

chunk = 200
while True:
    data = f.read(chunk)
    if not data:
        break
    print(data)
"""

"""
f = open("poem.txt", "r")

while True:
    line = f.readline()
    if not line:
        break
    print(line)
"""

"""
f = open("poem.txt", "r")

for line in f:
    print(line, end="")
"""

"""
f = open("poem_2.txt", "w")

f.write("When I think about myself, ")

f.write("I almost laugh myself to death.")

f.close() # close the file and flush the data in the buffer to the disk


f = open("poem_2.txt", "r") # open the file for reading

data = f.read() # read entire file

'When I think about myself, I almost laugh myself to death.'

print(data)
#When I think about myself, I almost laugh myself to death.

f.close()
"""
"""
f = open("poem_2.txt", "w")

f.write("When I think about myself, \n") # notice newline

f.write("I almost laugh myself to death.\n") # notice newline

f.close()

f = open("poem_2.txt", "r") # open the file again

data = f.read() # read the entire file

'When I think about myself, \nI almost laugh myself to death.\n'

print(data)
"""

lines = [
    "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod",
    "tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,"
    "quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo",
    "consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse",
    "cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non",
    "proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
    ]

f = open("lorem.txt", "w")

f.writelines(lines)

f.close()