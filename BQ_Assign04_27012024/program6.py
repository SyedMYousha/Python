file1  = open("program6exFile1.txt", "r")
file1_content = file1.read()            # reads all the content from file no. 1 and stores in file1_content
# print(file1_content)

file2 = open("program6exFile2.txt", "w")
file2.write(file1_content)              # writes file1_content in file2
