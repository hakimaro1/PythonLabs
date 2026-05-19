# Контрольное задание (к упр. 4):  расход ресурса цикл for
from random import randint

total = 100
for i in range(5):
    n = randint(1, 50)
    total = total - n
    if total < 0:
        total = 0
        break
else:
    print("Процесс выполнен полностью")
print("Осталось", total)
