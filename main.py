elif choice == "4":
    print("\n=== Civil Engineering Tools ===")
    print("1. Concrete Volume Calculator")

    civil_choice = input("Choose an option: ")

    if civil_choice == "1":
        length = float(input("Enter length (m): "))
        width = float(input("Enter width (m): "))
        height = float(input("Enter height/thickness (m): "))

        volume = length * width * height

        print("Concrete Volume =", volume, "cubic meters")
