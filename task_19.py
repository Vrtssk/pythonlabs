# Задача 19. Декоратор кэширования
from functools import wraps


def cache(func):
    """Кэширует результаты вызовов в словаре по аргументам."""
    storage = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        key = (args, tuple(kwargs.items()))
        try:
            hash(key)
        except TypeError:  # нехэшируемые аргументы (списки, словари)
            key = repr(key)

        if key in storage:
            print(f"  [кэш] {func.__name__}{args} -> результат взят из кэша")
            return storage[key]
        print(f"  [вызов] {func.__name__}{args} -> вычисляем")
        result = func(*args, **kwargs)
        storage[key] = result
        return result
    return wrapper


@cache
def slowSquare(n):
    return n * n


def main():
    print(f"slowSquare(4) = {slowSquare(4)}")
    print(f"slowSquare(4) = {slowSquare(4)}")
    print(f"slowSquare(5) = {slowSquare(5)}")
    print(f"slowSquare(5) = {slowSquare(5)}")


if __name__ == "__main__":
    main()
