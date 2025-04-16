import math


def transform(text):
    array_numbers = []
    for i in text:
        num = int(i)
        if num % math.sqrt(num) == 0 and num % 2 == 0 and num % 3 == 0 and num % 7 != 0:
            array_numbers.append(str(num))
    return array_numbers


if __name__ == "__main__":
    with open("file_one.txt", "r") as file_f:
        txt = file_f.readline().split(",")

    array = transform(txt)

    with open("file_two.txt", "w") as file_g:
        file_g.write(" ".join(array))

