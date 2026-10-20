def collectUnique(items, result):
    for item in items:
        if isinstance(item, list):
            collectUnique(item, result)
        elif item not in result:
            result.append(item)


def uniqueElements(items):
    result = []
    collectUnique(items, result)
    return result


def main():
    listA = [1, 2, 3, [4, 3, 1], 5, [6, [7, [10], 8, [9, 2, 3]]]]
    print(f"Исходный список: {listA}")
    print(f"Уникальные элементы: {uniqueElements(listA)}")


if __name__ == "__main__":
    main()
