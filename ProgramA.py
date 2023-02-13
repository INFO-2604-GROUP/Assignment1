f = open("NoMoreMurders.dat", "r")

print(f.read()) # read the first 3 characters

print(f.read()) # End of the file (EOF) is reached
''

f.close()


