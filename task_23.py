CATEGORY_LIMITS = {
    "жилье": 30,
    "питание": 15,
    "транспорт": 10,
    "здоровье": 10,
    "развлечения": 10,
    "одежда": 5,
    "прочее": 10,
}
DEFAULT_LIMIT = 10

TIPS = {
    "жилье": "пересмотрите тарифы ЖКХ, подключите счётчики, рассмотрите более выгодные условия аренды/ипотеки",
    "питание": "планируйте меню на неделю, покупайте по списку и по акциям, чаще готовьте дома",
    "транспорт": "используйте проездной, каршеринг вместо своего авто для редких поездок, совмещайте маршруты",
    "здоровье": "используйте полис ОМС и профилактику, сравнивайте цены в аптеках",
    "развлечения": "установите месячный лимит, выбирайте бесплатные форматы досуга, проверьте платные подписки",
    "одежда": "покупайте в сезон распродаж, составляйте список нужных вещей заранее",
    "прочее": "ведите детальный учёт: в «прочем» часто прячутся незапланированные траты",
}

RECOMMENDED_SAVINGS_PERCENT = 20
EMERGENCY_FUND_MONTHS = 6

def total(values):
    result = 0.0
    for value in values:
        result += value
    return result


def sort_items_desc(items):
    result = items[:]
    n = len(result)
    for i in range(n):
        best = i
        for j in range(i + 1, n):
            if result[j][1] > result[best][1]:
                best = j
        result[i], result[best] = result[best], result[i]
    return result


def money(value):
    return f"{value:,.2f}".replace(",", " ") + " руб."


def ceil_div(a, b):
    months = int(a / b)
    if months * b < a:
        months += 1
    return months


def read_pairs(title, hint):
    print(f"\n{title}")
    print(hint)
    data = {}
    while True:
        name = input("  Название (пустая строка - закончить ввод): ").strip().lower()
        if name == "":
            break
        amount = float(input(f"  Сумма для «{name}», руб.: "))
        data[name] = data.get(name, 0.0) + amount
    return data

def analyze(incomes, expenses):
    total_income = total(incomes.values())
    total_expenses = total(expenses.values())
    balance = total_income - total_expenses
    savings_rate = balance / total_income * 100 if total_income > 0 else 0.0

    print("АНАЛИЗ ДОХОДОВ И РАСХОДОВ")
    print(f"Общий доход за месяц:    {money(total_income)}")
    print(f"Общие расходы за месяц:  {money(total_expenses)}")
    print(f"Баланс (доход - расход): {money(balance)}")
    print(f"Норма сбережений:        {savings_rate:.1f}% от дохода")

    if balance < 0:
        print("ВНИМАНИЕ: расходы превышают доходы, вы живёте в долг!")
    elif balance == 0:
        print("Вы тратите всё, что зарабатываете: сбережений нет.")
    else:
        print("Бюджет в плюсе - это хороший знак.")

    print("\nСтруктура расходов (от больших к меньшим):")
    ranked = sort_items_desc(list(expenses.items()))
    for name, amount in ranked:
        share = amount / total_income * 100 if total_income > 0 else 0.0
        share_of_exp = amount / total_expenses * 100 if total_expenses > 0 else 0.0
        bar = "#" * int(share_of_exp / 2)
        print(f"  {name:<14} {money(amount):>18}  "
              f"{share:5.1f}% дохода | {share_of_exp:5.1f}% расходов {bar}")

    if ranked:
        print(f"\nСамая затратная категория: «{ranked[0][0]}» ({money(ranked[0][1])})")
        print(f"Наименее затратная категория: «{ranked[-1][0]}» ({money(ranked[-1][1])})")

    return total_income, total_expenses, balance, ranked


def optimize(total_income, expenses, ranked):
    print("РЕКОМЕНДАЦИИ ПО ОПТИМИЗАЦИИ РАСХОДОВ")

    potential = 0.0
    found = False
    for name, amount in ranked:
        limit_percent = CATEGORY_LIMITS.get(name, DEFAULT_LIMIT)
        limit_amount = total_income * limit_percent / 100
        if amount > limit_amount:
            found = True
            excess = amount - limit_amount
            potential += excess
            print(f"- «{name}»: {money(amount)} при рекомендуемом пределе "
                  f"{limit_percent}% дохода ({money(limit_amount)}).")
            print(f"  Перерасход: {money(excess)}.")
            print(f"  Совет: {TIPS.get(name, 'проанализируйте эти траты и сократите необязательные')}.")

    if not found:
        print("Все категории укладываются в рекомендуемые пределы. Отличная работа!")
    else:
        print(f"\nПотенциал экономии при соблюдении норм: {money(potential)} в месяц "
              f"({money(potential * 12)} в год).")
    return potential


def plan_savings(total_income, total_expenses, balance):
    print("СБЕРЕЖЕНИЯ")

    recommended = total_income * RECOMMENDED_SAVINGS_PERCENT / 100
    print(f"Рекомендуемые накопления ({RECOMMENDED_SAVINGS_PERCENT}% дохода): "
          f"{money(recommended)} в месяц")
    actual = balance if balance > 0 else 0.0
    print(f"Фактически можно откладывать:                  {money(actual)} в месяц")

    if actual >= recommended:
        print("Вы откладываете не меньше рекомендуемого. Так держать!")
    else:
        print(f"Не хватает {money(recommended - actual)} в месяц до рекомендуемой нормы.")

    current_savings = float(input("\nВведите вашу текущую сумму накоплений, руб.: "))
    target = total_expenses * EMERGENCY_FUND_MONTHS
    print(f"Цель - «подушка безопасности» на {EMERGENCY_FUND_MONTHS} мес. расходов: {money(target)}")

    if current_savings >= target:
        print(">>> Подушка безопасности уже сформирована. "
              "Можно думать об инвестициях и крупных целях.")
    else:
        remaining = target - current_savings
        print(f"Осталось накопить: {money(remaining)}")
        if actual > 0:
            print(f"  При текущих темпах: {ceil_div(remaining, actual)} мес.")
        else:
            print("  При текущих темпах накопить не получится - сначала сократите расходы.")
        if recommended > 0:
            print(f"  При откладывании по рекомендации: {ceil_div(remaining, recommended)} мес.")

    return current_savings


def plan_big_purchases(balance, potential):
    print("ПЛАНИРОВАНИЕ КРУПНЫХ РАСХОДОВ")

    answer = input("Хотите спланировать крупную покупку? (да/нет): ").strip().lower()
    while answer == "да":
        name = input("  Что планируете купить: ").strip()
        cost = float(input("  Стоимость, руб.: "))
        months = int(input("  Желаемый срок накопления, мес.: "))

        per_month = cost / months
        print(f"\n  Цель «{name}»: {money(cost)} за {months} мес.")
        print(f"  Нужно откладывать: {money(per_month)} в месяц")

        if balance > 0 and per_month <= balance:
            print(f"Цель реальна: свободного остатка ({money(balance)}) хватает.")
            left = balance - per_month
            print(f"      После откладывания на цель останется {money(left)} в месяц.")
        else:
            print(f"При текущем балансе ({money(balance)}) уложиться в срок не получится.")
            if balance > 0:
                print(f"      Накопить на текущем балансе можно за {ceil_div(cost, balance)} мес.")
            if potential > 0 and balance + potential > 0:
                boosted = balance + potential
                print(f"      Если сократить расходы до рекомендуемых норм, "
                      f"доступно {money(boosted)} в месяц:")
                print(f"      срок составит {ceil_div(cost, boosted)} мес.")
            print("      Варианты: увеличить срок, найти дополнительный доход "
                  "или рассмотреть рассрочку без переплаты.")

        answer = input("\nСпланировать ещё одну покупку? (да/нет): ").strip().lower()


def main():
    print("ЛИЧНЫЙ ФИНАНСОВЫЙ ПОМОЩНИК")
    print("Введите данные за один месяц.")

    incomes = read_pairs(
        "ДОХОДЫ",
        "Примеры: зарплата, подработка, стипендия, проценты по вкладу."
    )
    expenses = read_pairs(
        "РАСХОДЫ",
        "Примеры категорий: жилье, питание, транспорт, здоровье, "
        "развлечения, одежда, прочее."
    )

    total_income, total_expenses, balance, ranked = analyze(incomes, expenses)
    potential = optimize(total_income, expenses, ranked)
    plan_savings(total_income, total_expenses, balance)
    plan_big_purchases(balance, potential)



if __name__ == "__main__":
    main()