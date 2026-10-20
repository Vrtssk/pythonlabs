# Задача 10. Система скидок в магазине
from datetime import date

MAX_DISCOUNT = 25


def calculateDiscount(amount, age, isBirthday, isVip):
    rules = []

    regular = 0
    if amount > 1000:
        regular = 10
        rules.append("сумма покупки > 1000 руб.: 10%")

    discount = regular
    if isVip:
        if 15 > regular:
            discount = 15
        rules.append("VIP-клиент: 15% (берется максимальная из обычной и VIP)")

    if age >= 63:
        discount += 5
        rules.append("пенсионер: +5%")
    if isBirthday:
        discount += 5
        rules.append("день рождения: +5%")

    if discount > MAX_DISCOUNT:
        discount = MAX_DISCOUNT
        rules.append(f"применено ограничение максимальной скидки: {MAX_DISCOUNT}%")

    return discount, rules


def main():
    amount = float(input("Введите сумму покупки (руб.): "))
    birthDate = input("Введите дату рождения (ДД.ММ.ГГГГ): ")
    isVip = input("Клиент VIP? (да/нет): ").strip().lower() == "да"

    day, month, year = (int(part) for part in birthDate.split("."))
    today = date.today()
    age = today.year - year
    if (today.month, today.day) < (month, day):
        age -= 1
    isBirthday = (today.day, today.month) == (day, month)

    discount, rules = calculateDiscount(amount, age, isBirthday, isVip)
    finalPrice = amount * (1 - discount / 100)

    print(f"Возраст покупателя: {age}")
    print("Применённые правила:")
    for rule in rules:
        print(f"  - {rule}")
    if not rules:
        print("  скидки не предусмотрены")
    print(f"Итоговая скидка: {discount}%")
    print(f"Сумма к оплате: {finalPrice:.2f} руб.")


if __name__ == "__main__":
    main()
