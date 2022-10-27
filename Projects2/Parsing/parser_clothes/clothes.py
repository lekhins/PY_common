# parsing with def
import requests
from bs4 import BeautifulSoup
import lxml.html

list_card_url = []
headers = {
    'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/87.0.4280.77 Mobile/15E148 Safari/604.1'
}


url = 'https://www.lamoda.ru/c/515/clothes-muzhskie-rubashki-i-sorochki/?sitelink=topmenuM&l=9'
HOST = 'https:'
DOMAIN = 'https://www.lamoda.ru'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'lxml')

data = soup.find_all('div', class_='x-product-card__card')

for i in data:
    card_url = DOMAIN + i.find('a').get('href')
    list_card_url.append(card_url)
    print(list_card_url)