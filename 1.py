a = [1000,3500]
c = 834
b = []
clc = 0
for i in a:
    while i >= c:
        i -= c
        b.append(i)
        clc += 1
print(len(b))
print(clc)