#47 i mej te kar vor url hascen 404 error er talis, es grvelaa vor stugvi sax, ete error lini

import requests
from PIL import Image

#raw = requests.get('http://sanroyal.ru/upload/iblock/d08/2zl2601fu2lwrf1b6hzu3jrxaja5lpu0.jpg', stream=True).raw
#image = Image.open(raw)
#image.show()

#card = Image.new("RGB", (220, 220), (255, 255, 255))
#img = Image.open(r"C:\\Users\\karen\\Desktop\\H10029(1).png")
#x, y = img.size
#print(x,y)
#card.paste(img, (0, 0, x, y), img)
#card.save(r"C:\\Users\\karen\\Desktop\\test.png")


image = Image.open(r"C:\\Users\\karen\\Desktop\\H10029(1).png").convert("RGBA")
new_image = Image.new("RGBA", image.size, (255, 255, 255))
x, y = image.size
new_image.paste(image, (0, 0, x, y), image)
new_image.save(r"C:\\Users\\karen\\Desktop\\H10029.png", format="png")

