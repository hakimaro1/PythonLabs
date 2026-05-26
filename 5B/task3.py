# Задание 3. Возведение числа в степень (рекурсивный и итеративный способы)


def power_recursive(base, exponent):
        if exponent == 0:
        return 1
    return base * power_recursive(base, exponent - 1)


def power_iterative(base, exponent):
        result = 1
    for _ in range(exponent):
        result *= base
    return result


def main():
    
    base = float(input("Введите основание: "))
    exponent = int(input("Введите степень (целое неотрицательное число): "))

    if exponent < 0:
        print("Степень должна быть неотрицательной.")
        return

    recursive_result = power_recursive(base, exponent)
    iterative_result = power_iterative(base, exponent)

    print(f"Рекурсивный способ: {recursive_result:.2f}")
    print(f"Итеративный способ: {iterative_result:.2f}")


if __name__ == "__main__":
    main()
