from food_product import FoodProduct
from dish import Dish
from exercise_types import create_exercise
from meal import Meal
from workout import Workout
from diary import Diary


def run_test():
    apple = FoodProduct("Яблуко", calories_per_100g=52, protein_per_100g=0.3, fat_per_100g=0.2, carbs_per_100g=13.8)
    chicken = FoodProduct("Куряче філе", calories_per_100g=165, protein_per_100g=31.0, fat_per_100g=3.6, carbs_per_100g=0.0)
    oatmeal = Dish("Вівсянка з молоком", total_weight_grams=300, total_calories=350, total_protein=15, total_fat=10, total_carbs=50)

    running = create_exercise("Ранкова пробіжка", "кардіо", met=9.8)
    squats = create_exercise("Присідання зі штангою", "сила", met=6.0)
    stretching = create_exercise("Розтяжка після тренування", "розтяжка", met=2.5)

    breakfast = Meal("Сніданок")
    breakfast.add_item(apple, 200)
    breakfast.add_item(oatmeal, 250)

    lunch = Meal("Обід")
    lunch.add_item(chicken, 250)

    light_dinner = Meal("Легка вечеря")
    light_dinner.add_item(apple, 150)

    morning_run = Workout("Ранкове кардіо", weight_kg=70)
    run_part = morning_run.add_part("Основна пробіжка")
    run_part.add_exercise(running, duration_min=45)

    gym_session = Workout("Силове тренування", weight_kg=70)
    main_part = gym_session.add_part("Базові вправи")
    main_part.add_exercise(squats, duration_min=40)
    cooldown_part = gym_session.add_part("Заминка")
    cooldown_part.add_exercise(stretching, duration_min=15)

    my_diary = Diary()

    day1 = my_diary.get_or_create_entry("2026-11-15")
    day1.add_meal(breakfast)
    day1.add_meal(lunch)
    day1.add_workout(morning_run)
    day1.add_workout(gym_session)

    day2 = my_diary.get_or_create_entry("2026-11-16")
    day2.add_meal(light_dinner)
    day2.add_workout(morning_run)

    print("=== ДЕННІ ЗВІТИ ТА ПОЛІМОРФНІ ДОСЯГНЕННЯ ===")
    for entry in my_diary.get_sorted_entries(by="date", reverse=False):
        nut = entry.get_consumed_nutrition()
        print(f"\nДата: {entry.get_date()}")
        print(f"  Спожито: {nut['calories']} ккал (Б: {nut['protein']}г, Ж: {nut['fat']}г, В: {nut['carbs']}г)")
        print(f"  Спалено: {entry.get_burned_calories()} ккал | Баланс: {entry.get_daily_balance()} ккал")
        print(f"  Бонусні бали за день: {entry.get_bonus_points(my_diary.get_achievements())}")
        for ach_text in entry.check_achievements(my_diary.get_achievements()):
            print(f"    * {ach_text}")

    print("\n=== ПОШУК, ФІЛЬТРАЦІЯ ТА СОРТУВАННЯ ===")
    found = my_diary.find_entry_by_date("2026-11-15")
    print(f"Пошук за 2026-11-15: знайдено запис, спалено {found.get_burned_calories()} ккал")

    active_days = my_diary.filter_entries_by_burned_calories(600)
    print(f"Дні, де спалено >= 600 ккал: {[d.get_date() for d in active_days]}")

    sorted_by_points = my_diary.get_sorted_entries(by="points", reverse=True)
    print(f"Сортування за бонусними балами (спадання): {[d.get_date() for d in sorted_by_points]}")

    print("\n" + my_diary.visualize_statistics())

    filename = "diary_data_lr3.json"
    my_diary.save_to_file(filename)
    print(f"\nДані збережено у {filename}.")

    restored_diary = Diary()
    restored_diary.load_from_file(filename)
    stats = restored_diary.get_statistics()
    print("=== СТАТИСТИКА ПІСЛЯ ВІДНОВЛЕННЯ З ФАЙЛУ ===")
    print(f"Днів відновлено: {stats['total_days']}")
    print(f"Середньодобове споживання: {stats['avg_daily_consumed']} ккал (білок: {stats['avg_daily_protein']} г)")
    print(f"Середньодобові витрати: {stats['avg_daily_burned']} ккал")
    print(f"Загальна сума бонусних балів: {stats['total_bonus_points']}")


if __name__ == "__main__":
    run_test()
