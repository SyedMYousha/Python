# With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and 
# n(both included). and then the program should print the dictionary.
 
n = int(input("Enter an integral number (n) : \t"))


def Square_dictionary(n):
    for i in range(1, n+1):   # generates the squares of the n itself and all the preceding numbers
      square = {i: i*i}       #dictionary
      print(square)

Square_dictionary(n)


