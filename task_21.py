# Задача 21. Замер времени
import time
from functools import wraps


def timing(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = (time.perf_counter() - start) * 1000
        print(f"Функция {func.__name__} выполнилась за {elapsed:.3f} мс")
        return result
    return wrapper


@timing
def sumToN(n):
    total = 0
    for i in range(n + 1):
        total += i
    return total


@timing
def pause():
    time.sleep(0.2)


def main():
    print(f"Сумма чисел от 0 до 1000000: {sumToN(1000000)}")
    pause()


if __name__ == "__main__":
    main()
