UNITS = {
    "длина": {
        "мм": 0.001, "см": 0.01, "м": 1, "км": 1000,
        "дюйм": 0.0254, "фут": 0.3048, "миля": 1609.344,
    },
    "масса": {
        "г": 0.001, "кг": 1, "т": 1000, "фунт": 0.45359237, "унция": 0.028349523,
    },
    "время": {
        "сек": 1, "мин": 60, "час": 3600, "сутки": 86400, "неделя": 604800,
    },
    "объем": {
        "мл": 0.001, "л": 1, "м3": 1000, "галлон": 3.785411784,
    },
    "данные": {
        "байт": 1, "кб": 1024, "мб": 1024 ** 2, "гб": 1024 ** 3, "тб": 1024 ** 4,
    },
    "скорость": {
        "м/с": 1, "км/ч": 1 / 3.6, "миля/ч": 0.44704, "узел": 0.514444,
    },
    "площадь": {
        "см2": 0.0001, "м2": 1, "га": 10000, "км2": 1000000, "акр": 4046.8564224,
    },
    "температура": {"c": None, "f": None, "k": None},
}


def convertTemperature(value, fromUnit, toUnit):
    if fromUnit == "c":
        celsius = value
    elif fromUnit == "f":
        celsius = (value - 32) * 5 / 9
    else:
        celsius = value - 273.15

    if toUnit == "c":
        return celsius
    if toUnit == "f":
        return celsius * 9 / 5 + 32
    return celsius + 273.15


def convert(category, fromUnit, toUnit, value):
    if category == "температура":
        return convertTemperature(value, fromUnit, toUnit)
    units = UNITS[category]
    return value * units[fromUnit] / units[toUnit]


def main():
    print("Доступные типы измерений:")
    for category, units in UNITS.items():
        print(f"  {category}: {', '.join(units)}")

    category = input("Введите тип измерения: ").strip().lower()
    fromUnit = input("Введите исходную единицу: ").strip().lower()
    toUnit = input("Введите целевую единицу: ").strip().lower()
    value = float(input("Введите значение: "))

    result = convert(category, fromUnit, toUnit, value)
    print(f"Результат: {value} {fromUnit} = {result:.6g} {toUnit}")


if __name__ == "__main__":
    main()
