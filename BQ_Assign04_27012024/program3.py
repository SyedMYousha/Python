# Python program to display the sum of n numbers using a list

# for numbers (n) input as a list

num_list = []
n = int(input("Enter the quantity of numbers you want to enter"))
for i in range(0, n):
    nums = int(input("Enter number :"))   # takes number inputs
    num_list.append(nums)                 # appends to numbers to the list

def sum_of_numbers(num_list):
     total = sum(num_list)      # predefined sum() function used to add all the values in the list
     print(total)

sum_of_numbers(num_list)
