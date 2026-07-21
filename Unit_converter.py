print("╔══════════════════════════════════╗")
print("║      🔄 UNIT CONVERTER 🔄        ║")
print("╚══════════════════════════════════╝")
print()

while True:
    print(" Select the type of conversion")
    print("\n1. Length Converter")
    print("2. Weight Converter")
    print("3. Temperature converter")
    print("4. Exit")
    print()

    choice = input(" Enter your choice (1-4) : ")

    if choice == "1":
        print("Length Convertr")
        print("\n 1. KM to miles")
        print(" 2. Miles to KM")
        print("3. inches to cm")
        print("4. cm to inches")

        sub_choice = input(" Enter your choice (1-4) : ")
        value = float(input("Enter the value to convert : "))

        if sub_choice == "1":
            print(f" Result {value * 0.621371} Miles")
        elif sub_choice == "2":
                print(f" result {value * 1.6093} KM")
        elif sub_choice == "3":
            print(f" result {value * 2.54} cm")
        elif sub_choice == "4":
            print(f" result{value * 0.393701} inches")


    elif choice == "2":
         print(" Weight Converter")
         print("\n 1. KG to Pounds")
         print(" 2. Pounds to Kg")
         print(" 3. Grams to Ounces")
         print(" 4. Ounces to Grams")

         sub_choice = input(" Enter your choice (1-4): ")
         value = float(input(" Enter the value to convert :"))

         if sub_choice == "1":
              print(f" Result {value * 2.20462} pounds")
         elif sub_choice == "2":
             print(f" Result {value * 0.453592} KG")
         elif sub_choice == "3":
              print(f" Result {value * 0.035271} ounces")
         elif sub_choice == "4":
              print(f" Result {value * 28.3495} grams")
            
    elif choice == "3":
         print( "Temperature converter")
         print("\n 1. Celsius to Fahrenheit" )
         print("2. Fahrenheit to Celsius")
         print("3. Celsius to kelvin")
         print("4. kelvin to celsius")

         sub_choice = input("Enter your choice (1-4): ")
         value = float(input("Enter the value to convert : "))

         if sub_choice == "1":
              print(f" Result {value * 9/5 + 32} Fahrenheit")
         elif sub_choice == "2":
              print(f" Result {(value -32)* 5/9 } celsius")
         elif sub_choice == "3":
              print(f" Result {value + 273.15} kelvin")
         elif sub_choice == "4":
              print(f" Result {value - 273.15} celsius")
    elif choice == "4":
        print("Thank you for using the unit converter ! GoodBye.....")
        break
    else:
         print("-----------------Invalid choice ! -------------")

        