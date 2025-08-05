import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

page = requests.get('https://quotes.toscrape.com', headers=headers)
soup = BeautifulSoup(page.text, 'html.parser')

h1_elements = soup.find_all('h1')
main_title_element = soup.find(id='main')