import csv

import bs4
import time
from selenium import webdriver  # pip install selenium
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager  # pip install webdriver-manager

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36')
chrome_options.add_argument("--disable-blink-features=AutomationControlled")

count = 1
while True:
    with webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=chrome_options) as driver:  # Открываем хром
        driver.get(
            f"https://samara.cian.ru/cat.php?deal_type=rent&engine_version=2&offer_type=flat&p={count}&region=4966")  # Открываем страницу
        time.sleep(5)  # Время на прогрузку страницы
        soup = bs4.BeautifulSoup(driver.page_source, 'html.parser')
        urls = soup.find_all('div', class_='_93444fe79c--content--lXy9G')
        for url in urls:
            print(url.find_next('a').get('href'))
            get_url = (url.find_next('a').get('href'))
            with webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                                  options=chrome_options) as driver:  # Открываем хром
                driver.get(
                    get_url)  # Открываем страницу
                time.sleep(2)  # Время на прогрузку страницы
                block = bs4.BeautifulSoup(driver.page_source, 'html.parser')
                try:
                    name = block.find('div', class_='a10a3f92e9--container--u51hg')
                    print(name.text.strip())
                    head = (name.text.strip())
                except:
                    name = block.find('div', class_='detail-top--name tmp-font--big_bold')
                    print(name.text.strip())
                    head = (name.text.strip())
                address = block.find('address')
                print(address.text.strip())
                addr = (address.text.strip())
                price = block.find('div', class_='a10a3f92e9--amount--ON6i1')
                print(price.text.strip())
                cena = (price.text.strip())
                params = block.find('div', class_='a10a3f92e9--container--tqDAE').find_all('div',

                                                                                           class_='a10a3f92e9--text--eplgM')
                all_charact = []
                for i in params:
                    charact_1 = i.find_all_next('span',
                                                class_='a10a3f92e9--color_gray60_100--mYFjS a10a3f92e9--lineHeight_4u--E1SPG a10a3f92e9--fontWeight_normal--JEG_c a10a3f92e9--fontSize_12px--pY5Xn a10a3f92e9--display_block--KYb25 a10a3f92e9--text--e4SBY a10a3f92e9--text_letterSpacing__0--cQxU5')
                    # print(charact_1[0].text.strip())
                    param_1 = (charact_1[0].text.strip())
                    chract_2 = i.find_all_next('span',
                                               class_='a10a3f92e9--color_black_100--Ephi7 a10a3f92e9--lineHeight_6u--cedXD a10a3f92e9--fontWeight_bold--BbhnX a10a3f92e9--fontSize_16px--QNYmt a10a3f92e9--display_block--KYb25 a10a3f92e9--text--e4SBY')
                    # print(chract_2[0].text.strip())
                    param_2 = (chract_2[0].text.strip())
                    all_params = (param_1 + ':' + ' ' + param_2)
                    print(all_params)
                    all_charact.append(all_params)
                pixes = block.find('ul', class_='a10a3f92e9--container--RuwgA').find_all('li')
                photo_1 = (pixes[0].find_next('img', src=True))
                print(photo_1['src'])
                photo_2 = (pixes[1].find_next('img', src=True))
                print(photo_1['src'])
                photo_3 = (pixes[2].find_next('img', src=True))
                print(photo_1['src'])
                photo_4 = (pixes[3].find_next('img', src=True))
                print(photo_1['src'])
                photo_5 = (pixes[4].find_next('img', src=True))
                print(photo_1['src'])

                print('\n')

                # storage = {'name': head, 'adress': addr, 'price': cena, 'params': ';'.join(all_charact), 'url': get_url,
                #            'photo_1': photo_1, 'photo_2': photo_2, 'photo_3': photo_3, 'photo_4': photo_4,
                #            'photo_5': photo_5}

                # with open('cian_pars.csv', 'a+', encoding='utf-16') as f:
                #     pisar = csv.writer(f, delimiter=';', lineterminator='\r')
                #     pisar.writerow(
                #         [storage['name'], storage['adress'], storage['price'], storage['params'], storage['url'],
                #          storage['photo_1'],
                #          storage['photo_2'],
                #          storage['photo_3'],
                #          storage['photo_4'],
                #          storage['photo_5']])
        count += 1
