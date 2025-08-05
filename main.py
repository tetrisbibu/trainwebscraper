import requests
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com'
all_quotes = []

while url:
    
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')
    qoute_blocks = soup.find_all('div', class_='quote')

    for quote in qoute_blocks:
        text = quote.find('span', class_='text').get_text(strip=True)
        author = quote.find("small", class_="author").get_text(strip=True)
        tags = [tag.get_text(strip=True) for tag in quote.find_all('a', class_='tag')]

        all_quotes.append({
            'text': text,
            'author': author,
            'tags': tags
        })

    next_btn = soup.find('li', class_='next')
    if next_btn:
        next_link = next_btn.find('a')['href']
        url = 'https://quotes.toscrape.com' + next_link
    else:
        url = None

print(f'All quotes: {len(all_quotes)}\n')
for i, quote in enumerate(all_quotes[:5], 1): #here is a fixed number of quotes to be displayed
    print(f"{i}: \"{quote['text']}\" — {quote['author']} (Tags: {', '.join(quote['tags'])})")