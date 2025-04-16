def adding_spaces(user_string, need_user_len):
    words_arr = user_string.split()
    string = " |".join(words_arr)

    i = 0
    while len(string.replace("|", "")) != need_user_len:
        if string[i] == "|":
            string = string[:i] + " |" + string[i + 1:]
            i += 1
        i += 1
        if i >= len(string):
            i = 0

    return string.replace("|", "")


if __name__ == "__main__":
    while True:
        try:
            user_input = input("Введите строку: ")  # Lorem ipsum dolor sit amet, consectetur adipiscing elit
            need_len = int(input(f"Ведите желаемую длинну строки от {len(user_input)}: "))

            if need_len <= len(user_input):
                raise Exception("Желаемая длинна должна быть больше вводимой строки!")

            converted_string = adding_spaces(user_input, need_len)
            print("Преобразованная строка:\n", converted_string)
            print("Длинна преобразованной строки:", len(converted_string))
        except Exception as exc:
            print(exc)
