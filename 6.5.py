import re


def func(string):
    result = re.findall(r"[:;]?[-]*[()\[\]]+", string)
    print("Количество смайликов в введенной строке: ", len(result))


if __name__ == "__main__":
    while True:
        try:
            user_string = input("Введите строку: ")
            func(user_string)
        except Exception as exc:
            print("Ошибка", exc)