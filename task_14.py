def parseNumbers(line):
    numbers = []
    token = ""
    for char in line + " ":
        if char == " ":
            if token != "":
                value = float(token) if "." in token else int(token)
                if value not in numbers:  # убираем дубликаты внутри набора
                    numbers.append(value)
                token = ""
        else:
            token += char
    return numbers


def intersection(first, second):
    result = []
    for number in first:
        if number in second:
            result.append(number)
    return result


def difference(first, second):
    result = []
    for number in first:
        if number not in second:
            result.append(number)
    return result


def main():
    first = parseNumbers(input("Введите первый набор чисел через пробел: "))
    second = parseNumbers(input("Введите второй набор чисел через пробел: "))

    both = intersection(first, second)
    onlyFirst = difference(first, second)
    onlySecond = difference(second, first)

    print(f"Первый набор: {first}")
    print(f"Второй набор: {second}")
    print(f"1. Числа, присутствующие в обоих наборах: {both}")
    print(f"2. Есть в первом, но нет во втором: {onlyFirst}")
    print(f"   Есть во втором, но нет в первом: {onlySecond}")
    print(f"3. Числа обоих наборов без общих: {onlyFirst + onlySecond}")


if __name__ == "__main__":
    main()
