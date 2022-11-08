import pandas as pd
from PIL import Image
import requests
import os

dic = {}
file = pd.read_excel(r"C:\\Users\\karen\\Desktop\\all1.xlsx")
for i in range(len(file['Артикул'])):
    # print(file['Артикул'][i])
    # print(file['Картинки'][i])
    dic[(file['Артикул'][i])] = file['Картинки'][i]


os.chdir(r"C:\\Users\\karen\\Desktop\\New folder (2)\\")
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

os.chdir(r"C:\\Users\\karen\\Desktop\\New folder (2)\\")
print(os.listdir(path="."))
for image_name in os.listdir(path="."):
    print(image_name)
    image_url1 = str(image_name)
    image_url2 = image_name.replace('png', 'jpg')
    print(image_url2)
    img = Image.open(str(image_url1)).convert("RGBA")
    x, y = img.size
    new_image = Image.new("RGB", img.size, (255, 255, 255))
    new_image.paste(img,(0,0,x,y), img)
    new_image.save(str(image_url2))

directory = r"C:\\Users\\karen\\Desktop\\New folder (2)\\"
files = os.listdir(directory)
for i in files:
    if i.endswith('.png'):
        path = f'{directory}\\{i}'
        print(path)
        os.remove(path)