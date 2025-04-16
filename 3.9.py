def func(new_arr_one, new_arr_two):
    if sum(new_arr_one) == sum(new_arr_two):
        print(new_arr_one)
    else:
        print(sum((new_arr_two)))

if __name__ == "__main__":
    while True:
        try:
            arr_one = list(map(int, input("Введите элементы первого списка: ").split()))
            arr_two = list(map(int, input("Введите элементы второго списка: ").split()))
            func(arr_one, arr_two)
        except ValueError:
            print("Вводите числа")
