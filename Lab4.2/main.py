print("Введите предварительную сумму заказа: ")
Summ = float(input())
Tax = Summ * 13 / 100
print(f"Налог на сумму: {Tax:.2f}")
Tip = Summ * 10 / 100
print(f"Чаевые официанту: {Tip:.2f}")
print(f"Ощая сумма: {(Summ + Tax + Tip):.2f}")