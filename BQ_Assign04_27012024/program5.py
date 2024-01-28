 # Write a Python program to read a file line by line and store it in a list.


file = open("program5exFile.txt", "r")
lines = list(file.readlines())   # reads all the lines from the file and stores each line in the list as an element
print("the list of lines is : \n ", lines)                     # prints the lines as list

for i in lines: 
    print (i)                    # printd all the lines read from the file