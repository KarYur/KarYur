

print('Длина листа (мм): ')
d1 = float(input())
print('Высота листа (мм): ')
d2 = float(input())

print('Количество деталей: ')
n = int(input())

lis1, lis2 = [], []
for i in range(n):
    print('Длина ' f'{i+1}''ой детали (мм): ')
    lis1.append(float(input()))
    print('Высота ' f'{i+1}''ой детали (мм): ')
    lis2.append(float(input()))

print(lis1)
print(lis2)
s = d1*d2/1000000
print('Общая площадь листа: ',s)
list_s = []
for i in range(n):
    list_s.append(lis1[i] * lis2[i]/1000000)

print('общая площадь деталей: ',list_s)
s1 = 0
for i in range(n):
    s1 += list_s[i]
print(s-s1)


