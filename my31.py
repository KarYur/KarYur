import pandas as pd

dict = {}
def color(i):
    dict[i] = 'хром'
    if i.count('X') != 0:
        dict[i] = 'хром'
    if i.count('R') != 0:
        dict[i] = 'синий'
    if i.count('D') != 0:
        dict[i] = 'бронзовый'
    if i.count('C') != 0:
        dict[i] = 'черный'
    if i.count('F') != 0:
        dict[i] = 'белый'
    if i.count('G') != 0:
        dict[i] = 'сатин'
    if i.count('A') != 0:
        dict[i] = 'бежевый'
    if i.count('P') != 0:
        dict[i] = 'серый'
    if i.count('E') != 0:
        dict[i] = 'золотистый'
    if i.count('S') != 0:
        dict[i] = 'красный'
    if i.count('T') != 0:
        dict[i] = 'зеленый'
    if i.count('M') != 0:
        dict[i] = 'бежевый'
    if i.count('CC') != 0:
        dict[i] = 'черный-черный'
    if i.count('GC') != 0:
        dict[i] = 'сатин-черный'
    if i.count('GP') != 0:
        dict[i] = 'сатин-серый'
    if i.count('FF') != 0:
        dict[i] = 'белый-белый'
    if i.count('GF') != 0:
        dict[i] = 'сатин-белый'

s = []
file = open(r'C:\\Users\\karen\\Downloads\\Hansen1.txt')
for i in file:
    i = i.strip()
    color(i)
file.close()
artikul = []
artikul_color = []
for i, j in dict.items():
    artikul.append(i)
    artikul_color.append(j)
df = pd.DataFrame(
    {'Name': [artikul[i] for i in range(len(artikul))], 'color': [artikul_color[i] for i in range(len(artikul))]})
print(df)
df.to_excel(r'C:\\Users\\karen\\Downloads\\Han.xlsx')
