x = '123'
y = x
y = '4'

x = 1, 2, 3
y = x
x = 4

x = (1, 2, 3)
y = x
y = 5

x = [1, 2, 3]  # appendi kam (+=)i jamanak poxvuma obyekte erkusi hamarel
y = x
y.append(4)
y += [5]
y = [6]
y += [7]

print(id(x))
print(id(y))
print(x, y)

a = 1
b = 1
c = 1
a += 4
print(a,b,c)
