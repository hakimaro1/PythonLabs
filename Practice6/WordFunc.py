def search_word_in_file(filename, word):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            count = content.lower().count(word.lower())
            return count > 0, count
    except FileNotFoundError:
        return False, 0


filename = input("Введите имя файла: ")
word = input("Введите слово для поиска: ")

found, count = search_word_in_file(filename, word)

if found:
    print(f"Слово '{word}' найдено. Количество вхождений: {count}")
else:
    print(f"Слово '{word}' не найдено")