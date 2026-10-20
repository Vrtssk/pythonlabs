BASE_PRICE = 24.99
INCLUDED_MINUTES = 60
INCLUDED_SMS = 30
INCLUDED_MB = 1024  
MINUTE_PRICE = 0.89
SMS_PRICE = 0.59
MB_PRICE = 0.79
TAX_RATE = 0.02


def main():
    minutes = int(input("Введите количество минут разговора: "))
    sms = int(input("Введите количество SMS-сообщений: "))
    traffic = int(input("Введите интернет-трафик (в Мб): "))

    total = BASE_PRICE
    print(f"Базовая сумма тарификации: {BASE_PRICE:.2f} руб.")

    if minutes > INCLUDED_MINUTES:
        extra = minutes - INCLUDED_MINUTES
        cost = extra * MINUTE_PRICE
        total += cost
        print(f"Дополнительные минуты ({extra} шт.): {cost:.2f} руб.")

    if sms > INCLUDED_SMS:
        extra = sms - INCLUDED_SMS
        cost = extra * SMS_PRICE
        total += cost
        print(f"Дополнительные сообщения ({extra} шт.): {cost:.2f} руб.")

    if traffic > INCLUDED_MB:
        extra = traffic - INCLUDED_MB
        cost = extra * MB_PRICE
        total += cost
        print(f"Дополнительный интернет-трафик ({extra} Мб): {cost:.2f} руб.")

    tax = total * TAX_RATE
    print(f"Налог (2%): {tax:.2f} руб.")
    print(f"Итоговая сумма к оплате: {total + tax:.2f} руб.")


if __name__ == "__main__":
    main()
