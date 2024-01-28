#  Python program to print the Fibonacci series

def fibonacci(n):
    fib_series = [0, 1]
    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])   #it checks if the length of fibonacci series is less than the nth-term then 
    return fib_series                                         # appends the sum of the last two elements of the list to the list and continues this 
                                                                # e.g: [0,1] the elements with indexes -1 and -2 are respectively 1 and 0
# Example: Generate Fibonacci series up to 10 terms               # so 1+0 = 1 , so it appends 1 to the list and the list becomes [0,1,1]
n_terms = 10                                                       # now the elements with indexes -1 and -2 are 1 and 1
result = fibonacci(n_terms)                                         # 1 + 1 = 2 so it appends 2 to the list , and the process continues
print(result)
