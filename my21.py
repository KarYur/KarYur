def funct(address):
    s = ''
    with open(address, 'r') as f:
        for i, row in enumerate(f, 1):
            s += str(i) + ' ' + str(row)
    with open(address, 'w') as f:
        f.write(s)

s = r'C:/Users/karen/Desktop/New1.txt'
funct(s)