import pandas as pd
from PIL import Image
import requests
import os

dic = {}
file = pd.read_excel(r"C:\\Users\\karen\\Desktop\\Ganzer Vier - Copy.xlsx")
for i in range(len(file['Артикул'])):
    # print(file['Артикул'][i])
    # print(file['Картинки'][i])
    dic[(file['Артикул'][i])] = file['Картинки'][i]


os.chdir(r"C:\\Users\\karen\\Desktop\\GZ\\")
for i in dic:
    #print(i)
    qurl = dic[i].split()
    #print(qurl)
    k = 1
    for url in qurl:
        #print(url)
        #print(i)
        raw = requests.get(url, stream=True).raw
        image = Image.open(raw)
        if url.count('.png'):
            image_name = i + '(' + str(k) + ')' + '.png'
        if url.count('.jpg'):
            image_name = i + '(' + str(k) + ')' + '.jpg'
        print(image_name)
        image.save(str(image_name))
        #print(os.listdir())
        k += 1