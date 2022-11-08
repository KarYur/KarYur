def sqr(x):
    if x == 0:
        return 0
    if x == 1:
        return 1
    else:

        return sqr(x ** (1/2))


print(sqr(25))
