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
print('Выберите тип стекла: закаленное/сырое')
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

# print(k, k_h, k_i, k_ih)

# Цена профиля
profiles = (k*profile30x32) + (k_h*profile57x15) + ((k_i+k_ih)*profile22)
# print(profiles)

# Цена уплотнители
uplotniteli = ((2 * (shirina/door)) + (2 * visota) + (impost_v * visota * 2) + (2 * impost_h * shirina / door)) * door * 40 * 2 / 1000
# print(uplotniteli)

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
# print(glass(steklo, type_steklo))

# Цена трэка, крышки, кореткы и болты + расходники + покраска
treks = trek * shirina * trek_cena/1000
krishki = 2 * krishka * shirina/1000
koretki = karetok * door
bolts = bolti * door
vmeste = treks + koretki + krishki + bolts + rasxodniki + pokraska
# print(vmeste)

# Введите сумму монтажа
print("Введите сумму монтажа")
montaj = int(input()) * area

# Введите сумму доставки
print("Введите сумму доставки")
dostavka = int(input())


# Работа
rabota = montaj + dostavka
# print(rabota)

sebestoimost = profiles + uplotniteli + int(glass(steklo, type_steklo)) + vmeste + rabota

print("себестоимость = ",sebestoimost)

print(profiles, uplotniteli, int(glass(steklo, type_steklo)), vmeste, rabota)



import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import tkinter as tk
from tkinter import simpledialog


def draw_partition(shirina, visota, door, impost_v,impost_h):
    width = shirina / 1000  # переводим в метры для визуализации
    height = visota / 1000  # переводим в метры для визуализации

    fig, ax = plt.subplots()

    # Общая рамка перегородки (периметр)
    ax.add_patch(Rectangle((0, 0), width, height, fill=False, edgecolor="black", linewidth=5))  # Толстая рамка

    # Деление на двери
    door_width = width / door
    for i in range(door):
        # Рисуем каждую дверь с выбранным материалом
        ax.add_patch(
            Rectangle((i * door_width, 0), door_width, height, fill=True, facecolor="lightblue", edgecolor="black",
                      linewidth=5))

        # Если пользователь выбрал вертикальное деление дверей
        if impost_v:
            ax.plot([i * door_width + door_width / 2, i * door_width + door_width / 2], [0, height], color="black",
                    linewidth=3)

        # Горизонтальные деления дверей, если горизонтальные секции больше 0
        if impost_h > 0:
            section_height = height / impost_h
            for j in range(1, impost_h):
                ax.plot([i * door_width, (i + 1) * door_width], [j * section_height, j * section_height], color="black",
                        linewidth=3)

    # Убираем оси
    ax.set_xticks([])
    ax.set_yticks([])

    # Добавляем размеры на чертеже
    # Ширина под перегородкой
    ax.text(width/2,height+0.5, f"{shirina} мм", ha='center', fontsize=14)  # Перенесли ширину под чертеж
    # Высота справа от перегородки
    ax.text(width + 0.4, height / 2, f"{visota} мм", va='center', rotation=90, fontsize=14)

    # Настройки отображения
    ax.set_xlim([-0.1, width + 0.25])
    ax.set_ylim([-0.3, height + 0.1])
    ax.set_aspect('equal')

    plt.gca().invert_yaxis()  # Инвертируем ось Y для удобного отображения
    plt.show()

# Окно для ввода данных с помощью Tkinter
def get_user_input():
    root = tk.Tk()
    root.withdraw()

    draw_partition(shirina, visota, door, impost_v,impost_h+1)

# Запуск программы
get_user_input()