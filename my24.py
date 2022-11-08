import math as m
import random as r



def generate1():
    a = r.uniform(0, 1)
    b = r.uniform(0, 1)
    return a * m.cos(2 * m.pi * b), a * m.sin(2 * m.pi * b)

def generate2():
    while True:
        x = r.uniform(-1, 1)
        y = r.uniform(-1, 1)
        if x ** 2 + y ** 2 > 1:
            continue
        return x, y
