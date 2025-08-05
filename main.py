import requests
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com'
response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')
qoute_blocks = soup.find_all('div', class_='quote')

for quote in qoute_blocks:
    text = quote.find('span', class_='text').get_text(strip=True)
    author = quote.find("small", class_="author").get_text(strip=True)
    tags = [tag.get_text(strip=True) for tag in quote.find_all('a', class_='tag')]

    print(text)
    print(author)
    print(tags)
    print('-' * 40)

