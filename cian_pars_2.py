import requests # pip install requests
from bs4 import BeautifulSoup # pip install bs4
# pip install lxml


url = 'https://www.cian.ru/cat.php?deal_type=sale&engine_version=2&offer_type=flat&region=1&room1=1&room2=1&room3=1&room4=1&room5=1&room6=1'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
data = requests.get(url, headers=headers).text
block = BeautifulSoup(data, 'lxml')
urls = block.find_all('div', class_='_93444fe79c--content--lXy9G')
for url in urls:
    print(url.find_next('a').get('href'))
