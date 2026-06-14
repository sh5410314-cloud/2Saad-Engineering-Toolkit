print("=== 2Saad Universal Engineering Assistant ===")

while True:
    print("\n1. Calculator")
    print("2. Unit Converter")
    print("3. About Project")
    print("4. Civil Engineering Tools")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    # Calculator
    if choice == "1":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        print("\nSelect operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")

        operation = input("Choose operation (1-4): ")

        if operation == "1":
            print("Result =", num1 + num2)

        elif operation == "2":
            print("Result =", num1 - num2)

        elif operation == "3":
            print("Result =", num1 * num2)

        elif operation == "4":
            if num2 != 0:
                print("Result =", num1 / num2)
            else:
                print("Error: Cannot divide by zero!")

        else:
            print("Invalid operation!")

    # Unit Converter
    elif choice == "2":
        print("\nUnit Converter")
        print("1. Meter to Feet")
        print("2. Feet to Meter")

        converter = input("Choose option (1-2): ")

        if converter == "1":
            meters = float(input("Enter meters: "))
            feet = meters * 3.28084
            print("Feet =", feet)

        elif converter == "2":
            feet = float(input("Enter feet: "))
            meters = feet / 3.28084
            print("Meters =", meters)

        else:
            print("Invalid option!")

    # About Project
    elif choice == "3":
        print("\n=== About Project ===")
        print("Project: 2Saad Universal Engineering Assistant")
        print("Founder: Saad Muhammad Hasan")
        print("Mission: Building tools for engineers worldwide.")
        print("Built with: Python, Pydroid 3, Termux, GitHub")

    # Civil Engineering Tools
    elif choice == "4":
        print("\n=== Civil Engineering Tools ===")
        print("1. Concrete Volume Calculator")

        civil_choice = input("Choose an option: ")

        if civil_choice == "1":
            length = float(input("Enter length (m): "))
            width = float(input("Enter width (m): "))
            height = float(input("Enter thickness (m): "))

            volume = length * width * height

            print("Concrete Volume =", volume, "cubic meters")

        else:
            print("Invalid option!")

    # Exit
    elif choice == "5":
        print("Thank you for using 2Saad Universal Engineering Assistant!")
        print("Goodbye!")
        break

    # Invalid Input
    else:
        print("Invalid option. Try again.")
