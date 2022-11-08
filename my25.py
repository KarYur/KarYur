x, y = input().split()
x = int(x)
y = int(y)
try:
    a = x / y
except ZeroDivisionError:
    a = 0
print(a)
