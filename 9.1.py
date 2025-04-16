"""
import turtle


length_hip = int(input("Введите длинну бедра: "))
length_base = int(input("Введите длинну основания: "))
degree = int(input("Введите угол при основании: "))



tur = turtle.Turtle()
tur.forward(length_base)
tur.left(degree)
tur.forward(length_hip)
tur.left(degree * -2)
tur.forward(length_hip)
turtle.done()
"""

from PIL import Image, ImageDraw


if __name__ == "__main__":
    while True:
        try:
           base_length = int(input("Введите длинну основания: "))
           height_length = int(input("Введите длинну высоты: "))
           img = Image.new("RGB", (1200, 1200))
           draw = ImageDraw.Draw(img)
           draw.polygon([(base_length + 150, height_length), (300, height_length + 400), (base_length + 300, height_length + 400)], fill='white')
           img.show()
        except ValueError:
            print("Вводите числа!")