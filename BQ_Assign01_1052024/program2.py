print("Average Calculator \n")
num1 = float(input("Enter first number  :"))
num2 = float(input("Enter second number  :"))
#round() function used to round the avg to the number of decimals equal to the second parameter of the function i.e. 2
avg = round((num1 + num2) / 2, 2)
print(f"The average of two numbers is {avg}")