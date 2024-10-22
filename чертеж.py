import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import tkinter as tk
from tkinter import simpledialog


def draw_partition(width_mm, height_mm, doors, horizontal_sections, vertical_split, material):
    width = width_mm / 1000  # переводим в метры для визуализации
    height = height_mm / 1000  # переводим в метры для визуализации

    # Определение цвета в зависимости от выбранного материала
    material_colors = {
        "Стекло": "lightblue",
        "ЛДСП": "lightgray",
        "Металл": "silver"
    }
    door_color = material_colors.get(material, "white")

    fig, ax = plt.subplots()

    # Общая рамка перегородки (периметр)
    ax.add_patch(Rectangle((0, 0), width, height, fill=False, edgecolor="black", linewidth=5))  # Толстая рамка

    # Деление на двери
    door_width = width / doors
    for i in range(doors):
        # Рисуем каждую дверь с выбранным материалом
        ax.add_patch(
            Rectangle((i * door_width, 0), door_width, height, fill=True, facecolor=door_color, edgecolor="black",
                      linewidth=5))

        # Если пользователь выбрал вертикальное деление дверей
        if vertical_split:
            ax.plot([i * door_width + door_width / 2, i * door_width + door_width / 2], [0, height], color="black",
                    linewidth=3)

        # Горизонтальные деления дверей, если горизонтальные секции больше 0
        if horizontal_sections > 0:
            section_height = height / horizontal_sections
            for j in range(1, horizontal_sections):
                ax.plot([i * door_width, (i + 1) * door_width], [j * section_height, j * section_height], color="black",
                        linewidth=3)

    # Убираем оси
    ax.set_xticks([])
    ax.set_yticks([])

    # Добавляем размеры на чертеже
    # Ширина под перегородкой
    ax.text(width / 2, -0.1, f"{width_mm} мм", ha='center', fontsize=14)  # Перенесли ширину под чертеж
    # Высота справа от перегородки
    ax.text(width + 0.15, height / 2, f"{height_mm} мм", va='center', rotation=270, fontsize=14)

    # Настройки отображения
    ax.set_xlim([-0.1, width + 0.25])
    ax.set_ylim([-0.3, height + 0.1])
    ax.set_aspect('equal')

    plt.gca().invert_yaxis()  # Инвертируем ось Y для удобного отображения
    plt.show()


# Окно для ввода данных с помощью Tkinter
def get_user_input():
    root = tk.Tk()
    root.withdraw()

    width_mm = simpledialog.askfloat("Ширина", "Введите ширину перегородки (в мм):", minvalue=1000, maxvalue=10000)
    height_mm = simpledialog.askfloat("Высота", "Введите высоту перегородки (в мм):", minvalue=2000, maxvalue=3500)
    doors = simpledialog.askinteger("Количество дверей", "Введите количество дверей:", minvalue=2, maxvalue=6)
    horizontal_sections = simpledialog.askinteger("Горизонтальные секции",
                                                  "Введите количество горизонтальных делений (0 для отсутствия):",
                                                  minvalue=0, maxvalue=6)

    vertical_split = simpledialog.askstring("Вертикальные деления",
                                            "Делить ли двери по вертикали на две части? (да/нет):").lower() == "да"

    material = simpledialog.askstring("Материал", "Введите материал (Стекло, ЛДСП, Металл):", initialvalue="Стекло")

    draw_partition(width_mm, height_mm, doors, horizontal_sections, vertical_split, material)


# Запуск программы
get_user_input()