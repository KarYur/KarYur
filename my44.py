from PIL import Image

#hzor nkarneri redaktor
image = Image.open(r'C:\\Users\\karen\\Desktop\\GZ01031.jpg')
#image.show()
print(image.format)# Формат исходного файла.
print(image.mode)# Формат пикселей, используемый изображением. Типичные значения: «1», «L», «RGB» или «CMYK».
print(image.size)# Размер изображения в пикселях. Размер задается как 2-кортеж (ширина, высота).
print(image.palette) # Таблица цветовой палитры, если есть.
#Когда вы закончите обработку изображения,
#вы можете сохранить его в файл с помощью метода save(),
# передав имя, которое будет использоваться для обозначения файла изображения.
# При сохранении изображения вы можете указать расширение, отличное от его оригинала,
# и сохраненное изображение будет преобразовано в указанный формат.
#image = Image.open('demo_image.jpg')
#image.save('new_image.png') или image.save('new_image.png', 'PNG')

# chapere poxum enq bayc zoom -a anum nkare
#image = Image.open(r'C:\\Users\\karen\\Desktop\\H10001.jpg')
#new_image = image.resize((1916,1970))
#new_image.save(r'C:\\Users\\karen\\Desktop\\H10001_test.jpg')
#print(image.size)
#print(new_image.size)

# chapere poxum enq bayc zoom -chi anum nkare
#image = Image.open(r'C:\\Users\\karen\\Desktop\\H10001.jpg')
#print(image.size)
#image.thumbnail((1916,1970))
#image.save(r'C:\\Users\\karen\\Desktop\\H10001_test.jpg')
#print(image.size)

#nkare ktrum enq (minus chapernel avelanuma nkari koxqeric sev fonov)
#image = Image.open(r'C:\\Users\\karen\\Desktop\\H10001.jpg')
#box = (-250,-100,700,800)
#cropped_image = image.crop(box)
#cropped_image.save(r'C:\\Users\\karen\\Desktop\\H10001_test.jpg')
#print(cropped_image.size)

#fonenq sarqum(12 anunov) vren dnumenq logo-n` foni mejtexic
#image = Image.open(r'C:\\Users\\karen\\Desktop\\12.jpg')
#logo = Image.open(r'C:\\Users\\karen\\Desktop\\GZ01031.jpg')
#image_copy = image.copy()
#pos1 = int(logo.width/2)
#pos2 = int(logo.height/2)
#pos3 = int(image.width/2)
#pos4 = int(image.height/2)
#print(pos1,pos2,pos3,pos4)
#position = ((pos3-pos1), (pos4-pos2))
#image_copy.paste(logo,position)
#image_copy.save(r'C:\\Users\\karen\\Desktop\\pasted_image1.jpg')




