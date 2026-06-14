print("=== 2Saad Universal Engineering Assistant ===")

while True:
    print("\n1. Calculator")
    print("2. Unit Converter")
    print("3. About Project")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Result:", num1 + num2)

    elif choice == "2":
        meters = float(input("Enter meters: "))
        feet = meters * 3.28084
        print("Feet:", feet)

    elif choice == "3":
        print("\n2Saad Technology BD")
        print("Founder: Saad Muhammad Hasan")
        print("Mission: Building tools for engineers worldwide.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Try again.")
    
