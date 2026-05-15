print("Введите предварительную сумму заказа: ")
Summ = float(input())
Tax = Summ * 13 / 100
print(f"Налог на сумму: {Tax:.2f}")
Tip = Summ * 10 / 100
print(f"Чаевые официанту: {Tip:.2f}")
##Разные варианты форматирования
print(f"Общая сумма: {(Summ + Tax + Tip):.2f}")
print("Общая сумма: {:7.2f} ".format(Summ +Tax + Tip))

