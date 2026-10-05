from exercise import Exercise
from exercise_catalog import ExerciseCatalog


def run_test():
    running = Exercise(name="Ранкова пробіжка", activity_type="Кардіо", met=9.8)

    print("=== ТЕСТ ОДНІЄЇ ВПРАВИ ===")
    print(f"Назва: {running.get_name()}")
    print(f"Тип: {running.get_activity_type()}")
    print(f"MET: {running.get_met()}")

    result = running.calculate_calories(weight_kg=70, duration_min=45)
    print(f"Калорії за 45 хв бігу (70 кг): {result['calories']} ккал")

    print("\n=== ТЕСТ ОБРОБКИ ПОМИЛОК ===")
    try:
        Exercise(name="Невірна вправа", activity_type="Тест", met=-5)
    except ValueError as e:
        print(f"Очікувана помилка (негативний MET): {e}")

    try:
        running.calculate_calories(weight_kg=-10, duration_min=30)
    except ValueError as e:
        print(f"Очікувана помилка (негативна вага): {e}")

    try:
        running.calculate_calories(weight_kg=70, duration_min=0)
    except ValueError as e:
        print(f"Очікувана помилка (нульова тривалість): {e}")

    print("\n=== ТЕСТ КАТАЛОГУ ВПРАВ ===")
    catalog = ExerciseCatalog("test_met_values.json")

    print(f"Базові вправи у каталозі: {catalog.list_exercises()}")

    result2 = catalog.calculate_calories_for("Біг", weight_kg=65, duration_min=40)
    print(f"Калорії для 'Біг' (40 хв, 65 кг): {result2['calories']} ккал")

    print("\n=== ДОДАВАННЯ НОВОЇ ВПРАВИ ===")
    catalog.add_exercise("Бокс", "Кардіо", met=10.3)
    print(f"Каталог після додавання: {catalog.list_exercises()}")

    result3 = catalog.calculate_calories_for("Бокс", weight_kg=65, duration_min=30)
    print(f"Калорії для 'Бокс' (30 хв, 65 кг): {result3['calories']} ккал")

    print("\n=== ТЕСТ ПОВТОРНОГО ДОДАВАННЯ ===")
    try:
        catalog.add_exercise("Бокс", "Кардіо", met=12.0)
    except ValueError as e:
        print(f"Очікувана помилка (вправа вже існує): {e}")

    print("\n=== ТЕСТ ПОШУКУ НЕІСНУЮЧОЇ ВПРАВИ ===")
    try:
        catalog.get_exercise("Танці")
    except ValueError as e:
        print(f"Очікувана помилка (вправи немає): {e}")

    print("\nВсі тести виконано успішно!")


if __name__ == "__main__":
    run_test()
