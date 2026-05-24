filename = input()

with open(filename, 'r', encoding='utf-8') as fp:
    content = fp.read()

letters = sum(map(str.isalpha, content))
words = len(content.split())
lines = content.count('\n')

print('Input file contains:')
print(f'{letters} letters')
print(f'{words} words')
print(f'{lines} lines')
