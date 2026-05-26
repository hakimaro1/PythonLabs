# Задание 1. Средняя температура за день (очистка списка от None)


def remove_none_values(temperatures):
        return [value for value in temperatures if value is not None]


def average_temperature(temperatures):
        return sum(temperatures) / len(temperatures)


def parse_temperature_item(item):
        normalized = item.strip().lower()
    if normalized in ("none", "null", ""):
        return None
    return int(item)


def main():
        print("Введите температуры через пробел (для сбоя устройства укажите None):")

    raw_input_line = input("> ").split()
    temperatures = [parse_temperature_item(item) for item in raw_input_line]

    valid_temperatures = remove_none_values(temperatures)
    average = average_temperature(valid_temperatures)

    print(f"Исходный список: {temperatures}")
    print(f"Очищенный список: {valid_temperatures}")
    print(f"Средняя температура: {average:.2f}")


if __name__ == "__main__":
    main()
