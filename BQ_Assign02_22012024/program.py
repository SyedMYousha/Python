while True:
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter choice (1/2/3/4/5): ")

    if choice == '5':
        print("Exiting the calculator.")
        break

    if (choice == '1' or choice =='2' or choice == '3' or choice =='4' ):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", num1 + num2)
        elif choice == '2':
            print(num1, "-", num2, "=", num1 - num2)
        elif choice == '3':
            print(num1, "*", num2, "=", num1 * num2)
        elif choice == '4':
            if num2 != 0:
                print(num1, "/", num2, "=", num1 / num2)
            else:
                print("Cannot divide by zero")
    else:
        print("Invalid Input. Please enter a valid choice.")
