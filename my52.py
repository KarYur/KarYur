import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

# Parsing https://www.work.ua/ru/jobs-odesa/?page=2 saytic

URL_TEMPLATE = "https://www.work.ua/ru/jobs-odesa/?page=2"
r = requests.get(URL_TEMPLATE)
print(r.status_code) # 200 nshanakuma drakan patasxan unenq HTTP serveric
# print(r.text)

soup = bs(r.text, "html.parser")
vacancies_names = soup.find_all('h2', class_="")
for name in vacancies_names:
    print(name.a['title'])

#vacancies_info = soup.find_all('p', class_="overflow text-muted add-top-sm cut-bottom")
#for name in vacancies_info:
#    print('https://www.work.ua' + name.a['href'])
#for info in vacancies_info:
#    print(info.text)


