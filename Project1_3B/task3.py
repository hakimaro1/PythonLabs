# Задание 3. Акростих

words = []

print("Вводите слова по одному. Пустая строка — конец ввода.")

while True:
    word = input("Слово: ")
    if word == "":
        break
    words.append(word)

acrostic = ""
for word in words:
    acrostic += word[0]

print("Акростих:", acrostic)
