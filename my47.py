import pandas as pd
from PIL import Image
import requests
import os

#excelic nkarnere qashel formate poxel u save anel mihat file-i mej, anunnernel (1)..(n) avelacnelov
dic = {}
file = pd.read_excel(r"C:\\Users\\karen\\Desktop\\обновление.xlsx")
for i in range(len(file['Артикул'])):
    #print(file['Артикул'][i])
    #print(file['Новый набор ссылок'][i])
    dic[(file['Артикул'][i])] = file['Новый набор ссылок'][i]
#print(file.head(len(file)))
#print(dic['H10001'])
#print(dic)


os.chdir(r"C:\\Users\\karen\\Desktop\\Hansen_photos\\")
for i in dic:
    try:
        qurl = dic[i].split()
    except AttributeError:
        dic[i] = '#N/A'
        qurl = dic[i]
    #print(i)
    qurl = dic[i].split()
    #print(qurl)
    k = 1
    for url in qurl:
        if url.count('#N/A'):
            continue
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


os.chdir(r"C:\\Users\\karen\\Desktop\\Hansen_photos\\")
print(os.listdir(path="."))
for image_name in os.listdir(path="."):
    if image_name.count('.png'):
        print(image_name)
        image_url1 = str(image_name)
        image_url2 = image_name.replace('png', 'jpg')
        print(image_url2)
        image = Image.open(str(image_url1))
        new_image = Image.new("RGB", image.size, (255, 255, 255))
        new_image.paste(image, image)
        new_image.save(str(image_url2))

directory = r"C:\\Users\\karen\\Desktop\\Hansen_photos\\"
files = os.listdir(directory)
for i in files:
    if i.endswith('.png'):
        path = f'{directory}\\{i}'
        print(path)
        os.remove(path)
