import pandas as pd

d = {'Name': ['Arsenal', 'Liverpool', 'Chelsea', 'Man.City', 'Tottenham'],
     'Score': [66, 89, 71, 90, 68],
     'Win': [21, 27, 20, 28, 21],
     'Defeat': [13, 2, 6, 3, 11]}
df = pd.DataFrame(d)
df.to_excel('C:/Users/karen/desktop/states.xlsx', sheet_name='States', index=False)

ashxatavardz1 = pd.DataFrame({'Names': ['Julia', 'Stephen', 'Camilla', 'Tom'],
                              'Salary': [1000000, 100000, 70000, 60000]})

ashxatavardz2 = pd.DataFrame({'Names': ['Pete', 'April', 'Marty'],
                              'Salary': [120000, 110000, 50000]})

ashxatavardz3 = pd.DataFrame({'Names': ['Victor', 'Victoria', 'Jennifer'],
                              'Salary': [75000, 90000, 40000]})

ashxatavardzi_list = {'Xumb1': ashxatavardz1, 'Xumb2': ashxatavardz2, 'Xumb3': ashxatavardz3}
writer = pd.ExcelWriter('C:/Users/karen/desktop/income.xlsx', engine='xlsxwriter')

for eji_anun in ashxatavardzi_list.keys():
    ashxatavardzi_list[eji_anun].to_excel(writer, sheet_name=eji_anun, index=False)

writer.save()
