import math


def func(num):
    composition = 1
    lst = num.split()
    lst = [int(i) for i in lst]
    for i in lst:
        composition *= i
    if composition == math.factorial(len(lst)):
        print("True")
    else:
        print("False")


if __name__ == "__main__":
    while True:
        try:
            user_input = input("Ведите элементы списка через пробел: ")
            func(user_input)
        except ValueError:
            print("Вводите числа!")


