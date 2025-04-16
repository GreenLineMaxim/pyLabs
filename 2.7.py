def func(size, string):
    if size == len(string):
        print("Строка равна желаемой длинне")
    elif size < len(string):
        print("Желаемая длинна меньше входной строки, ошибка!")
    else:
        new_string = ''
        n = 2
        while len(new_string) != size:
            separator = " " * n
            new_string = separator.join(string.split())
            n += 1

    print(new_string)
    print("Итоговая длинна: ", len(new_string))


if __name__ == "__main__":
    while True:
        try:
            string = input("Введите строку: ")
            string_size = int(input("Введите желаемую длинну строки: "))
            func(string_size, string)
        except Exception:
             print("Ошибка")


