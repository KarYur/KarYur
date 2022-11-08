import requests

with open(r"C:\Users\karen\Downloads\dataset_3378_3.txt") as file:
    file = file.read().strip()
print(file)
while 1:
    r = requests.get(file)
    r = r.text
    if r[0:2] == 'We':
        print(r)
        break
    print(r)
    url = "https://stepic.org/media/attachments/course67/3.6.3/"
    file = url + r
    print(file)
