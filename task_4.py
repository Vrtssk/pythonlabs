def normalize(text):
    result = ""
    for char in text:
        if char.isalnum():
            result += char.lower()
    return result


def isPalindrome(text):
    text = normalize(text)
    left = 0
    right = len(text) - 1
    while left < right:
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1
    return True


def main():
    text = input("Введите строку: ")
    if isPalindrome(text):
        print(f"Строка '{text}' является палиндромом")
    else:
        print(f"Строка '{text}' не является палиндромом")


if __name__ == "__main__":
    main()
