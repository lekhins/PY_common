# код без функций и ООП
# https://www.youtube.com/watch?v=lOfm04oLD1U&list=WL&index=11&t=1984s
import \
    requests  # позволяет отправлять https запросы к сайтами и получать от них ответ (те html-код конкретной страницы)
from bs4 import BeautifulSoup  # производит поиск интересующих нас элементов в этом(сверху) html-коде
import \
    lxml  # это спец парсер, который помогает анализировать полученный код с помощью requests и подготавливает его в удобочитаемый вид для bs4
from time import \
    sleep  # позволяет щаморозить работу скрипта на определенное количество секунд (для того, чтобы система при парсинге  не приняла меня за бота)

# list_card_url = [] #
host = 'https://scrapingclub.com/'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}  # (для того, чтобы система при парсинге  не приняла меня за бота)


def download(url):
    resp = requests.get(url, stream=True)
    r = open(r"C:\Users\M108_User\PycharmProjects\repka4\PRACTICE\\image\\" + url.split('/')[-1] + "wb")
    for value in resp.iter_content(1024 * 1024):
        r.write(value)
    r.close()


def get_url():
    for count in range(1, 8):
        # sleep(1)  # сколько сек перерыва
        url = f"https://scrapingclub.com/exercise/list_basic/?page={count}"
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text,
                             'lxml')  # это html.parser (анализатор html-кода). Похожий инструмент - html.parcer
        data = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
        for i in data:
            card_url = host + i.find('a').get('href')
            yield card_url


def array():
    for card_url in get_url():
        response = requests.get(card_url, headers=headers)
        sleep(1)
        soup = BeautifulSoup(response.text, 'lxml')
        data = soup.find('div', class_='card mt-4 my-4')
        name = data.find('h3', class_='card-title').text
        price = data.find('h4').text
        text = data.find('p', class_='card-text').text
        url_img = host + data.find('img', class_='card-img-top img-fluid').get('src')
        download(url_img)
        yield name, price, text, url_img

    # print(card_url)

    # name = i.find('h4', class_='card-title').text.replace('\n', '')
    # price = i.find('h5').text
    # url_img = host + i.find('img', class_='card-img-top img-fluid').get('src')
    # print(name + '\n' + price + '\n' + url_img + '\n\n')
