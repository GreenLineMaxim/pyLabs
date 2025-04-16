# 1.17 Составить программу перевода чисел из непозиционной, например, римской системы счисления в десятичную.
rome_system = {
    "M": 1000,
    "MC": 900,
    "D": 500,
    "DC": 400,
    "C": 100,
    "XC": 90,
    "L": 50,
    "XL": 40,
    "X": 10,
    "IX": 9,
    "V": 5,
    "IV": 4,
    "I": 1,
}


def rome_to_dec(string, number_system):
    summ = 0

    for key in number_system:
        while string.startswith(key):
            summ += number_system[key]
            string = string[len(key):]
    
    return summ


if __name__ == "__main__":
    while True:
        try:
            user_input = input("Введите число, которое хотите перевести: ")

            for i in user_input:
                if i not in rome_system:
                    raise Exception("Введенное число не римское!")

            result = rome_to_dec(user_input, rome_system)
            print(result)
        except Exception as exc:
            print(exc)