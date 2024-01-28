# Program to count unique values inside a list

# to count the no. of unique values inside the
def unique_values_counter(ex_list):
    list = set(ex_list)
    uniqueValues = len(ex_list)
    print("The number of uniques values in the list are :", uniqueValues)

# Example list input
ex_list = []
n = int(input("Enter the number of elements you want to enter"))

for i in range (0, n):
    elements = input("Enter the element : ")
    list.append(elements)

# prints no. of unique values
unique_values_counter(ex_list)



