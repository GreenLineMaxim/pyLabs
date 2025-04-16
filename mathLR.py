# max_row - максимальная длинна ряда
# row_num_n - число по заданной формуле
# number_e - заданное число e
def f(score, text):
    while True:
        try:
            if score == 0:
                num = int(input(text))
            else:
                num = float(input(text))
            if num > 0:
                break
            else:
                print("Введите значение больше 0")
        except ValueError:
            pass
    return num

if __name__ == "__main__":

    max_row = f(0, "Введите целое максимальное значение ряда для n: ")
    number_e = f(1, "Введите значение до которого будет вестись рассчет: ")

    sum_n = 0
    for k in range(1, max_row + 1):
        row_num_n = (5 * k) / (k ** 2 + 81)
        sum_n += row_num_n
    print("Cумма ряда", sum_n)

    k1 = 0
    E = 0
    while True:
        k1 += 1
        E = (5 * k1) / (k1 ** 2 + 81)
        if E >= number_e:
            print("Номер числа:", k1, " Число:", E)
        else:
            break


