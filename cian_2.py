import re

text = "Найдено 210 объявлений"

number = re.findall(r'\d+', text)[0]
print(number)

