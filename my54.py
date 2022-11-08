import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

# Parsing miangamic excelli mej https://sun-diamond.ru/category/smesiteli_1/ saytic
URL_TEMPLATE = "https://sun-diamond.ru/category/smesiteli_1/"
FILE_NAME = r'C://Users//karen//Desktop//test.csv'
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

# Parsing https://www.work.ua/ru/jobs-odesa/?page=2 saytic

URL_TEMPLATE = "https://sun-diamond.ru/category/smesiteli_1/"
r = requests.get(URL_TEMPLATE)
print(r.status_code) # 200 nshanakuma drakan patasxan unenq HTTP serveric
# print(r.text)

soup = bs(r.text, "html.parser")
smesitels_names = soup.find_all('ul', class_="name")
for name in smesitels_names:
    print(name.a)
    print(name.a['href'])

#Smesitells_info = soup.find_all(itemprop="description", class_="summary")
#for info in Smesitells_info:
#    print(info.text)
