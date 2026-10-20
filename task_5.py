def main():
    a = float(input("Введите число a: "))
    b = float(input("Введите число b: "))

    print(f"Сумма a + b = {a + b}")
    print(f"Разность a - b = {a - b}")
    print(f"Произведение a * b = {a * b}")

    if b == 0:
        print("Частное a / b: деление на ноль невозможно")
        print("Остаток a % b: деление на ноль невозможно")
    else:
        print(f"Частное a / b = {a / b}")
        print(f"Остаток a % b = {a % b}")

    try:
        print(f"Степень a ** b = {a ** b}")
    except ZeroDivisionError:
        print("Степень a ** b: ноль нельзя возводить в отрицательную степень")


if __name__ == "__main__":
    main()
