# parsing with def
import requests
from bs4 import BeautifulSoup
from time import sleep
import csv

CSV = 'cards.csv'
HOST = 'https://www.vbr.ru/'
URL = 'https://www.vbr.ru/banki/kreditnyekarty/'
HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}


def get_html(url, params=''):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all('div', class_="product-card-cell")
    cards = []

    for item in items:
        cards.append(
            {
                'title': item.find('div', class_="product-card-head").get_text(strip=True),
                'link_product': HOST + item.find('div', class_="product-card-head").find('a').get('href'),
                'brand': item.find('div', class_="w100pr").get_text(strip=True),
                'card_img': HOST + item.find('div', class_="product-card-img").find('img').get('src'),
            }
        )
    return cards
