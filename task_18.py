# Задача 18. Декоратор вызовов
from datetime import datetime
from functools import wraps


def logCalls(fileName):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            timeString = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open(fileName, "a", encoding="utf-8") as file:
                file.write(f"{timeString} | {func.__name__} | args={args} | kwargs={kwargs}\n")
            return func(*args, **kwargs)
        return wrapper
    return decorator


@logCalls("calls.log")
def add(a, b):
    return a + b


@logCalls("calls.log")
def greet(name, greeting="Привет"):
    return f"{greeting}, {name}!"


def main():
    print(f"add(2, 3) = {add(2, 3)}")
    print(f"greet('Мир', greeting='Здравствуй') = {greet('Мир', greeting='Здравствуй')}")
    print("Содержимое файла calls.log:")
    with open("calls.log", encoding="utf-8") as file:
        print(file.read())


if __name__ == "__main__":
    main()
