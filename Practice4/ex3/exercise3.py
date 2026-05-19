# Упражнение 3. Расход ресурса (break, else)
from random import randint

total = 100  # запас ресурса
i = 0  # счетчик итераций цикла
while i < 5:
    n = randint(1, 50)  # имитация расхода ресурса
    total = total - n
    if total < 0:
        total = 0
        break
    else:
        print("Процесс выполнен полностью")
    i = i + 1
print("Осталось", total)
