import csv
import requests
from bs4 import BeautifulSoup
import bs4
import time
from selenium import webdriver  # pip install selenium
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager  # pip install webdriver-manager

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36')
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
# chrome_options.headless = True

print(
    'Выберите ркгион из списка: Москва и МО, Санкт-Петербург и ЛО, Екатеринбург, Краснодар, Новосибирск, Красноярск, Челябинск, Ростов-на-Дону, Тюмень, Уфа, Казань, Пермь, Нижний Новгород, Самара, Саратов, Омск, Балашиха, Волгоград, Воронеж, Иркутск, Хабаровск, Томск, Ярославль, Сочи, Сургут, Подольск, Мытищи, Владивосток, Калуга, Пятигорск')
gorod = input()
city = ''
if gorod == 'Москва и МО':
    city = 1
elif gorod == 'Санкт-Петербург и ЛО':
    city = 2
elif gorod == 'Екатеринбург':
    city = 4743
elif gorod == 'Краснодар':
    city = 4820
elif gorod == 'Новосибирск':
    city = 4897
elif gorod == 'Красноярск':
    city = 4827
elif gorod == 'Челябинск':
    city = 5048
elif gorod == 'Ростов-на-Дону':
    city = 4959
elif gorod == 'Тюмень':
    city = 5024
elif gorod == 'Уфа':
    city = 176245
elif gorod == 'Казань':
    city = 4777
elif gorod == 'Пермь':
    city = 4927
elif gorod == 'Нижний Новгород':
    city = 4885
elif gorod == 'Самара':
    city = 4966
elif gorod == 'Саратов':
    city = 4969
elif gorod == 'Омск':
    city = 4914
elif gorod == 'Балашиха':
    city = 174292
elif gorod == 'Волгоград':
    city = 4704
elif gorod == 'Воронеж':
    city = 4713
elif gorod == 'Иркутск':
    city = 4774
elif gorod == 'Хабаровск':
    city = 5039
elif gorod == 'Томск':
    city = 5016
elif gorod == 'Ярославль':
    city = 5075
elif gorod == 'Сочи':
    city = 4998
elif gorod == 'Сургут':
    city = 5003
elif gorod == 'Подольск':
    city = 4935
elif gorod == 'Мытищи':
    city = 175378
elif gorod == 'Владивосток':
    city = 4701
elif gorod == 'Калуга':
    city = 4780
elif gorod == 'Пятигорск':
    city = 4951
# else:
#     print('Введите корректный запрос...')

print(
    'Введите раздел коммерческой недвижимости: оффис, торговая площадь, склад, производство, здание, помещение свободного назначения, готовый бизнес, гараж')
room = input().lower()
vidned = ''
if room == 'оффис':
    vidned = 1
elif room == 'торговая площадь':
    vidned = 2
elif room == 'склад':
    vidned = 3
elif room == 'производство':
    vidned = 7
elif room == 'здание':
    vidned = 11
elif room == 'помещение свободного назначения':
    vidned = 5
elif room == 'готовый бизнес':
    vidned = 10
elif room == 'гараж':
    vidned = 6
else:
    print('Введите корректные данные')
print('Выберите нужный раздел: аренда, продажа')
razdel = input()
tema = ''
if razdel == 'аренда':
    tema = 'rent'
elif razdel == 'продажа':
    tema = 'sale'
else:
    print('Введите корректный запрос')
print('Введите имя файла')
file_name = input().lower()

count = 1
while True:
    with webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=chrome_options) as driver:  # Открываем хром
        driver.get(
            f"https://www.cian.ru/cat.php?deal_type={tema}&engine_version=2&offer_type=offices&office_type%5B0%5D={vidned}&p={count}&region={city}")  # Открываем страницу
        time.sleep(5)  # Время на прогрузку страницы
        soup = bs4.BeautifulSoup(driver.page_source, 'html.parser')
        print(city)
        urls = soup.find_all('div', class_='_32bbee5fda--offer-title-content-container--_kUhi')
        for url in urls:
            print(url.find_next('a').get('href'))

            get_url = (url.find_next('a').get('href'))
            data = requests.get(get_url).text
            time.sleep(5)  # Время на прогрузку страницы
            block = BeautifulSoup(data, 'lxml')
            # Время на прогрузку страницы
            try:
                name = block.find('h1', class_='a10a3f92e9--title--vlZwT')
                print(name.text.strip())
                head = (name.text.strip())
            except:
                # name = block.find('div', class_='a10a3f92e9--header--cUtKM').find('h1', class_='a10a3f92e9--title--vlZwT')
                # print(name.text.strip())
                # head = (name.text.strip())
                print('None')
                head = 'None'
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
            try:
                pixes = block.find('ul', class_='a10a3f92e9--container--C9mtE').find_all('li')

                photo_1 = (pixes[0].find_next('img', src=True))
                print(photo_1['src'])
                pix_1 = (photo_1['src'])
                try:
                    photo_2 = (pixes[1].find_next('img', src=True))
                    print(photo_2['src'])
                    pix_2 = (photo_2['src'])
                except:
                    print('None')
                    pix_2 = 'None'
                try:
                    photo_3 = (pixes[2].find_next('img', src=True))
                    print(photo_3['src'])
                    pix_3 = (photo_3['src'])
                except:
                    print('None')
                    pix_3 = 'None'
                try:
                    photo_4 = (pixes[3].find_next('img', src=True))
                    print(photo_4['src'])
                    pix_4 = (photo_4['src'])
                except:
                    print('None')
                    pix_4 = 'None'
                photo_5 = (pixes[4].find_next('img', src=True))
                print(photo_5['src'])
                pix_5 = (photo_5['src'])
            except:
                pixes = block.find('ul', class_='a10a3f92e9--container--RuwgA').find_all('li')
                try:
                    photo_1 = (pixes[0].find_next('img', src=True))
                    print(photo_1['src'])
                    pix_1 = (photo_1['src'])
                except:
                    print('None')
                    pix_1 = 'None'
                try:
                    photo_2 = (pixes[1].find_next('img', src=True))
                    print(photo_2['src'])
                    pix_2 = (photo_2['src'])
                except:
                    print('None')
                    pix_2 = 'None'
                try:
                    photo_3 = (pixes[2].find_next('img', src=True))
                    print(photo_3['src'])
                    pix_3 = (photo_3['src'])
                except:
                    print('None')
                    pix_3 = 'None'
                try:
                    photo_4 = (pixes[3].find_next('img', src=True))
                    print(photo_4['src'])
                    pix_4 = (photo_4['src'])
                except:
                    print('None')
                    pix_4 = 'None'
                try:
                    photo_5 = (pixes[4].find_next('img', src=True))
                    print(photo_5['src'])
                    pix_5 = (photo_5['src'])
                except:
                    print('None')
                    pix_5 = 'None'
                    continue

            print('\n')

            storage = {'name': head, 'adress': addr, 'price': cena, 'params': ';'.join(all_charact), 'url': get_url,
                       'photo_1': pix_1, 'photo_2': pix_2, 'photo_3': pix_3, 'photo_4': pix_4,
                       'photo_5': pix_5}

            with open(f'{file_name}.csv', 'a+', encoding='utf-16') as f:
                pisar = csv.writer(f, delimiter=';', lineterminator='\r')
                pisar.writerow(
                    [storage['name'], storage['adress'], storage['price'], storage['params'], storage['url'],
                     storage['photo_1'],
                     storage['photo_2'],
                     storage['photo_3'],
                     storage['photo_4'],
                     storage['photo_5']])
    count += 1
