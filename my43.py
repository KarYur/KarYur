def fun_x16(n):
    s = ''
    h = '0123456789ABCDEF'
    while n > 0:
        s = h[n % 16] + s
        n = n // 16
    return s
#data = [input() for i in range(N)]
#print(data)
#n = int(input())
#print(x16(n))

file = open('data.csv','r')
N = int(file.readline())
s = [0 for i in range(N)]
fio = [0 for i in range(N)]
fio_set = set()
b_data = []
birtday = [0 for i in range(N)]
t = []
for i in range(N):
    s[i] = file.readline().strip().split(',')
    fio[i] = s[i][0] + s[i][1] + s[i][2]
    birtday[i] = str(s[i][3]) + str(s[i][4])
    t.append(fio[i][0])
    w = 0
    for g in birtday[i]:
        w += int(g)
    b_data.append(w)
#print(s)
fio_str = []
#print(fio_split)
for i in range(len(s)):
    for j in fio[i]:
        fio_set.add(j)
    fio_str.append(len(fio_set))
    fio_set = set()
d = []
dic = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
for i in t:
    if i in dic.keys():
        d.append(dic[i])
#print(fio_str)
#print(b_data)
s1,s2,s3,s4 = [],[],'',[]
for i in range(len(s)):
    n = fio_str[i] + (b_data[i] * 64) + (d[i] * 256)
    #print(n)
    s1.append(fun_x16(n))
    #print(s1)
    for j in s1:
        for k in range(1,len(j)):
            s3 += j[k]
        s2 += [s3]
        s3 = ''
    s1 = []
#print(s2)
for i in s2:
    print(i,end=' ')