import requests

from pprint import pprint

url = ' https://currate.ru/api/?get=rates&pairs=USDRUB,EURRUB&key=25ec6aa2f0f7b53aa53ba28d9e7fdc54'
homework_statuses = requests.get(url)

# А можно ответ в формате JSON привести к типам данных Python и напечатать и его
pprint(homework_statuses.json())