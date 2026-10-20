import random


def main():
    secret = random.randint(1, 100)
    attempts = 0
    print("Я загадал число от 1 до 100. Попробуйте угадать!")

    while True:
        guess = int(input("Ваша догадка: "))
        attempts += 1
        if guess < secret:
            print("Больше")
        elif guess > secret:
            print("Меньше")
        else:
            print(f"Поздравляю! Вы угадали число {secret} за {attempts} попыток(ки).")
            break


if __name__ == "__main__":
    main()
