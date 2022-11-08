import requests

req = requests.get('http://ruonia.ru/files/csv/ruonia_data/21.12.2020.xls')
#print(req.encoding)
#print(req.status_code)
#print(req.cookies)
#print(req.headers)
#print(req.text)
#print(req.json())
#k = req.raw
#stream=True
print(req.raw)