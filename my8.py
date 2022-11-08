import requests

with open(r'C:/Users/karen/Downloads/dataset_3378_3.txt') as file:
    link = file.read().strip()
url = "https://stepic.org/media/attachments/course67/3.6.3/"
r = url + requests.get(link).text
while 1:
    if requests.get(r).text.count('We') >= 1:
        print(requests.get(r).text)
        break
    r = url + requests.get(r).text
    print(r)