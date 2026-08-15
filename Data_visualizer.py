import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def stock_visualizer(company, dates, prices):
    plt.figure(figsize=(12, 6))
    plt.plot(dates, prices, color='green', marker='o', linewidth=2)
    plt.fill_between(dates, prices, alpha=0.3, color='green')
    plt.title(f"📈 {company} Stock Price")
    plt.xlabel("Date")
    plt.ylabel("Price (PKR)")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    
    print(f"\n📊 {company} Stock Analysis:")
    print(f"📈 Highest: PKR {max(prices)}")
    print(f"📉 Lowest: PKR {min(prices)}")
    print(f"📊 Average: PKR {sum(prices)/len(prices):.2f}")

print("╔══════════════════════════════════╗")
print("║   📈 STOCK VISUALIZER 📈         ║")
print("╚══════════════════════════════════╝")

company = input("\nEnter company name: ")
days = int(input("Enter number of days: "))

dates = []
prices = []

for i in range(1, days + 1):
    date = input(f"Enter date {i} (DD-MM-YYYY): ")
    price = float(input(f"Enter price for {date} (PKR): "))
    dates.append(date)
    prices.append(price)

stock_visualizer(company, dates, prices)