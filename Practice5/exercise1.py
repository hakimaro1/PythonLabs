# Упражнение 1. Использование списков

fruits = ['Apple', 'Grape', 'Peach', 'Banan', 'Orange']

print(fruits[0])  # нумерация начинается с нуля
print(fruits[1])
print(fruits[4])
print(fruits[-1])  # последний элемент — индексирование в обратную сторону

fruits[0] = 'Watermelon'
fruits[3] = 'Lemon'

fruits.append('Banan')

if 'Apple' in fruits:
    print('В списке есть элемент Apple')
else:
    print('В списке нет элемента Apple')

print(fruits)

# Apple отсутствует, потому что fruits[0] был заменён на 'Watermelon'
