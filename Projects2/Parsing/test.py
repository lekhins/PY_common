import requests
from bs4 import BeautifulSoup
from time import sleep
import csv

CSV = 'cards.csv'
HOST = 'https://www.mvideo.ru/'
URL = 'https://www.mvideo.ru/pylesosy-i-aksessuary-2428/pylesosy-2438'
HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
}


def get_html(url, params=''):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all('div', class_="ng-star-inserted")
    cards = []

    for item in items:
        cards.append(
            {
                'title': item.find('div', class_="product-title product-title--mobile").get_text(strip=True),
                'link_product': HOST + item.find('div', class_="product-title product-title--mobile").find('a').get('href'),
                'card_img': HOST + item.find('div', class_="mobile-img ng-star-inserted").find('img').get('srcset'),
            }
        )
    return cards