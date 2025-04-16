import math


def func(number):
    array = []
    for i in range(1, number):
        for n in range(1, number // 2 + 1):
            for m in range(1, number // 2 + 1):
                if n**2 + m**2 == i and i not in array:
                    array.append(i)
    print(", ".join([str(i) for i in array]))
            
        
if __name__ == "__main__":
    while True:
        try:
            user_input = int(input("Введите натуральное число n: "))
            if user_input > 0:
                func(user_input)
            else:
                raise ValueError
        except ValueError:
            print("Вводите натуральное число")
