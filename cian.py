import bs4
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver  # pip install selenium
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager  # pip install webdriver-manager

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36')
chrome_options.add_argument("--disable-blink-features=AutomationControlled")


with webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                      options=chrome_options) as driver:  # Открываем хром
    driver.get(
        "https://www.cian.ru/cat.php?deal_type=sale&engine_version=2&offer_type=flat&region=1&room1=1&room2=1&room3=1&room4=1&room5=1&room6=1")  # Открываем страницу
    time.sleep(3)  # Время на прогрузку страницы
    soup = bs4.BeautifulSoup(driver.page_source, 'html.parser')
    urls = soup.find_all('div', class_='_93444fe79c--content--lXy9G')
    for url in urls:
        print(url.find_next('a').get('href'))
        get_url = (url.find_next('a').get('href'))
        # headers = {
        #     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        data = requests.get(get_url).text
        time.sleep(2)
        block = BeautifulSoup(data, 'lxml')
        name = block.find('div', class_='a10a3f92e9--container--u51hg')
        print(name.text.strip())
        address = block.find('address')
        print(address.text.strip())
        price = block.find('div', class_='a10a3f92e9--amount--ON6i1')
        print(price.text.strip())
        param = []
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

        print('\n')
