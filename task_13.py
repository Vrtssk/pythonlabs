def parseNumbers(line):
    numbers = []
    token = ""
    for char in line + " ":
        if char == " ":
            if token != "":
                if "." in token:
                    numbers.append(float(token))
                else:
                    numbers.append(int(token))
                token = ""
        else:
            token += char
    return numbers


def countOf(numbers, value):
    count = 0
    for number in numbers:
        if number == value:
            count += 1
    return count


def main():
    numbers = parseNumbers(input("Введите числа через пробел: "))

    unique = []
    repeated = []
    for number in numbers:
        if number not in unique:
            unique.append(number)
        if countOf(numbers, number) > 1 and number not in repeated:
            repeated.append(number)

    even = []
    odd = []
    negative = []
    floats = []
    multiplesOfFive = 0
    for number in unique:
        if isinstance(number, int):
            if number % 2 == 0:
                even.append(number)
            else:
                odd.append(number)
        else:
            floats.append(number)
        if number < 0:
            negative.append(number)
    for number in numbers:
        if number % 5 == 0:
            multiplesOfFive += number

    biggest = numbers[0]
    smallest = numbers[0]
    for number in numbers:
        if number > biggest:
            biggest = number
        if number < smallest:
            smallest = number

    print(f"Введённые числа: {numbers}")
    print(f"1. Уникальные числа (без повторов): {unique}")
    print(f"2. Повторяющиеся числа: {repeated}")
    print(f"3. Чётные числа: {even}; нечётные числа: {odd}")
    print(f"4. Отрицательные числа: {negative}")
    print(f"5. Числа с плавающей точкой: {floats}")
    print(f"6. Сумма чисел, кратных 5: {multiplesOfFive}")
    print(f"7. Самое большое число: {biggest}")
    print(f"8. Самое маленькое число: {smallest}")


if __name__ == "__main__":
    main()
