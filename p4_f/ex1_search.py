import os

folder = r'C:\Users\sanya\Desktop\PythonLabs\p4_f\PythonPrim\Textfiles'
answ = set()
search = input("Введите поисковый запрос: ")

for filename in os.listdir(folder):
    filepath = os.path.join(folder, filename)
    with open(filepath, 'r', encoding='utf-8') as fp:
        for line in fp:
            if search in line:
                answ.add(filename)

print("\nФайлы, содержащие искомое слово:")
for i in answ:
    print(i)
