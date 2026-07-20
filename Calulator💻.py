import math




def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error! Cannot divide by zero."
    return a / b


def modulus(a, b):
    if b == 0:
        return "Error! Cannot calculate modulus with zero."
    return a % b


def power(a, b):
    return a ** b


def floor_div(a, b):
    if b == 0:
        return "Error! Cannot divide by zero."
    return a // b


def square_root(a):
    if a < 0:
        return "Error! Square root of a negative number is not possible."
    return math.sqrt(a)


def display_menu():
    print("\n" + "=" * 40)
    print("        🧮 PYTHON CALCULATOR 🧮")
    print("=" * 40)
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")
    print("6. Power (**)")
    print("7. Floor Division (//)")
    print("8. Square Root (√)")
    print("9. Exit")
    print("=" * 40)


while True:

    display_menu()

    choice = input("Enter your choice: ")

    
    if choice == "9":
        print("\nThank you for using Python Calculator.")
        print("Good Bye!")
        break

    
    if choice not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
        print("Invalid Choice! Please try again.")
        continue

    
    if choice == "8":
        try:
            num = float(input("Enter Number: "))
            print("Answer =", square_root(num))
        except ValueError:
            print("Invalid Input! Please enter a valid number.")
        continue

    try:
        num1 = float(input("Enter First Number: "))
        num2 = float(input("Enter Second Number: "))
    except ValueError:
        print("Invalid Input! Please enter valid numbers.")
        continue

    
    if choice == "1":
        print("Answer =", add(num1, num2))

    elif choice == "2":
        print("Answer =", subtract(num1, num2))

    elif choice == "3":
        print("Answer =", multiply(num1, num2))

    elif choice == "4":
        print("Answer =", divide(num1, num2))

    elif choice == "5":
        print("Answer =", modulus(num1, num2))

    elif choice == "6":
        print("Answer =", power(num1, num2))

    elif choice == "7":
        print("Answer =", floor_div(num1, num2))