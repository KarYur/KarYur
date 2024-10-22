from flask import Flask, request, send_file, render_template, redirect, url_for, flash
from PIL import Image, ImageDraw, ImageFont
import io
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Необходимо для flash-сообщений


# Главная страница
@app.route('/')
def home():
    return render_template('form.html')


# Валидация пользовательского ввода
def validate_input(data):
    try:
        shirina = float(data['shirina'])
        visota = float(data['visota'])
        door = int(data['door'])
        trek = int(data['trek'])
        impost_v = int(data['impost_v'])
        impost_h = int(data['impost_h'])
        steklo = int(data['steklo'])
        type_steklo = int(data['type_steklo'])
        montaj = int(data['montaj'])
        dostavka = int(data['dostavka'])
        return (shirina, visota, door, trek, impost_v, impost_h, steklo, type_steklo, montaj, dostavka)
    except ValueError:
        return None


# Расчет стоимости проекта
def calculate_cost(shirina, visota, door, impost_v, impost_h, steklo, type_steklo, montaj, dostavka):
    profile57x15 = 1580
    profile30x32 = 1837
    profile22 = 1050
    krishka = 840
    trek_cena = 580
    karetok = 1500
    uplotnitel = 40
    pokraska = 5000
    bolti = 60
    rasxodniki = 500
    steklo_4mm = 660
    zak_steklo_4mm = 1410
    steklo_6mm = 900
    zak_steklo_6mm = 1605
    steklo_8mm = 1545
    zak_steklo_8mm = 2540

    # Подсчет профилей и стекол
    vertical_profile_cost = door * profile30x32
    horizontal_profile_cost = door * profile57x15
    impost_vertical_cost = impost_v * profile22
    impost_horizontal_cost = impost_h * profile22

    # Расчет стоимости стекла
    area = shirina * visota / 1_000_000  # Площадь в квадратных метрах
    if steklo == 4:
        steklo_cost = zak_steklo_4mm * area if type_steklo else steklo_4mm * area
    elif steklo == 6:
        steklo_cost = zak_steklo_6mm * area if type_steklo else steklo_6mm * area
    else:
        steklo_cost = zak_steklo_8mm * area if type_steklo else steklo_8mm * area

    # Итоговая стоимость
    total_cost = (
            vertical_profile_cost + horizontal_profile_cost + impost_vertical_cost + impost_horizontal_cost +
            steklo_cost + montaj + dostavka + pokraska + bolti * door + karetok * door
    )

    return total_cost


# Визуализация перегородки
def draw_partition(shirina, visota, door, impost_v, impost_h):
    width = shirina / 1000  # в метрах
    height = visota / 1000  # в метрах

    fig, ax = plt.subplots()

    # Общая рамка перегородки
    ax.add_patch(Rectangle((0, 0), width, height, fill=False, edgecolor="black", linewidth=5))

    # Деление на двери
    door_width = width / door
    for i in range(door):
        # Рисуем каждую дверь
        ax.add_patch(
            Rectangle((i * door_width, 0), door_width, height, fill=True, facecolor="lightblue", edgecolor="black",
                      linewidth=5))

        # Вертикальные импосты
        if impost_v:
            ax.plot([i * door_width + door_width / 2, i * door_width + door_width / 2], [0, height], color="black",
                    linewidth=3)

        # Горизонтальные импосты
        if impost_h > 0:
            section_height = height / impost_h
            for j in range(1, impost_h):
                ax.plot([i * door_width, (i + 1) * door_width], [j * section_height, j * section_height], color="black",
                        linewidth=3)

    # Убираем оси
    ax.set_xticks([])
    ax.set_yticks([])

    # Добавляем размеры
    ax.text(width / 2, height + 0.05, f"{shirina} мм", ha='center', fontsize=14)
    ax.text(width + 0.05, height / 2, f"{visota} мм", va='center', rotation=90, fontsize=14)

    # Настройки отображения
    ax.set_xlim([-0.1, width + 0.2])
    ax.set_ylim([-0.1, height + 0.1])
    ax.set_aspect('equal')
    plt.gca().invert_yaxis()

    # Сохраняем изображение в буфер
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    return buf


# Обработка формы и расчет
@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.form
    valid_data = validate_input(data)

    if valid_data is None:
        flash("Ошибка: неверные данные, пожалуйста, проверьте ввод.")
        return redirect(url_for('home'))

    shirina, visota, door, trek, impost_v, impost_h, steklo, type_steklo, montaj, dostavka = valid_data
    total_cost = calculate_cost(shirina, visota, door, impost_v, impost_h, steklo, type_steklo, montaj, dostavka)

    # Генерация изображения перегородки
    img_buf = draw_partition(shirina, visota, door, impost_v, impost_h)

    # Сохраняем изображение в файл
    img_path = 'static/partition.png'
    with open(img_path, 'wb') as f:
        f.write(img_buf.read())

    # Возврат результата пользователю
    return render_template('form.html', total_cost=total_cost, img_path=img_path)


if __name__ == '__main__':
    app.run(debug=True)
