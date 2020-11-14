import requests
from bs4 import BeautifulSoup

BASE_URL_MILANUNCIOS = 'https://www.milanuncios.com'
RELATIVE_URLS = 'motor-en-canarias/camper.htm?fromSearch=1&desde=500&hasta=25000'

class Milanuncios:
    def fetch(self):
        web = requests.get(f'{BASE_URL_MILANUNCIOS}/{RELATIVE_URLS}')
        if web.status_code != 200:
            logging.error(f'Cant fech {BASE_URL_MILANUNCIOS}')
        return web.content

    def parse(self, page):
        bs = BeautifulSoup(page, 'html.parser')
        items = bs.find_all('div', class_='aditem ProfesionalCardTestABClass')

        items = [i.find('div', class_='aditem-detail') for i in items]
        return[
            {
                'content': i.find('div', class_='tx').text,
                'header': i.find('a', class_='aditem-detail-title').text,
                'price': i.find('div', class_='aditem-price').text,
                'link': f"{BASE_URL_MILANUNCIOS}{i.find('a', class_='aditem-detail-title').href}"
            }
                for i in items
        ]
