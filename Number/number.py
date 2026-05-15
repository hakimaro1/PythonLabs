name = input("Введите фамилию и имя: ")
Name = name.title()
parts = Name.split()

if len(parts) != 2:
    print("Нужно ровно два слова: имя и фамилия.")
else:
    last_name_raw, first_name_raw = parts
    last_name = last_name_raw
    first_name = first_name_raw
##Если вывести без изменений в регистре
    login = last_name[:4] + first_name[0]

    print(f"{last_name} {first_name}: {login}")

##Если првести все к нижнему регистру
    login = (last_name[:4] + first_name[0]).lower()

    print(f"{last_name} {first_name}: {login}")

