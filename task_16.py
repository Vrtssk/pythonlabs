def flattenList(items):
    i = 0
    while i < len(items):
        if isinstance(items[i], list):
            inner = items[i]
            flattenList(inner)
            items[i:i + 1] = inner
            i += len(inner)
        else:
            i += 1


def main():
    listA = [1, 2, 3, [4], 5, [6, [7, [], 8, [9]]]]
    print(f"Исходный список: {listA}")
    flattenList(listA)
    print(f"Плоский список: {listA}")


if __name__ == "__main__":
    main()
