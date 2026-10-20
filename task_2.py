def checkPassword(password):
    """Возвращает оценку надёжности пароля."""
    if len(password) < 16:
        return "Слишком короткий"
    if password.isalpha() or password.isdigit():
        return "Слабый пароль"
    return "Надежный пароль"


def main():
    password = input("Введите пароль: ")
    print(f"Результат проверки пароля: {checkPassword(password)}")


if __name__ == "__main__":
    main()
