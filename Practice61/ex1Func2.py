import math

a = float(input("Введите число: "))

# Вычисление квадратного корня
y1 = math.sqrt(a)

# Округление до ближайшего целого вверх
y = math.ceil(y1)

print('sqrt(a) =', y1)
print('Округлённый результат =', y)

