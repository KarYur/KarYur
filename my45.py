from PIL import Image
import os

#nkarnere razmerov sortavorelu hamar
os.chdir(r"C:\\Users\\karen\\Desktop\\sax_nkarnere\\")
print(os.listdir(path="."))
for i in os.listdir(path="."):
    url = r"C:\\Users\\karen\\Desktop\\sax_nkarnere\\" + str(i)
    image = Image.open(url)
    if image.width <= 500 and image.height <= 500:
        print(url,image.size)
        image_copy = image.copy()
        copy_url = r"C:\\Users\\karen\\Desktop\\500x500\\" + str(i)
        print(copy_url)
        image_copy.save(copy_url)
    if image.width < 500 and 500 < image.height < 1000:
        print(url,image.size)
        image_copy = image.copy()
        copy_url = r"C:\\Users\\karen\\Desktop\\500x1000\\" + str(i)
        print(copy_url)
        image_copy.save(copy_url)
    if 500 < image.width < 1000 and image.height < 500:
        print(url,image.size)
        image_copy = image.copy()
        copy_url = r"C:\\Users\\karen\\Desktop\\1000x500\\" + str(i)
        print(copy_url)
        image_copy.save(copy_url)
    else:
        image_copy = image.copy()
        copy_url = r"C:\\Users\\karen\\Desktop\\else\\" + str(i)
        print(url, image.size)
        print(copy_url)
        image_copy.save(copy_url)
