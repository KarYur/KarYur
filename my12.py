import numpy as np

a = np.array([1, 2, 3, 4])
print(a)
a = np.array([(1, 2, 3), (4, 5, 6)])
print(a)
print(a.ndim)  # tox
print(a.shape)  # syun
print(a.size)  # el.qanak
z = np.zeros((3, 2))  # 0-akan 3 toxov 2 syamb masiv(matrica)
print(z)
a = np.arange(1, 10)  # [1 2 3 4 5 6 7 8 9]
a = np.arange(1, 10, 2)  # [1 3 5 7 9]
print(a)
a = np.linspace(1, 2, 5)  # [1.   1.25 1.5  1.75 2.  ]
print(a)
a = np.arange(1, 11).reshape(2, 5)  # [[ 1  2  3  4  5] [ 6  7  8  9 10]]
a = np.arange(12).reshape(3, 4)  # [[ 0  1  2  3] [ 4  5  6  7] [ 8  9 10 11]]
print(a)
a = np.array([1, 2, 3])
b = np.linspace(0, 9, 3)
print(a, b, a + b)  # [1 2 3] [0.  4.5 9. ] [ 1.   6.5 12. ]

import pylab

x = pylab.linspace(1, 10, 4)
y = x ** 2
pylab.figure()
pylab.plot(x, y, 'g')
pylab.xlabel('x')
pylab.ylabel('y')
pylab.title('parabola')
pylab.show()

fig = pylab.plt.figure()
axes = fig.add_axes([0.8, 0.8, 0.1, 0.1])  # grafike tanuma dzax,verev,
axes.plot(x, y, 'r')  # laynacnuma aj u laynacnuma verv,tvere tokosov,
axes.set_xlabel('x')  # 0.8 orinak 80% na amboxj bacvox akoshki
axes.set_ylabel('y')
axes.set_title('title')
pylab.show()

fig = pylab.plt.figure()
axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])  # main axes
axes2 = fig.add_axes([0.2, 0.5, 0.25, 0.3])  # insert axes
# main axes
axes1.plot(x, y, 'b')
axes1.set_xlabel('x')
axes1.set_ylabel('y')
axes1.set_title('title')
# insert axes
axes2.plot(y, x, 'g')
axes2.set_xlabel('x')
axes2.set_ylabel('y')
axes2.set_title('insert title')
pylab.show()

# 2 arandznacvac grafikner
fig, axes = pylab.plt.subplots(nrows=1, ncols=2)

for ax in axes:
    ax.plot(x, y, 'r')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('title')

fig.tight_layout()
pylab.show()
