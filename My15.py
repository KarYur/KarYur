import os
import pandas as pd

r = os.listdir(path=".")
d = []
for i in range(len(r)):
    d += r[i].split('.')
print(len(r))
print(r)
print(d)

file_size = []
url = "C:/Users/karen/PycharmProjects/pythonProject1/files/"
for i in r:
    file_name = url + str(i)
    print(file_name)
    file_stats = os.stat(file_name)
    kb = float(file_stats.st_size / (1024 * 1024))
    print(kb)
    file_size += [kb]
print(file_size)

filename, fileformat = [], []
for i in range(0, len(d), 2):
    filename += [d[i]]
print(filename)
for i in range(1, len(d), 2):
    fileformat += [d[i]]
print(fileformat)
number = [i for i in range(1, len(r) + 1)]
s = []
for i in range(len(r)):
    s.append([number[i], filename[i], fileformat[i], file_size[i]])
print(s)

dic = {}
title = ['Number', 'name', 'format', 'size']
for i in range(len(title)):
    dic[title[i]] = [s[j][i] for j in range(len(r))]
print(dic)

df = pd.DataFrame(dic)

df.to_excel('./states.xlsx', index=False)
print(df)
df.to_csv('filename.csv', index=False)

df.to_csv('name.csv', sep=',')
print(df)
