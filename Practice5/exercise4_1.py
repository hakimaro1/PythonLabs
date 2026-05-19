# Упражнение 4.1 (контрольное). Объем продаж

sales = []

for day in range(7):
    value = float(input(f'Введите объем продаж за день {day + 1}: '))
    sales.append(value)

total = sum(sales)
print(f'Общий объем продаж за неделю: {total}')

for value in sorted(sales):
    print(value)
