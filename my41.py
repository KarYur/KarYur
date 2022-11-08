import os
import pandas as pd

dic = {}
os.chdir(r"C:\\Users\\karen\\Desktop\\Hansen_14.10.2022.1.53\\")
file = pd.read_excel(r"C:\\Users\\karen\\Desktop\\обновление14.10.2022.xlsx")
for i in file['Артикул']:
    s = ''
    #print(i)
    for j in os.listdir(path="."):
        #print(i,j)
        if j.count(str(i)):
            s += '/' + str(j) + '; '
            #print(i,j)
    dic[i] = s
print(dic)
#print(os.listdir(path="."))
artikul = []
artikul_pictures = []
for i, j in dic.items():
    artikul.append(i)
    artikul_pictures.append(j)
df = pd.DataFrame(
    {'Артикул': [artikul[i] for i in range(len(artikul))], 'pictures': [artikul_pictures[i] for i in range(len(artikul_pictures))]})
print(df)
df.to_excel(r"C:\\Users\\karen\\Desktop\\обновление.xlsx")


