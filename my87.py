
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
t_steklo = int(input())
print('если закаленное стекло введите 1, если сырое стекло 0')
type_steklo = int(input())

print('\n\n//////////////Steklo/////////////\n//////////////interior///////////\n\n')

#Цена
profile57 = 1580
profile30 = 1837
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
montaj = 2000
sborka = 5000
zamer = 3500
podyom = 5000
dostavka = 5000

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

#импост вертикальный
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
    print(f'Вертикальный импост профиль {0} шт., из них {0} остатки')
else:
    print(f'Вертикальный импост профиль {k_i} шт., из них {ostatki_I} остатки')

#импост горизонтальный
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


#Всякое
krishki = 2* shirina
print(f'Крышки 2 шт, каждый по {shirina} мм')
treks = trek * shirina
print(f'Треков {trek} шт, каждый по {shirina} мм')


# Стекло
s = visota*shirina/1000000
print(f'общая квадратура стекла {s} м.кв.')

def steklo(t_steklo, type_steklo):
    global s,steklo_6mm, steklo_4mm, steklo_8mm, zak_steklo_6mm, zak_steklo_4mm, zak_steklo_8mm
    if t_steklo == 4:
        if type_steklo == 1:
            cena_s = zak_steklo_4mm * s
        if type_steklo == 0:
            cena_s = steklo_4mm * s
    if t_steklo == 6:
        if type_steklo == 1:
            cena_s = zak_steklo_6mm*s
        if type_steklo == 0:
            cena_s = steklo_6mm*s
    if t_steklo == 8:
        if type_steklo == 1:
            cena_s = zak_steklo_8mm*s
        if type_steklo == 0:
            cena_s = steklo_8mm*s
    return cena_s
#print(f'1.Стоимость стекла: {steklo(t_steklo, type_steklo)} руб.')
cena_s = steklo(t_steklo,type_steklo)

uplatnitel_4, uplatnitel_6, uplatnitel_8 = 0, 0, 0
if t_steklo == 4:
    uplatnitel_4 = (door * (2 * (visota + (shirina/ door))) + (2 * door * impost_v * visota) + (2 * impost_h * shirina))/1000
    print(f'2.Уплотнитель 4 мм {uplatnitel_4} м.п.')
if t_steklo == 6:
    uplatnitel_6 = (door * (2 * (visota + (shirina/ door))) + (2 * door * impost_v * visota) + (2 * impost_h * shirina))/1000
    print(f'2.Уплотнитель 6 мм {uplatnitel_6} м.п.')
if t_steklo == 8:
    uplatnitel_8 = (door * (2 * (visota + (shirina/ door))) + (2 * door * impost_v * visota) + (2 * impost_h * shirina))/1000
    print(f'2.Уплотнитель 8 мм {uplatnitel_8} м.п.')
cena_shotochni_ulpotnitel = uplotnitel_shyotochni * door * 2 * visota

sebes1 = ((k*profile30) + (k_h*profile57) + (k_i*profile22) + (krishki*krishka) + (treks*trek))/1000
sebes2 = ((uplatnitel_4*uplotnitel) + (uplatnitel_6*uplotnitel) + (uplatnitel_8*uplotnitel) + (uplotnitel_shyotochni*door*2*visota) + cena_shotochni_ulpotnitel)/1000
sebes3 = (bolti*door*2) + (door*karetok) + pokraska + ruchki + cena_s + (montaj*shirina*visota/1000000) + sborka + zamer + dostavka + podyom
print(sebes1, sebes2, sebes3)
print(sebes1+sebes2+sebes3)


