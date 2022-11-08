q = []
with open(r'C://Users//karen//Desktop//121212.txt') as file:
    for i in file.readlines():
        q = i.replace('\n',';')
        w = q.replace('\t','; ')
        print(w)
