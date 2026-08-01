import requests

API_KEY = "01903f35eb2f43ac80d830110f0de5a3"
BASE_URL = "https://newsapi.org/v2/top-headlines"

def get_news(category="general" , country="us"):
    url = f"{BASE_URL}?categitgory={category}&country={country}&apiKey={API_KEY}"
    response = requests.get(url)
    data = response.json()

    if data ["status"] == "ok":
        articles = data["articles"]
        print(f"\n Top news Headlines: \n")
        print("-" * 50)
        for i, article in enumerate(articles[:5]):
            print(f"\n {i+1} . {article['title']}")
            print(f"🔗 {article['url']}")
            print("-" * 50)
    else:
        print("Error ❌ ! Fetching News!")

print("╔══════════════════════════════════╗")
print("║        📰 NEWS APP 📰            ║")
print("╚══════════════════════════════════╝")


while True:

    print("\n1. General News")
    print("2. Technology News")
    print("3. Health News")
    print("4. Sports News")
    print("5. Exit")


    choice = input("Enter your choice (1-5) : ")

    if choice == "1":
        get_news("general")

    elif choice ==  "2":
        get_news("technology")

    elif choice == "3":
        get_news("health")

    elif choice =="4":
        get_news("sports")

    elif choice == "5":
        print("Good bye ------------")
        break
    else:
        print("Invalid choice")

