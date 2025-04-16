from PIL import Image, ImageDraw


def image(base, height):
    dynamic_expansion = 500
    coordinate_x = 300
    coordinate_y = 400
    img = Image.new("RGB", (max((base, height)) + dynamic_expansion, (max((base, height)) + dynamic_expansion)))
    draw = ImageDraw.Draw(img)
    draw.polygon([(base // 2 + coordinate_x, height), (coordinate_x, height + coordinate_y), (base + coordinate_x, height + coordinate_y)], fill = "white")
    img.show()


if __name__ == "__main__":
    while True:
        try:
            base_length = int(input("Ввидети длинну основания в пекселях: "))
            height_length = int(input("Ввидети длинну высоты в пекселях: "))    
            image(base_length, height_length)
        except ValueError:
            print("Вводите числа!")
       
