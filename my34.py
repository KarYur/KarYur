import pandas as pd
from io import BytesIO
from PIL import Image
import requests
import pandas
import os

#file = pd.read_excel(r"C:\\Users\\karen\\Desktop\\New.xlsx")
#print(file.head(len(file)))

os.chdir(r"C:\\Users\\karen\\Desktop\\Ganzer Vier_photos\\")
s, urls = [], []
file = open(r"C:\\Users\\karen\\Desktop\\New.txt")
for i in file:
    s.append(i.strip().split())
for i in range(len(s)):
    for j in range(len(s[i])):
        urls.append(s[i][j])
print(urls)
k = 0
for url in urls:
    #print(url)
    if url.count('png'):
        raw = requests.get(url, stream=True).raw
        image = Image.open(raw)
        image_name = str(k) + '.png'
        print(image_name)
        image.save(str(image_name))
        print(os.listdir())
        k += 1









