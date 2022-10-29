# parsing with def
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
    items = soup.find_all('div', class_="product-cards-layout__item")
    cards = []
    print(items)

    for item in items:
        cards.append(
            {
                'title': item.find('div', class_="product-title product-title--mobile").get_text(strip=True),
                'link_product': HOST + item.find('div', class_="product-title product-title--mobile").find('a').get('href'),
                'card_img': HOST + item.find('div', class_="mobile-img ng-star-inserted").find('img').get('srcset'),
            }
        )
    return cards


def save_doc(items, path):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Название продукта', 'Ссылка на продукт', 'Изображение карты'])
        for item in items:
            writer.writerow([item['title'], item['link_product'], item['card_img']])


def parser():
    PAGENATION = input('Укажите количество страниц для парсинга: ')
    PAGENATION = int(PAGENATION.strip())
    html = get_html(URL)
    if html.status_code == 200:
        cards = []
        for page in range(1, PAGENATION):
            print(f'Парсим страницу: {page}')
            html = get_html(URL, params={'': page})
            cards.extend(get_content(html.text))
            save_doc(cards, CSV)
        print(cards)
    else:
        print('Error')


parser()
