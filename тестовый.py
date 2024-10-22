import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk, ImageDraw


# Функция для расчетов и отрисовки перегородки
def calculate_and_draw():
    # Вводим все значения из полей
    width = int(width_entry.get())
    height = int(height_entry.get())
    doors = int(doors_entry.get())
    tracks = int(tracks_entry.get())
    vert_imposts = int(vertical_imposts_entry.get())
    hor_imposts = int(horizontal_imposts_entry.get())
    glass_thickness = int(glass_thickness_entry.get())
    glass_type = glass_type_entry.get()
    install_cost = float(install_cost_entry.get())
    delivery_cost = float(delivery_cost_entry.get())

    # Пример расчета: (можно заменить на ваш расчет из предоставленного кода)
    material_cost = (width * height / 1000000) * 3000  # условный расчет стоимости материалов
    total_cost = material_cost + install_cost + delivery_cost

    # Отображение результата
    result_label.config(text=f"Итоговый стоимость: {total_cost:.2f} РУБ.")

    # Отрисовка перегородки
    partition_image = Image.new('RGB', (400, 400), color='white')
    draw = ImageDraw.Draw(partition_image)

    # Пример упрощенной схемы перегородки (рисование квадратов для дверей)
    door_width = width // doors
    for i in range(doors):
        draw.rectangle([(i * door_width, 0), ((i + 1) * door_width, height)], outline="black", width=3)

    # Отображение чертежа в интерфейсе
    img = ImageTk.PhotoImage(partition_image)
    drawing_label.config(image=img)
    drawing_label.image = img


# Создание главного окна
root = tk.Tk()
root.title("Расчётчик раздвижных перегородок")
root.geometry("600x700")

# Поля для ввода данных
tk.Label(root, text="Ширина (мм):").grid(row=0, column=0, padx=10, pady=5)
width_entry = tk.Entry(root)
width_entry.grid(row=0, column=1)

tk.Label(root, text="Высота (мм):").grid(row=1, column=0, padx=10, pady=5)
height_entry = tk.Entry(root)
height_entry.grid(row=1, column=1)

tk.Label(root, text="количество двери (шт.):").grid(row=2, column=0, padx=10, pady=5)
doors_entry = tk.Entry(root)
doors_entry.grid(row=2, column=1)

tk.Label(root, text="количество трэков (шт.):").grid(row=3, column=0, padx=10, pady=5)
tracks_entry = tk.Entry(root)
tracks_entry.grid(row=3, column=1)

tk.Label(root, text="Вертикальное деление:").grid(row=4, column=0, padx=10, pady=5)
vertical_imposts_entry = tk.Entry(root)
vertical_imposts_entry.grid(row=4, column=1)

tk.Label(root, text="Горизонтальное деление:").grid(row=5, column=0, padx=10, pady=5)
horizontal_imposts_entry = tk.Entry(root)
horizontal_imposts_entry.grid(row=5, column=1)

tk.Label(root, text="Толщина стекла (мм):").grid(row=6, column=0, padx=10, pady=5)
glass_thickness_entry = ttk.Combobox(root, values=['4', '6', '8'])
glass_thickness_entry.grid(row=6, column=1)

tk.Label(root, text="тип стекла:").grid(row=7, column=0, padx=10, pady=5)
glass_type_entry = ttk.Combobox(root, values=["Сырое", "Закаленное"])
glass_type_entry.grid(row=7, column=1)

tk.Label(root, text="Сумма монтажа (Руб./м²):").grid(row=8, column=0, padx=10, pady=5)
install_cost_entry = tk.Entry(root)
install_cost_entry.grid(row=8, column=1)

tk.Label(root, text="Сумма доставки (Руб.):").grid(row=9, column=0, padx=10, pady=5)
delivery_cost_entry = tk.Entry(root)
delivery_cost_entry.grid(row=9, column=1)

# Кнопка для расчета и отображения чертежа
calculate_button = tk.Button(root, text="Calculate", command=calculate_and_draw)
calculate_button.grid(row=10, column=0, columnspan=2, pady=20)

# Поле для вывода итоговой стоимости
result_label = tk.Label(root, text="Себестоимость: ")
result_label.grid(row=11, column=0, columnspan=2)

# Поле для отображения чертежа
drawing_label = tk.Label(root)
drawing_label.grid(row=12, column=0, columnspan=2)

# Запуск интерфейса
root.mainloop()
