#program to Calculate the factorial of a given number

n = int(input("Enter a number: "))
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(f"The factorial of {n} is: {factorial(n)}")


