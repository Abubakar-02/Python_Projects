import string
import random

all_character = string.ascii_letters + string.digits + string.punctuation

print("╔══════════════════════════════════╗")
print("║     🔐 PASSWORD GENERATOR 🔐     ║")
print("╚══════════════════════════════════╝")
print()

while True:
    length= int(input("🔢 Write the length of your password (8-32) : "))
    password =""
    for i in range(length):
        password += random.choice(all_character)
    print(f" ✅  Generated Password : {password}")
    print()
    
    again = input(" Generate more password : (Yes/NO) = ")

    if again != "yes":
        print("Thanks ! Apna passsword yaad rakho")
        break