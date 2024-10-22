from PIL import Image, ImageDraw, ImageFont

def draw_partition_pil(shirina, visota, door, impost_h, impost_v):
    img_width = int(shirina / 5)
    img_height = int(visota / 5)
    img = Image.new('RGB', (img_width + 190, img_height + 120), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)

    # Нарисуем трэк сверху перегородки
    draw.rectangle([50, 20, shirina / 5 + 50, 48], outline="black", fill="grey", width=3)

    # Определение размеров двери
    door_width = img_width / door
    door_height = img_height

    # Рисуем двери с синим стеклом
    for i in range(door):
        # Заполнение синим цветом для имитации стекла
        draw.rectangle([i * door_width + 50, 50, (i + 1) * door_width + 50, 50 + door_height], outline="black", fill="lightblue", width=12)

        # Рисуем вертикальные импосты
        if impost_v > 0:
            for j in range(impost_v):
                x_pos = i * door_width + (j + 1) * door_width / (impost_v + 1) + 50
                draw.line([x_pos, 50, x_pos, 50 + door_height], fill="black", width=5)

        # Рисуем горизонтальные импосты
        if impost_h > 0:
            for k in range(impost_h):
                y_pos = 50 + (k + 1) * door_height / (impost_h + 1)
                draw.line([i * door_width + 50, y_pos, (i + 1) * door_width + 50, y_pos], fill="black", width=5)

    # Линия между дверьми с небольшей толщиной
    for i in range(1, door):
        x_pos = i * door_width + 50
        draw.line([x_pos, 50, x_pos, 50 + door_height], fill="white", width=1)

    # Загрузка шрифта
    font = ImageFont.truetype("arial.ttf", size=30)

    # Поворот текста высоты на 90 градусов
    txt_img = Image.new('RGBA', (100, img_height), (255, 255, 255, 0))
    txt_draw = ImageDraw.Draw(txt_img)
    txt_draw.text((10, img_width / 2), f"{int(shirina)} мм", font=font, fill="black")

    draw.text((img_width / 2, img_height + 60), f"{int(shirina)} мм", font=font, fill="black")
    draw.text((img_width + 60, img_height / 2), f"{int(visota)} мм", font=font, fill="black")

    # Добавляем горизонтальный текст для ширины
    # draw.text((img_width / 2, img_height - 60), f"{int(visota)} мм", font=font, fill="black")
    # # Поворачиваем текст на 90 г радусов и вставляем его на основное изображение
    # rotated_txt_img = txt_img.rotate(90, expand=1)
    # img.paste(rotated_txt_img, (img_width + 60, 50), rotated_txt_img)

    # Показ изображения
    img.show()



#Цена
profile57x15 = 1580
profile30x32 = 1837
profile22 = 1050
krishka = 840
trek_cena = 580
karetok = 1500
uplotnitel = 40
uplotnitel_shyotochni = 35
pokraska = 5000
bolti = 60
rasxodniki = 500
steklo_4mm = 660
zak_steklo_4mm = 1410
steklo_6mm = 900
zak_steklo_6mm = 1605
steklo_8mm = 1545
zak_steklo_8mm = 2540
zamer = 3500


# Раздвижная перегородка
print("Введите ширину перегородки (мм): ")
shirina = float(input())
print("Введите высоту перегородки (мм): ")
visota = float(input())
print("количество дверей (шт.): ")
door = int(input())
print("количество треков (шт.): ")
trek = int(input())
print('Введите количество вертикальных импостов:')
impost_v = int(input())
print('Введите количество горизонтальных импостов:')
impost_h = int(input())
profile_v = 5400
profile_h = 6000
profile_impost = 6000

print('введите толщину стекла 4,6 или 8 (мм):')
steklo = int(input())
print('Выберите тип стекла: введите 1 для закаленного или 0 для обычного')
type_steklo = int(input())


# Расчет 30х32 профиля
j,n,w,k,e,ostatki_V = 0,0,0,1,0,[]
r = True
while r == True:
    if w < door:
        e += 1
        j += visota
        if j > 5400:
            k += 1
            ostatki_V.append(5400-(j-visota))
            j = visota
        n += 1
        if n == 2:
            w += 1
            n = 0
    else:
        ostatki_V.append(5400-j)
        r = False
print(f'Вертикальный профиль {k} шт., из них {ostatki_V} остатки')


# Расчет 57х15 профиля
j_h,n_h,w_h,k_h,e_h,ostatki_H = 0,0,0,1,0,[]
r_h = True
while r_h == True:
    if w_h < door:
        e_h += 1
        j_h += shirina/door
        if j_h > 6000:
            k_h += 1
            ostatki_H.append(6000-(j_h-shirina/door))
            j_h = shirina/door
        n_h += 1
        if n_h == 2:
            w_h += 1
            n_h = 0
    else:
        ostatki_H.append(6000-j_h)
        r_h = False
print(f'Горизонтальный профиль {k_h} шт., из них {ostatki_H} остатки')


# расчет вертикальных профилей при деление или не деление двери

j_i,n_i,w_i,k_i,e_i,ostatki_I = 0,0,0,1,0,[]
r_i = True
while r_i == True:
    if w_i < ((door*impost_v)/2):
        e_i += 1
        j_i += visota
        if j_i > 6000:
            k_i += 1
            ostatki_I.append(6000-(j_i-visota))
            j_i = visota
        n_i += 1
        if n_i == 2:
            w_i += 1
            n_i = 0
    else:
        ostatki_I.append(6000-j_i)
        r_i = False
if impost_v == 0:
    k_i = 0
    print(f'Вертикальный импост профиль {k_i} шт., из них {0} остатки')
else:
    print(f'Вертикальный импост профиль {k_i} шт., из них {ostatki_I} остатки')


#импост горизонтальный
if impost_h == 0:
    k_ih = 0
else:
    c = True
    z = shirina/door
    x = door * impost_h
    for i in ostatki_I:
            while i >= z:
                i -= z
                x -= 1

    j_ih,n_ih,w_ih,k_ih,e_ih,ostatki_iH = 0,0,0,1,0,[]
    r_ih = True
    while r_ih == True:
        if w_ih < door:
            e_ih += 1
            j_ih += shirina/door
            if j_ih > 6000:
                k_ih += 1
                ostatki_iH.append(6000-(j_ih-shirina/door))
                j_ih = shirina/door
            n_ih += 1
            if n_ih == impost_h:
                w_ih += 1
                n_ih = 0
        else:
            ostatki_iH.append(6000-j_ih)
            r_ih = False
    print(f'Горизонтальный импост профиль {k_ih} шт., из них {ostatki_iH} остатки')

print(k, k_h, k_i, k_ih)

# Цена профиля
profiles = (k*profile30x32) + (k_h*profile57x15) + ((k_i+k_ih)*profile22)
print(profiles)

# Цена уплотнители
uplotniteli = ((2 * (shirina/door)) + (2 * visota) + (impost_v * visota * 2) + (2 * impost_h * shirina / door)) * door * 40 * 2 / 1000
print(uplotniteli)

# Цена стекла
area = visota * shirina / 1000000
def glass(steklo, type_steklo):
    global area, steklo_6mm, steklo_4mm, steklo_8mm, zak_steklo_6mm, zak_steklo_4mm, zak_steklo_8mm
    if steklo == 4:
        if type_steklo == 1:
            cena_s = zak_steklo_4mm * area
        if type_steklo == 0:
            cena_s = steklo_4mm * area
    if steklo == 6:
        if type_steklo == 1:
            cena_s = zak_steklo_6mm * area
        if type_steklo == 0:
            cena_s = steklo_6mm * area
    if steklo == 8:
        if type_steklo == 1:
            cena_s = zak_steklo_8mm * area
        if type_steklo == 0:
            cena_s = steklo_8mm * area
    return cena_s
print(glass(steklo, type_steklo))

# Цена трэка, крышки, кореткы и болты + расходники + покраска
treks = trek * shirina * trek_cena/1000
krishki = 2 * krishka * shirina/1000
koretki = karetok * door
bolts = bolti * door
vmeste = treks + koretki + krishki + bolts + rasxodniki + pokraska
print(vmeste)

# Введите сумму монтажа
print("Введите сумму монтажа")
montaj = int(input()) * area

# Введите сумму доставки
print("Введите сумму доставки")
dostavka = int(input())


# Работа
rabota = montaj + dostavka
print(rabota)

sebestoimost = profiles + uplotniteli + int(glass(steklo, type_steklo)) + vmeste + rabota

print(f"Итого себестоимость проекта: {sebestoimost}")


# Пример вызова функции для рисования чертежа
draw_partition_pil(shirina=shirina, visota=visota, door=door, impost_h=impost_h, impost_v=impost_v)
