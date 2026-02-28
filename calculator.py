def calculator():
    print("Select operation.")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")

    no1 = int(input("Enter first number: "))
    no2 = int(input("Enter second number: "))

    if choice == '1':
        print(no1, "+", no2, "=", num1 + no2)

    elif choice == '2':
        print(no1, "-", no2, "=", no1 - no2)

    elif choice == '3':
        print(no1, "*", no2, "=", no1 * no2)

    elif choice == '4':
        if num2 != 0:
            print(no1, "/", no2, "=", no1 / no2)
        else:
            print("Cannot divide by zero!")

    else:
        print("Invalid choice")

calculator()