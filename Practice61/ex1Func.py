a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = float(input("Введите третье число: "))

maximum = max(a, b, c)
print(f"Максимальное число: {maximum}")

minimum = min(a, b, c)
print(f"Минимальное число: {minimum}")

total = sum([a, b, c])
print(f"Сумма чисел: {total}")

rounded_sum = round(total, 2)
print(f"Округлённая сумма (до 2 знаков): {rounded_sum}")

