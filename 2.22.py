if __name__ == "__main__":
    string = input("Введите строку из которой нужно удалить + перед цифрой: ")
    for i in range(10):
        string = string.replace(f'+{i}', f'{i}')
    print('Преобразованная строка:', string)

