def splitWords(text):
    words = []
    current = ""
    for char in text:
        if char.isalnum() or char == "-":
            current += char.lower()
        else:
            if current != "":
                words.append(current)
                current = ""
    if current != "":
        words.append(current)
    return words


def countFrequency(words):
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency


def analyze(words, title):
    print(f"\n{title}")
    if len(words) == 0:
        print("Слов нет")
        return

    print(f"Слова: {words}")
    print(f"Общее количество слов: {len(words)}")

    frequency = countFrequency(words)
    print("Частота слов:")
    for word, count in frequency.items():
        print(f"  {word}: {count}")

    topWord = words[0]
    for word in frequency:
        if frequency[word] > frequency[topWord]:
            topWord = word
    print(f"Самое частое слово: '{topWord}' ({frequency[topWord]} раз(а))")

    shortest = words[0]
    longest = words[0]
    for word in words:
        if len(word) < len(shortest):
            shortest = word
        if len(word) > len(longest):
            longest = word
    print(f"Самое короткое слово: '{shortest}'")
    print(f"Самое длинное слово: '{longest}'")


def main():
    text = input("Введите текст: ")
    words = splitWords(text)
    analyze(words, "Анализ исходного текста")

    filtered = []
    for word in words:
        if len(word) >= 3:
            filtered.append(word)
    analyze(filtered, "Анализ после удаления слов короче трёх символов")


if __name__ == "__main__":
    main()
