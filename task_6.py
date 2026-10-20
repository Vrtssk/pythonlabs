ZODIAC_SIGNS = [
    (1, 19, "Козерог"),
    (2, 18, "Водолей"),
    (3, 20, "Рыбы"),
    (4, 19, "Овен"),
    (5, 20, "Телец"),
    (6, 20, "Близнецы"),
    (7, 22, "Рак"),
    (8, 22, "Лев"),
    (9, 22, "Дева"),
    (10, 22, "Весы"),
    (11, 21, "Скорпион"),
    (12, 21, "Стрелец"),
]


def getZodiacSign(day, month):
    for lastMonth, lastDay, sign in ZODIAC_SIGNS:
        if (month, day) <= (lastMonth, lastDay):
            return sign
    return "Козерог" 


def main():
    day = int(input("Введите день рождения (число): "))
    month = int(input("Введите месяц рождения (число): "))
    print(f"Ваш знак зодиака: {getZodiacSign(day, month)}")


if __name__ == "__main__":
    main()
