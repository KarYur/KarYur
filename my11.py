import pylab

x = pylab.linspace(0, 5, 10)
y = x ** 2
print(x)
print(y)
pylab.figure()
pylab.plot(x, y, 'r')
pylab.xlabel('x')
pylab.ylabel('y')
pylab.title('title')
pylab.show()

x = pylab.arange(1,11)
y = x ** 2
pylab.figure()
pylab.plot(x,y,'g')
pylab.xlabel('x')
pylab.ylabel('y')
pylab.title('title')
pylab.show()

