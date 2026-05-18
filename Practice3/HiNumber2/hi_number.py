# Наибольшее из трёх чисел

a = float(input("Первое число: "))
b = float(input("Второе число: "))
c = float(input("Третье число: "))

if a >= b and a >= c:
    print("Наибольшее:", a)
elif b >= a and b >= c:
    print("Наибольшее:", b)
else:
    print("Наибольшее:", c)
