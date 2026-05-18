
def max_of_three(a: float, b: float, c: float) -> float:
   
    max_value = a
    if b > max_value:
        max_value = b
    if c > max_value:
        max_value = c
    return max_value


def main() -> None:
    print("Наибольшее из трёх чисел")
    print("-" * 28)

    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    c = float(input("Введите третье число: "))

    result = max_of_three(a, b, c)
    print(f"\nЧисла: {a}, {b}, {c}")
    print(f"Наибольшее: {result}")


if __name__ == "__main__":
    main()
