# Задача 15. Аналитика продаж


def calculateRevenue(sales):
    """Выручка по каждому товару (товар может встречаться несколько раз)."""
    revenue = {}
    for sale in sales:
        name = sale["name"]
        total = sale["price"] * sale["quantity"]
        if name in revenue:
            revenue[name] += total
        else:
            revenue[name] = total
    return revenue


def findMostProfitable(revenue):
    bestName = None
    bestValue = None
    for name, value in revenue.items():
        if bestValue is None or value > bestValue:
            bestName = name
            bestValue = value
    return bestName, bestValue


def main():
    sales = [
        {"name": "Ноутбук", "price": 55000, "quantity": 3},
        {"name": "Мышь", "price": 800, "quantity": 40},
        {"name": "Клавиатура", "price": 2500, "quantity": 15},
        {"name": "Монитор", "price": 18000, "quantity": 6},
        {"name": "Мышь", "price": 800, "quantity": 10},
    ]

    revenue = calculateRevenue(sales)
    print("Выручка по каждому товару:")
    for name, value in revenue.items():
        print(f"  {name}: {value:.2f} руб.")

    bestName, bestValue = findMostProfitable(revenue)
    print(f"Самый прибыльный товар: {bestName} ({bestValue:.2f} руб.)")
    print(f"Количество уникальных наименований: {len(revenue)}")


if __name__ == "__main__":
    main()
