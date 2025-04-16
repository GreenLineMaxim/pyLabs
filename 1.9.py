def func(num):
    fib1 = 0
    fib2 = 1
    chek_one = 0
    lst = []
    lst.append(fib1)
    lst.append(fib2)

    while chek_one < num:
        fib_next = fib1 + fib2
        fib1 = fib2
        fib2 = fib_next
        lst.append(fib_next)
        chek_one += 1

    for chek in lst:
        if num == chek:
            print(num,'Число фибоначчи')
            break
    else:
        print(num,'Не число фибоначчи')


if __name__ == "__main__" :
    while True:
        try:
            user_input = int(input('Введите проверяемое число: '))
            if user_input < 0:
                print('Ошибка, введите число больше 0!')
            else:
                func(user_input)
                break
        except ValueError:
            print('Ошибка, введите целое число!')



        
