# Упражнение 4. Сумма цифр числа (цикл for)
num = input('Введите число для подсчета суммы цифр: ')
sumIt = 0
for it in num:
    sumIt += int(it)
print(f"Сумма цифр числа {num} равна {sumIt}")
