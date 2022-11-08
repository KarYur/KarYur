from PIL import Image
import os, sys

im = Image.open(r"C:\Users\karen\PycharmProjects\pythonProject1\heno.png")
bg = Image.new("RGB", im.size, (255,255,255))
bg.paste(im,im)
bg.save("heno.jpg")



