import requests
from bs4 import BeautifulSoup
from datetime import datetime

def scrape_quotes():
    url = "https://quotes.toscrape.com/"
    response = requests.get(url)

    if response.status_code != 200:
        print("❌ Failed to fetch the site")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = soup.find_all('div', class_='quote')

    all_quotes = []

    for idx, quote in enumerate(quotes, 1):
        text = quote.find('span', class_='text').get_text(strip=True)
        author = quote.find('small', class_='author').get_text(strip=True)
        formatted = f"{idx}. {text} — {author}"
        print(formatted)
        all_quotes.append(formatted)

    return all_quotes

def save_to_txt(quotes):
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"quotes_{now}.txt"

    with open(filename, 'w', encoding='utf-8') as file:
        file.write("📜 Quotes from https://quotes.toscrape.com/\n")
        file.write("="*60 + "\n")
        for line in quotes:
            file.write(line + "\n")

    print(f"\n✅ Quotes saved to file: {filename}")

def main():
    print("📡 Scraping quotes...")
    quotes = scrape_quotes()
    if quotes:
        save_to_txt(quotes)
    else:
        print("❌ No quotes scraped.")

if __name__ == "__main__":
    main()
