import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

# Parsing miangamic excelli mej https://www.work.ua/ru/jobs-odesa/?page=2 saytic
URL_TEMPLATE = "https://www.work.ua/ru/jobs-odesa/?page=2"
FILE_NAME = r'C://Users//karen//Desktop//test.csv'

def parse(url = URL_TEMPLATE):
    result_list = {'href': [], 'title': [], 'about' : []}
    r = requests.get(url)
    soup = bs(r.text, "html.parser")
    vacancies_names = soup.find_all('h2', class_="")
    vacancies_info = soup.find_all('p', class_="overflow text-muted add-top-sm cut-bottom")
    for name in vacancies_names:
        result_list['href'].append('https://www.work.ua' + name.a['href'])
        result_list['title'].append(name.a['title'])
    for info in vacancies_info:
        result_list['about'].append(info.text)
    return result_list

df = pd.DataFrame(data=parse())
df.to_csv(FILE_NAME)