import matplotlib.pyplot as plt

# x = [1, 2, 3, 4, 5]
# y = [25, 32, 34, 20, 25]
# plt.plot(x, y)
# plt.xlabel('Ось х') #Подпись для оси х
# plt.ylabel('Ось y') #Подпись для оси y
# plt.title('Первый график') #Название
# plt.show()


# x = [1, 2, 3, 4, 5]
# y = [25, 32, 34, 20, 25]
# plt.plot(x, y, color='green', marker='o', markersize=7)
# plt.xlabel('Ось х') #Подпись для оси х
# plt.ylabel('Ось y') #Подпись для оси y
# plt.title('Первый график') #Название
# plt.show()

# x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# y = [25, 32, 34, 20, 25, 23, 21, 33, 19, 28]
# plt.scatter(x, y)
# plt.show()

x = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май']
y = [2, 4, 3, 1, 7]

plt.bar(x, y, label='Величина прибыли') #Параметр label позволяет задать название величины для легенды
plt.xlabel('Месяц года')
plt.ylabel('Прибыль, в млн руб.')
plt.title('Пример столбчатой диаграммы')
plt.legend()
plt.show()