from PIL import Image
import pandas as pd
import os
import requests

#sax nkarnere excelic qashuma sarguma jpg u qcuma ekrani vrai Vieir fili mej
os.chdir(r'C://Users//karen//Desktop//')
# print(os.listdir())
dic = {}
j = 0
file = pd.read_excel('1.xlsx')
for i in file['Artikul']:
    dic[i] = file['silki'][j].split(' ')
    j += 1
# print(dic)
# print(dic['V013521'])
os.chdir(r'C://Users//karen//Desktop//Vieir')
n = 0
for i in dic:
    n = 0
    for k in dic[i]:
        if k.count('.png'):
            print(i, k, '.png')
            img = requests.get(k, stream=True).raw
            image = Image.open(img)
            image_name = i + '(' + str(n) + ')' + '.jpg'
            img = image.save(image_name, 'jpeg')
            n += 1
        if k.count('.jpg'):
            print(i, k, '.jpg')
            img = requests.get(k, stream=True).raw
            image = Image.open(img)
            image_name = i + '(' + str(n) + ')' + '.jpg'
            img = image.save(image_name, 'jpeg')
            n += 1
        if k.count('.webp'):
            print(i, k, '.webp')
            img = requests.get(k, stream=True).raw
            image = Image.open(img)
            image_name = i + '(' + str(n) + ')' + '.jpg'
            img = image.save(image_name, 'jpeg')
            n += 1
        if k.count('.jpeg'):
            print(i, k, '.jpeg')
            img = requests.get(k, stream=True).raw
            image = Image.open(img)
            image_name = i + '(' + str(n) + ')' + '.jpeg'
            img = image.save(image_name, 'jpeg')
            n += 1
        if k.count('/orig'):
            print(i, k, '/orig')
            img = requests.get(k, stream=True).raw
            image = Image.open(img)
            image_name = i + '(' + str(n) + ')' + '.jpg'
            img = image.save(image_name, 'jpeg')
        if k.count('.gif'):
            print(i, k, '.gif')
            img = requests.get(k, stream=True).raw
            image = Image.open(img)
            image_name = i + '(' + str(n) + ')' + '.jpg'
            img = image.save(image_name, 'jpeg')
            n += 1
