# Задание 2. Разделение числовых аргументов на два отсортированных списка


def split_and_sort_numbers(*args):
        negatives = sorted((value for value in args if value < 0), reverse=True)
    non_negatives = sorted(value for value in args if value >= 0)
    return negatives, non_negatives


def main():
       print("Введите числа через пробел:")

    raw_input_line = input("> ").split()
    numbers = [float(item) for item in raw_input_line]

    negatives, non_negatives = split_and_sort_numbers(*numbers)

    print(f"Введённые числа: {numbers}")
    print(f"Отрицательные (по убыванию): {negatives}")
    print(f"Неотрицательные (по возрастанию): {non_negatives}")


if __name__ == "__main__":
    main()
