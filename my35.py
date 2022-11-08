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
# print(file.head(len(file)))
# print(dict['GZ01011'])


os.chdir(r"C:\\Users\\karen\\Desktop\\Ganzer Vier_photos\\")
for i in dic:
    # print(i)
    qurl = dic[i].split()
    print(qurl)
    k = 1
    for url in qurl:
        print(url)
        print(i)
        if url.count('png'):
            raw = requests.get(url, stream=True).raw
            image = Image.open(raw)
            image_name = i + '(' + str(k) + ')' + '.png'
            print(image_name)
            image.save(str(image_name))
            print(os.listdir())
            k += 1

os.chdir(r"C:\\Users\\karen\\Desktop\\Ganzer Vier_photos\\")
print(os.listdir(path="."))
for image_name in os.listdir(path="."):
    print(image_name)
    image_url1 = str(image_name)
    image_url2 = image_name.replace('png', 'jpg')
    print(image_url2)
    image = Image.open(str(image_url1))
    new_image = Image.new("RGB", image.size, (255, 255, 255))
    new_image.paste(image, image)
    new_image.save(str(image_url2))

directory = r"C:\\Users\\karen\\Desktop\\Ganzer Vier_photos\\"
files = os.listdir(directory)
for i in files:
    if i.endswith('.png'):
        path = f'{directory}\\{i}'
        print(path)
        os.remove(path)
