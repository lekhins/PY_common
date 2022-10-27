import requests
from bs4 import BeautifulSoup

URL = 'https://auto.ru/cars/vaz/all/'
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    'accept': '*/*'}


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='ListingItem')

    cars = []
    for item in items:
        cars.append({
            'title': item.find('h3', class_='ListingItemTitle').get_text(strip=True)
            # 'link': item.find('a', class_="css-1dlmvcl ewrty961").get('href'),
        })
        print(cars)


def parse():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)
    else:
        print('Error')


parse()
