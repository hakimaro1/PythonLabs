# Задание 1. Список случайных чисел и метки High / Low

import random

THRESHOLD = 50
COUNT = 20

numbers = [random.randint(1, 100) for _ in range(COUNT)]

labels = []
for value in numbers:
    if value > THRESHOLD:
        labels.append("High")
    else:
        labels.append("Low")

print("Пороговое значение:", THRESHOLD)
print("Числа:", numbers)
print("Метки:", labels)
