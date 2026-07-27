import json

def load_expenses():
    try:
        with open("expenses.json", "r") as f:
            return json.load(f)
    except:
        return []

def save_expenses(expenses):
    with open("expenses.json", "w") as f:
        json.dump(expenses, f)

def add_expense(expenses, item, amount):
    expenses.append({"item" : item, "amount": amount})
    save_expenses(expenses)

def view_expenses(expenses):
    if not expenses:
        print("No expenses are recorded yet .......!")
    else:
        print("\n All Expenses are listed below : ")
        print("-" * 40)
        for i, expense in enumerate(expenses):
            print(f"{i+1}. {expense["item"]} : Rs. {expense["amount"]}")
        print("-" *40)
        total = sum(expense["amount"] for expense in expenses)
        print(f"\n Total Expenses : Rs. {total}")

expenses = load_expenses()


print("╔══════════════════════════════════╗")
print("║      💰 EXPENSE TRACKER 💰       ║")
print("╚══════════════════════════════════╝")

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("\n Enter your choice (1-3): ")

    if choice == "1":
        item = input("Enter the expense item: ")
        amount= float(input("Enter the expense amount: "))
        add_expense(expenses, item , amount)
        print(f" {item } added successfully with amount Rs. {amount}------- !")

    elif choice == "2":
        view_expenses(expenses)

    elif choice == "3":
        print("Goodbye! Thank you for using the Expense Tracker. Have a great day -----")
        break
    else:
        print(" Invalid choice... Please try again later ! Thank you .........")

    

    
