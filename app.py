from flask import Flask, render_template, request, send_file
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import io

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('form.html')


@app.route('/calculate', methods=['POST'])
def calculate():
    # Получаем параметры из формы
    shirina = float(request.form['shirina'])
    visota = float(request.form['visota'])
    door = int(request.form['door'])
    impost_v = int(request.form['impost_v'])
    impost_h = int(request.form['impost_h'])
    steklo = int(request.form['steklo'])
    type_steklo = int(request.form['type_steklo'])
    montaj = int(request.form['montaj'])
    dostavka = int(request.form['dostavka'])

    # Цены на материалы
    profile30x32 = 1837
    profile57x15 = 1580
    profile22 = 1050
    trek_cena = 580
    uplotnitel = 40
    rasxodniki = 500
    pokraska = 5000
    steklo_prices = {
        (4, 0): 660,
        (4, 1): 1410,
        (6, 0): 900,
        (6, 1): 1605,
        (8, 0): 1545,
        (8, 1): 2540,
    }

    # Расчет профилей
    # Здесь ваш код расчета профилей, включая себестоимость и др.

    # Визуализация чертежа
    img = draw_partition(shirina, visota, door, impost_v, impost_h)

    # Сохраняем изображение в памяти и отправляем его
    img_io = io.BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)

    return render_template('results.html',
                           results=results,
                           image_data=img_io.getvalue())


def draw_partition(shirina, visota, door, impost_v, impost_h):
    width = shirina / 1000
    height = visota / 1000
    fig, ax = plt.subplots()

    ax.add_patch(Rectangle((0, 0), width, height, fill=False, edgecolor="black", linewidth=5))

    door_width = width / door
    for i in range(door):
        ax.add_patch(
            Rectangle((i * door_width, 0), door_width, height, fill=True, facecolor="lightblue", edgecolor="black",
                      linewidth=5))

        if impost_v:
            ax.plot([i * door_width + door_width / 2, i * door_width + door_width / 2], [0, height], color="black",
                    linewidth=3)

        if impost_h > 0:
            section_height = height / impost_h
            for j in range(1, impost_h):
                ax.plot([i * door_width, (i + 1) * door_width], [j * section_height, j * section_height], color="black",
                        linewidth=3)

    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlim([-0.1, width + 0.25])
    ax.set_ylim([-0.3, height + 0.1])
    ax.set_aspect('equal')
    plt.gca().invert_yaxis()

    plt.close(fig)  # Закрыть фигуру, чтобы избежать отображения в GUI
    return fig


if __name__ == '__main__':
    app.run(debug=True)
