# Упражнение 4.2 (контрольное). Форматирование по уровню

import random

numbers = [random.randint(1, 100) for _ in range(10)]

threshold = int(input('Введите пороговое значение: '))

levels = []
for num in numbers:
    if num > threshold:
        levels.append('High')
    else:
        levels.append('Low')

print('Исходный список:', numbers)
print('Список уровней:', levels)
