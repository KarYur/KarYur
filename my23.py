fib = lambda x: 1 if x <= 2 else fib(x - 1) + fib(x - 2)
print(fib(31))

x = [1, 2, 3]
y = x
y.append(4)

s = "123"
t = s
t = t + "4"

print(str(x) + " " + s)


def list_sum(lst):
    result = 0
    for element in lst:
        result += element
    return result


def sum(a, b):
    return a + b

y = sum(14,29)
z = list_sum([1, 2, 3])
print(y)
print(z)

