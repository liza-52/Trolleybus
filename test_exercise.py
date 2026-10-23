import os

from exercise import Exercise
from workout import Workout
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
    if os.path.exists("test_met_values.json"):
        os.remove("test_met_values.json")
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

    print("\n=== ТЕСТ КОМПОЗИЦІЇ (Workout -> WorkoutPart) ===")
    workout = Workout("Ранкове тренування", weight_kg=70)
    workout.add_part(catalog.get_exercise("Ходьба"), duration_min=10)
    workout.add_part(catalog.get_exercise("Біг"), duration_min=30)
    workout.add_part(catalog.get_exercise("Йога"), duration_min=20)
    print(workout)
    print(f"Загальна тривалість: {workout.get_total_duration()} хв")
    print(f"Загальні калорії: {workout.get_total_calories()} ккал")
    for info in workout.get_parts_info():
        print(f"  {info['activity']}: {info['duration_min']} хв, {info['calories']} ккал")

    try:
        workout.add_part(catalog.get_exercise("Біг"), duration_min=0)
    except ValueError as e:
        print(f"Очікувана помилка (нульова тривалість частини): {e}")

    try:
        Workout("Погане тренування", weight_kg=0)
    except ValueError as e:
        print(f"Очікувана помилка (нульова вага): {e}")

    try:
        workout.add_part(catalog.get_exercise("Танці"), duration_min=15)
    except ValueError as e:
        print(f"Очікувана помилка (вправи немає у каталозі): {e}")

    print("\n=== ТЕСТ АГРЕГАЦІЇ (вправа живе без каталогу) ===")
    removed = catalog.remove_exercise("Бокс")
    print(f"Каталог після видалення: {catalog.list_exercises()}")
    print(f"Об'єкт вправи все ще існує: {removed}")

    boxing_workout = Workout("Бокс вдома", weight_kg=65)
    boxing_workout.add_part(removed, duration_min=30)
    print(f"Калорії тренування з видаленою вправою: {boxing_workout.get_total_calories()} ккал")

    catalog.remove_exercise("Йога")
    print(f"Калорії ранкового тренування після видалення 'Йога' з каталогу: "
          f"{workout.get_total_calories()} ккал")

    try:
        catalog.remove_exercise("Йога")
    except ValueError as e:
        print(f"Очікувана помилка (вправу вже видалено): {e}")

    print("\nВсі тести виконано успішно!")


if __name__ == "__main__":
    run_test()
