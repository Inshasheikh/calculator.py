print("=== Simple Calculator ===")

while True:
    try:
        a = float(input("\nEnter first number: "))
        b = float(input("Enter second number: "))

        print("\nChoose Operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Enter choice (1/2/3/4/5): ")

        if choice == "1":
            print("Result:", a + b)

        elif choice == "2":
            print("Result:", a - b)

        elif choice == "3":
            print("Result:", a * b)

        elif choice == "4":
            if b != 0:
                print("Result:", a / b)
            else:
                print("Error: Cannot divide by zero")

        elif choice == "5":
            print("Thank you for using Calculator 😊")
            break

        else:
            print("Invalid choice! Try again.")

    except ValueError:
        print("Please enter valid numbers only.")