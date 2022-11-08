import numpy as np

s = [1,2,3,4,5,6]
print(s[1:4])
a = np.array([2, 3, 4])  # mi karg unecox tox(massiv)
print(a)
print(a.ndim)  # masivi karge (1d,2d,3d...)
print(a.shape)  # massivi chapse
b = np.array([(1.5, 2, 3), (4, 5, 6)])  # 2d massiv
print(b)
print(b.ndim)  # masivi karge (1d,2d,3d...)
print(b.shape)  # massivi chapse- (2, 3) 2 tox 3 syun
print(b.size)  # sax elementneri qanake (6 element)
z = np.zeros((3, 2))  # 0 andamnerov massiv 3 tox 2 syanmb
print(z)
w = np.arange(10, 30, 5)  # 10-ic 30, 5 qaylov arden massivi generaciaa
print(w)  # [10 15 20 25]
q = np.linspace(0, 2, 9)  # arangei nman uxaki amboxt tvernela meje
print(q)  # 0-ic 2 tvere 9 tverov [0.   0.25 0.5  0.75 1.   1.25 1.5  1.75 2.  ]
b = np.arange(12).reshape(4, 3)  # 1d sarquma 2d u 4tox 3 syun
print(b)  # [[ 0  1  2] [ 3  4  5] [ 6  7  8] [ 9 10 11]]
a = np.array([10, 20, 30])
b = np.arange(3)  # [0 1 2]
print(a + b)  # +-*/ ashxatuma elementnerov
print(a - b)
print(a ** 2)  # a^2 [100 400 900]
print(2 * np.sin(a))  # 2*sin(a)
print(a < 20)  # [ True False False]
