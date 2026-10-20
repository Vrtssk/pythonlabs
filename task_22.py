import inspect
from functools import wraps


def typeCheck(*types):
    def decorator(func):
        signature = inspect.signature(func)

        @wraps(func)
        def wrapper(*args, **kwargs):
            bound = signature.bind(*args, **kwargs)
            values = list(bound.arguments.items())
            for (name, value), expectedType in zip(values, types):
                if not isinstance(value, expectedType):
                    raise TypeError(
                        f"Параметр '{name}' должен иметь тип {expectedType.__name__}, "
                        f"получен {type(value).__name__}"
                    )
            return func(*args, **kwargs)
        return wrapper
    return decorator


@typeCheck(int, int)
def add(a, b):
    return a + b


def main():
    print(f"add(2, 3) = {add(2, 3)}")
    try:
        add(2, "3")
    except TypeError as error:
        print(f"Ошибка типа: {error}")


if __name__ == "__main__":
    main()