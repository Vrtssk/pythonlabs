def mergeValues(first, second):
    if isinstance(first, dict) and isinstance(second, dict):
        mergeDicts(first, second)
        return first
    if isinstance(first, list) and isinstance(second, list):
        for item in second:
            first.append(item)
        return first
    if isinstance(first, set) and isinstance(second, set):
        first.update(second)
        return first
    if isinstance(first, tuple) and isinstance(second, tuple):
        return first + second
    return second


def mergeDicts(dictA, dictB):
    for key, value in dictB.items():
        if key in dictA:
            dictA[key] = mergeValues(dictA[key], value)
        else:
            dictA[key] = value


def main():
    dictA = {"a": 1, "b": {"c": 1, "f": 4}}
    dictB = {"d": 1, "b": {"c": 2, "e": 3}}
    print(f"dictA до слияния: {dictA}")
    print(f"dictB: {dictB}")
    mergeDicts(dictA, dictB)
    print(f"dictA после слияния: {dictA}")

    dictC = {"x": [1, 2], "y": {1, 2}, "z": (1,), "w": {"k": [1]}}
    dictD = {"x": [3], "y": {2, 3}, "z": (2,), "w": {"k": [2], "m": 5}}
    mergeDicts(dictC, dictD)
    print(f"Слияние с коллекциями: {dictC}")


if __name__ == "__main__":
    main()
