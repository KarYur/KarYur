
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk, ImageDraw, ImageFont

def calculate_and_draw():
    shirina = int(width_entry.get())
    visota = int(height_entry.get())
    door = int(doors_entry.get())
    trek = int(tracks_entry.get())
    impost_v = int(vertical_imposts_entry.get())
    impost_h = int(horizontal_imposts_entry.get())
    steklo = int(glass_thickness_entry.get())
    type_steklo = glass_type_entry.get()
    montaj = int(install_cost_entry.get())
    dostavka = int(delivery_cost_entry.get())

    # Пример расчета:
    profile57x15 = 1580
    profile30x32 = 1837
    profile22 = 1050
    krishka = 840
    trek_cena = 580
    karetok = 1500
    uplotnitel = 40
    uplotnitel_shyotochni = 35
    pokraska = 5000
    bolti = 60
    rasxodniki = 500
    steklo_4mm = 660
    zak_steklo_4mm = 1410
    steklo_6mm = 900
    zak_steklo_6mm = 1605
    steklo_8mm = 1545
    zak_steklo_8mm = 2540
    zamer = 3500

    # Код для расчета и отображения итоговой стоимости и чертежа
    # Логика расчета остается прежней

root = tk.Tk()
root.title("Калькулятор себестоимости")

# Создаем фрейм для размещения виджетов
frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)

# Добавляем полосу прокрутки с левой стороны
scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL)
scrollbar.pack(side=tk.LEFT, fill=tk.Y)

# Привязываем полосу прокрутки к фрейму
canvas = tk.Canvas(frame, yscrollcommand=scrollbar.set)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar.config(command=canvas.yview)

# Создаем внутренний фрейм для виджетов внутри canvas
inner_frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=inner_frame, anchor='nw')

# Настройка для автоматического изменения размеров canvas
inner_frame.bind("<Configure>", lambda event: canvas.configure(scrollregion=canvas.bbox("all")))

# Добавление виджетов в inner_frame
tk.Label(inner_frame, text="Ширина (мм):").grid(row=0, column=0, padx=10, pady=5)
width_entry = tk.Entry(inner_frame)
width_entry.grid(row=0, column=1)

tk.Label(inner_frame, text="Высота (мм):").grid(row=1, column=0, padx=10, pady=5)
height_entry = tk.Entry(inner_frame)
height_entry.grid(row=1, column=1)

tk.Label(inner_frame, text="количество двери (шт.):").grid(row=2, column=0, padx=10, pady=5)
doors_entry = tk.Entry(inner_frame)
doors_entry.grid(row=2, column=1)

tk.Label(inner_frame, text="количество трэков (шт.):").grid(row=3, column=0, padx=10, pady=5)
tracks_entry = tk.Entry(inner_frame)
tracks_entry.grid(row=3, column=1)

tk.Label(inner_frame, text="Вертикальное деление:").grid(row=4, column=0, padx=10, pady=5)
vertical_imposts_entry = ttk.Combobox(inner_frame, values=[0, 1])
vertical_imposts_entry.grid(row=4, column=1)

tk.Label(inner_frame, text="Горизонтальное деление:").grid(row=5, column=0, padx=10, pady=5)
horizontal_imposts_entry = tk.Entry(inner_frame)
horizontal_imposts_entry.grid(row=5, column=1)

tk.Label(inner_frame, text="Толщина стекла (мм):").grid(row=6, column=0, padx=10, pady=5)
glass_thickness_entry = ttk.Combobox(inner_frame, values=['4', '6', '8'])
glass_thickness_entry.grid(row=6, column=1)

tk.Label(inner_frame, text="тип стекла:").grid(row=7, column=0, padx=10, pady=5)
glass_type_entry = ttk.Combobox(inner_frame, values=["Сырое", "Закаленное"])
glass_type_entry.grid(row=7, column=1)

tk.Label(inner_frame, text="Сумма монтажа (Руб./м²):").grid(row=8, column=0, padx=10, pady=5)
install_cost_entry = tk.Entry(inner_frame)
install_cost_entry.grid(row=8, column=1)

tk.Label(inner_frame, text="Сумма доставки (Руб.):").grid(row=9, column=0, padx=10, pady=5)
delivery_cost_entry = tk.Entry(inner_frame)
delivery_cost_entry.grid(row=9, column=1)

# Кнопка для расчета и отображения чертежа
calculate_button = tk.Button(inner_frame, text="РАССЧИТАТЬ", command=calculate_and_draw)
calculate_button.grid(row=10, column=0, columnspan=2, pady=20)

# Поле для вывода итоговой стоимости
result_label = tk.Label(inner_frame, text="Себестоимость: ")
result_label.grid(row=11, column=0, columnspan=2)

# Поле для отображения чертежа
drawing_label = tk.Label(inner_frame)
drawing_label.grid(row=12, column=0, columnspan=2)

# Запуск интерфейса
root.mainloop()
