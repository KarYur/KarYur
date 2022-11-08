import pandas as pd
import matplotlib as mpl

cols = [0, 1]
database = pd.read_excel('C:\\Users\\karen\\Desktop\\tz_data.xlsx', usecols=cols)
print(database)
for i in database.head():
    print(i)
#cols = [0, 1, 3]
#database = pd.read_excel('C:\\Users\\karen\\Desktop\\tz_data.xlsx', usecols=cols)
#print(database.head(6))
