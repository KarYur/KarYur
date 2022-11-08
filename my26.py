import csv


#with open('C:\\Users\\karen\\Downloads\\test_data.csv','r', encoding='utf-8') as f:
#    row = f.read().split(',')

#for i in row:
#    print(i)
manager_text, desired_text = [],[]
with open('C:\\Users\\karen\\Downloads\\test_data.csv','r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        if 'manager' in row:
            manager_text += row
            for i in row:
                if 'здравствуйте' in i:
                    desired_text += [row]
                if 'добрый день' in i:
                    desired_text += [row]
                if 'Добрый день' in i:
                    desired_text += [row]
                if 'зовут' in i:
                    desired_text += [row]
                if 'Да это' in i:
                    desired_text += [row]


print(manager_text)
print(desired_text)