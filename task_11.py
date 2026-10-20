HISTORY_POINTS = {"отличная": -2, "хорошая": 0, "удовлетворительная": 2, "плохая": 4}


def assessRisk(age, income, amount, term, history, hasGuarantors, hasCollateral):
    loanToIncome = amount / income
    paymentToIncome = (amount / term) / income
    score = 0

    if loanToIncome <= 5:
        score += 0
    elif loanToIncome <= 10:
        score += 1
    elif loanToIncome <= 20:
        score += 2
    else:
        score += 3

    if paymentToIncome <= 0.2:
        score += 0
    elif paymentToIncome <= 0.35:
        score += 1
    elif paymentToIncome <= 0.5:
        score += 2
    else:
        score += 4

    if age < 21 or age > 65:
        score += 2

    score += HISTORY_POINTS[history]
    if hasGuarantors:
        score -= 1
    if hasCollateral:
        score -= 2

    return loanToIncome, paymentToIncome, score


def getCategory(score):
    if score <= 0:
        return "низкий"
    if score <= 3:
        return "средний"
    if score <= 6:
        return "высокий"
    return "критический"


def main():
    age = int(input("Возраст заемщика: "))
    income = float(input("Ежемесячный доход (руб.): "))
    amount = float(input("Размер запрашиваемого кредита (руб.): "))
    term = int(input("Срок кредита (месяцы): "))
    history = input("Кредитная история (отличная/хорошая/удовлетворительная/плохая): ").strip().lower()
    hasGuarantors = input("Есть поручители? (да/нет): ").strip().lower() == "да"
    hasCollateral = input("Есть залог? (да/нет): ").strip().lower() == "да"

    loanToIncome, paymentToIncome, score = assessRisk(
        age, income, amount, term, history, hasGuarantors, hasCollateral
    )
    category = getCategory(score)

    print("\nРезультат оценки")
    print(f"Соотношение кредита к месячному доходу: {loanToIncome:.2f}")
    print(f"Ежемесячный платёж (без процентов) к доходу: {paymentToIncome * 100:.1f}%")
    print(f"Баллы риска: {score}")
    print(f"Категория риска: {category}")

    if category == "низкий":
        print("Процентная ставка: 12% годовых")
        print("Рекомендация: кредит одобрить")
    elif category == "средний":
        print("Процентная ставка: 15% годовых")
        print("Рекомендация: кредит одобрить")
    elif category == "высокий":
        print("Процентная ставка: 19% годовых")
        print("Рекомендация: одобрить с дополнительной проверкой или уменьшить сумму/увеличить срок")
    else:
        print("Процентная ставка: не предлагается")
        print("Рекомендация: в кредите отказать")


if __name__ == "__main__":
    main()
