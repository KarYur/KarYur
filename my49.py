artikul = []
artikul_pictures = []
for i, j in dic.items():
    artikul.append(i)
    artikul_pictures.append(j)
    print(artikul)
    print(artikul_pictures)


k = 0
os.chdir(r"C:\\Users\\karen\\Desktop\\")
file = pd.read_excel(r"C:\\Users\\karen\\Desktop\\для.xlsx")
for i in file['для']:
    s = ''
    if i.count('для рак'):
        print('для раковины')
    if i.count('для кухни'):
        print('для кухни')
    if i.count('для ванны'):
        print('для ванны')
    if i.count('для душа'):
        print('для душа')
    if i.count('для биде'):
        print('для биде')
    if i.count('Душевая система'):
        print('Душевая система')
    if i.count('для чаши'):
        print('для чаши')
    if i.count('на борт ванны'):
        print('на борт ванны')
    if i.count('приставка на унитаз'):
        print('приставка на унитаз')
    if i.count('борт раков'):
        print('борт раковины')
    if i.count('Душевой релинг'):
        print('Душевой релинг')
    if i.count('Комплект скрыт'):
        print('комплект скрытого монтажа')
    if i.count('Кронштейн для ТРОП'):
        print('для тропического душа')
    if i.count('Комплект скрыт'):
        print('комплект скрытого монтажа')
    k += 1
    print(end=' ')
    print(k)