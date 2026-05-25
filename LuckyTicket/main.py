number = input("Введите номер билета из 6 цифр: ")

#Вариант 1
if len(number) == 6:
    digits = list(map(int, number))  # Преобразуем строку в список цифр
    if sum(digits[:3]) == sum(digits[3:]):
        print("Счастливый билет!")
    else:
        print("Обычный билет")
else:
    print("Ошибка: номер должен содержать ровно 6 цифр")

#Вариант 2
# Проверяем, что введено ровно 6 символов
if len(number) != 6:
    print("Ошибка: номер должен содержать ровно 6 цифр")
else:
    # Преобразуем каждую цифру в число и суммируем половины
    first_half = int(number[0]) + int(number[1]) + int(number[2])
    second_half = int(number[3]) + int(number[4]) + int(number[5])

    # Сравниваем суммы и выводим результат
    if first_half == second_half:
        print("Счастливый билет!")
    else:
        print("Обычный билет")

