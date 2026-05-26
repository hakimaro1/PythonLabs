def gcd(a, b):
   #НОД
    a, b = abs(a), abs(b)  # Работаем с модулями чисел
    while b != 0:
        a, b = b, a % b
    return a


def max_of_three(a, b, c):
   #Наибольшее из трех чисел
    maximum = a
    if b > maximum:
        maximum = b
    if c > maximum:
        maximum = c
    return maximum


def is_leap_year(year):
    #Високосный год
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


def main():
    print("Выберите задачу:")
    print("1 — Наибольший общий делитель")
    print("2 — Наибольшее из трёх чисел")
    print("3 — Проверка високосного года")

    choice = input("Введите номер задачи (1-3): ")

    if choice == '1':
        num1 = int(input("Введите первое число: "))
        num2 = int(input("Введите второе число: "))
        result = gcd(num1, num2)
        print(f"НОД({num1}, {num2}) = {result}")

        # Дополнительная задача: используем НОД для упрощения дроби
        if result != 0:
            simplified_num1 = num1 // result
            simplified_num2 = num2 // result
            print(f"Упрощённая дробь: {simplified_num1}/{simplified_num2}")

    elif choice == '2':
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        num3 = float(input("Введите третье число: "))
        result = max_of_three(num1, num2, num3)
        print(f"Наибольшее число: {result}")

        # Дополнительная задача: используем результат для сравнения
        if result > 100:
            print("Число больше 100 — это большое число!")
        else:
            print("Число меньше или равно 100")

    elif choice == '3':
        year = int(input("Введите год: "))
        result = is_leap_year(year)
        if result:
            print(f"{year} год — високосный")
        else:
            print(f"{year} год — не високосный")

        # Дополнительная задача: считаем дни в году
        days = 366 if result else 365
        print(f"В {year} году {days} дней")
    else:
        print("Неверный выбор!")


# Запуск программы
main()
