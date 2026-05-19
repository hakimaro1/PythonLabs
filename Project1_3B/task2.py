# Задание 2. Списки имён (A–M и остальные)

import names

all_names = [names.get_full_name() for _ in range(100)]

names_a_to_m = []
names_other = []

for name in all_names:
    first_letter = name[0].upper()
    if "A" <= first_letter <= "M":
        names_a_to_m.append(name)
    else:
        names_other.append(name)

print("Всего имён:", len(all_names))
print("Имена (A–M):", len(names_a_to_m))
print("Остальные имена:", len(names_other))
print()
print("Пример (A–M):", names_a_to_m[:5])
print("Пример (остальные):", names_other[:5])
