# Раздвижная перегородка
print("Введите ширину перегородки (мм): ")
shirina = float(input())
print("Введите высоту перегородки (мм): ")
visota = float(input())
print("количество дверей (шт.): ")
door = int(input())
print('Введите количество вертикальных импостов:')
impost_v = int(input())
print('Введите количество горизонтальных импостов:')
impost_h = int(input())
profile_v = 5400
profile_h = 6000
profile_impost = 6000

print('введите толщину стекла 4 или 6 (мм):')
t_steklo = int(input())
print('если закаленное стекло введите 1, если сырое стекло 0')
type_steklo = int(input())

# mnacord = profile_v % visota
# qanak = profile_v // visota
# print(qanak, mnacord)

# импост вертикальный
j_i, n_i, w_i, k_i, e_i, ostatki_I = 0, 0, 0, 1, 0, []
r_i = True
while r_i == True:
    if w_i < ((door * impost_v) / 2):
        e_i += 1
        j_i += visota
        if j_i > 6000:
            k_i += 1
            ostatki_I.append(6000 - (j_i - visota))
            j_i = visota
        n_i += 1
        if n_i == 2:
            w_i += 1
            n_i = 0
    else:
        ostatki_I.append(6000 - j_i)
        r_i = False
print(f'Вертикальный импост профиль {k_i} шт., из них {ostatki_I} остатки')

# импост горизонтальный
c = True
z = shirina / door
x = door * impost_h
for i in ostatki_I:
    while i >= z:
        i -= z

        x -= 1

j_ih, n_ih, w_ih, k_ih, e_ih, ostatki_iH = 0, 0, 0, 1, 0, []
r_ih = True
while r_ih == True:
    if w_ih < x:
        e_ih += 1
        j_ih += shirina / door
        if j_ih > 6000:
            k_ih += 1
            ostatki_iH.append(6000 - (j_ih - shirina / door))
            j_ih = shirina / door
        n_ih += 1
        if n_ih == impost_h:
            w_ih += impost_h
            n_ih = 0
    else:
        ostatki_iH.append(6000 - j_ih)
        r_ih = False
print(f'Горизонтальный импост профиль {k_ih} шт., из них {ostatki_iH} остатки')




