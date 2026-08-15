import requests
from bs4 import BeautifulSoup

def scrape_wikipedia(topic):
    url = f"https://en.wikipedia.org/wiki/{topic}"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    
    title = soup.find("h1").text
    paragraphs = soup.find_all("p")
    
    print(f"\n📖 {title}")
    print("-" * 50)
    for i, para in enumerate(paragraphs[:3]):
        if para.text.strip():
            print(para.text.strip())
    print("-" * 50)

print("╔══════════════════════════════════╗")
print("║      🔍 WEB SCRAPER 🔍           ║")
print("╚══════════════════════════════════╝")

topic = input("\nEnter topic to search: ")
scrape_wikipedia(topic)