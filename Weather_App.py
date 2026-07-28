import requests

API_KEY = "298c1524fa6c4f6ef24f8f1605f691d2"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    url=f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
    response=requests.get(url)
    data=response.json()

    if data["cod"] == 200:
        name = data["name"]
        temp= data["main"]["temp"]
        feels= data["main"]["feels_like"]
        humidity= data["main"]["humidity"]
        desc= data["weather"][0]["description"]

        print(f"Weather in {name}: ")
        print(f"Temperature:{temp}°C")
        print(f"Feels_like: {feels}°C")
        print(f"Humidity: {humidity}%")
        print(f"Description: {desc}")
    else:
        print("city not found. Please check the city name and try again.")

print("╔══════════════════════════════════╗")
print("║       🌤️ WEATHER APP 🌤️          ║")
print("╚══════════════════════════════════╝")

while True:

     print("\nWelcome to the Weather App!")
     print("\n1. Get Weather")
     print("2. Exit")

     choice = input("Enter your choice (1-2): ")

     if choice == "1":
        city= input("Enter city name: ")
        get_weather(city)

     elif choice == "2":
        print("GoodBye! Thank you for using the Weather App.")
        break
     else:
        print("Invalid choice ! Please try again.")

