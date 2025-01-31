import heapq

def min_connection_cost(cables):
    """
    Функція знаходить мінімальні витрати на об'єднання всіх кабелів у один.
    :param cables: Список довжин кабелів.
    :return: Мінімальні витрати на об'єднання кабелів.
    """
    if len(cables) == 1:
        return 0  # Якщо один кабель - об'єднання не потрібне

    heapq.heapify(cables)  # Перетворюємо список у мінімальну купу
    total_cost = 0

    while len(cables) > 1:
        # Витягуємо два найкоротші кабелі
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)

        # Об'єднуємо їх
        cost = first + second
        total_cost += cost  # Додаємо витрати до загальної суми

        # Додаємо новий об'єднаний кабель назад у купу
        heapq.heappush(cables, cost)

    return total_cost  # Повертаємо загальні мінімальні витрати

# Приклад використання
cables = [4, 3, 2, 6]
result = min_connection_cost(cables)
print(f"Мінімальні витрати на об'єднання кабелів: {result}")
