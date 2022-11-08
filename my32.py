import os
import sys
import pandas as pd
from PIL import Image

#nkari formate poxelu dzeve
#os.listdir(r"C:\\Users\\karen\\Desktop\\Ganzer Vier_photos")
#im = Image.open(r"C:\Users\karen\PycharmProjects\pythonProject1\heno.png")
#bg = Image.new("RGB", im.size, (255,255,255))
#bg.paste(im,im)
#bg.save("heno.jpg")
#for i in os.listdir(path="."):
    #if i.count('.png'):
        #print(i)
        #k = i.replace('.png', '.jpg')
        #url = r"C:\Users\karen\PycharmProjects\pythonProject1" + '\\' + i
#print(url)
#for i in os.listdir(r"C:\\Users\\karen\\Desktop\\Ganzer Vier_photos"):
#    if i.count('.png'):
#        print(i)
#        k = i.replace('.png', '.jpg')
#        url = r"C:\\Users\\karen\\Desktop\\Ganzer Vier_photos" + '\\' + i
#        print(url)
#im = Image.open(str(url)).show()
#rgb_im = im.convert('RGB')
#rgb_im.save("colors.jpg")

os.chdir(r"C:\\Users\\karen\\Desktop\\Ganzer Vier_photos - experimental\\")
print(os.listdir())

k = 0
for i in os.listdir(r"C:\\Users\\karen\\Desktop\\Ganzer Vier_photos - experimental"):
    print(i)
    if i.count('.png'):
        image = Image.open(i)
        image_name = str(i) + str(k) + '.png'
        print(image_name)
        image.save(str(image_name))
        k += 1
#image = Image.open(r'C:\Users\karen\Desktop\Ganzer Vier_photos\Untitled.png')
#image.save('resized.png')