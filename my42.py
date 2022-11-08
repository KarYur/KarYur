import pandas as pd
import os
import requests

#format picturesic heto nkarneri anunnere exceli mej senc formatov '/V013541(0).jpg, /V013541(1).jpg, ' dnelu hamar
os.chdir(r'C://Users//karen//Desktop//')
# print(os.listdir())
dic = {}
j = 0
file = pd.read_excel('eee.xlsx')
for i in file['Artikul']:
    dic[i] = file['silki'][j].split(' ')
    j += 1
#print(dic)
# print(dic['V013521'])
bararan = {}
for i in dic:
    n = 0
    image_name = ''
    for k in dic[i]:

        #print(i, k)
        image_name += '/' + i + '(' + str(n) + ')' + '.jpg' + '; '
        #print(image_name)
        n += 1
    bararan[i] = image_name

for i in bararan.values():
    print(i)
