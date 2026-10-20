def exchangeMoney(amount, denominations):
    """Возвращает список пар (номинал, количество)."""
    result = []
    for value in denominations:
        count = amount // value
        amount = amount % value
        result.append((value, count))
    return result


def main():
    amount = int(input("Введите сумму в рублях: "))
    denominations = [100, 50, 10, 5, 2, 1]
    print(f"Для размена суммы {amount} руб. потребуется:")
    for value, count in exchangeMoney(amount, denominations):
        kind = "купюр" if value >= 5 else "монет"
        print(f"  {kind} номиналом {value} руб.: {count} шт.")


if __name__ == "__main__":
    main()
