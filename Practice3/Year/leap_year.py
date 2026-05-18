import datetime
import calendar

'''
Стандартный год состоит из 365 дней, а високосный из 366 дней.

Правила определения:
Високосный год кратен 4, но при этом не кратен 100, либо кратен 400.
Иными словами, если год делится на 4 без остатка, но делится на 100 только с остатком,
то он високосный, иначе — невисокосный, кроме случая, если он делится без остатка на 400 — тогда он всё равно високосный.
'''
current_date = datetime.date.today()
year = current_date.year  # проверяемая переменная

'''Задание 1. Проверка с условиями if-else'''
if year % 400 == 0:
    is_leap_1 = True
else:
    if year % 100 == 0:
        is_leap_1 = False
    else:
        if year % 4 == 0:
            is_leap_1 = True
        else:
            is_leap_1 = False

print(f"Задание 1 (if-else): год {year} — {'високосный' if is_leap_1 else 'невисокосный'}")

'''Задание 2. Проверка с дополнительными условиями elif'''
if year % 400 == 0:
    is_leap_2 = True
elif year % 100 == 0:
    is_leap_2 = False
elif year % 4 == 0:
    is_leap_2 = True
else:
    is_leap_2 = False

print(f"Задание 2 (elif): год {year} — {'високосный' if is_leap_2 else 'невисокосный'}")

'''Задание 3. Проверка с помощью логических операторов в одну строку if'''
is_leap_3 = True if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else False

print(f"Задание 3 (одна строка): год {year} — {'високосный' if is_leap_3 else 'невисокосный'}")

'''Задание 4. Проверка с применением специальной функции модуля calendar'''
# calendar.isleap(year) — возвращает True, если год високосный
is_leap_4 = calendar.isleap(year)

print(f"Задание 4 (calendar.isleap): год {year} — {'високосный' if is_leap_4 else 'невисокосный'}")
