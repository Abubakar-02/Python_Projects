import requests

API_KEY =  "bca58e76bebeda5f7ec8eb5e"
BASE_URL =   f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/"

def convert_currency(amount, from_currency, to_currency):
    url = BASE_URL + from_currency
    response = requests.get(url)
    data = response.json()

    if data["result"] == "success":
        rate = data["conversion_rates"][to_currency]
        result= amount * rate
        print(f"\n {amount}{from_currency} = {result :.2f} {to_currency}")
    
    else:
        print("Error! Check your Currency code")

print("╔══════════════════════════════════╗")
print("║    💱 CURRENCY CONVERTER 💱      ║")
print("╚══════════════════════════════════╝")

while True:

    print("\n1. Convert Currency")
    print("2. Exit")

    choice = input("Enter your choice (1-2): ")

    if choice == "1":
        amount =float(input("Enter Amount: "))
        from_cur = input(" From Currency  e.g: USD, PKR, EUR, SAR, INR, GBP : ").upper()
        to_cur = input(" To Currency e.g: USD , PKR, EUR, SAR, INR, GBP: ").upper()
        convert_currency(amount, from_cur, to_cur)
    elif choice == "2":
        print(" Good BYe !---------------")
        break
    else:
        print("Invalid choice <><><><><><><><>!!!")