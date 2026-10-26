from food_product import FoodProduct
from dish import Dish
from exercise import Exercise
from meal import Meal
from workout import Workout
from diary import Diary

def run_test():
    apple = FoodProduct(name="Яблуко", calories_per_100g=52, protein_per_100g=0.3, fat_per_100g=0.2, carbs_per_100g=13.8)
    oatmeal = Dish(name="Вівсянка з молоком", total_weight_grams=300, total_calories=350, total_protein=15, total_fat=10, total_carbs=50)
    running = Exercise(name="Ранкова пробіжка", activity_type="Кардіо", met=9.8)

    breakfast = Meal(name="Сніданок")
    breakfast.add_item(apple, 200)
    breakfast.add_item(oatmeal, 150)

    morning_workout = Workout(name="Ранкове кардіо", weight_kg=70)
    morning_workout.add_part(running, duration_min=45)

    my_diary = Diary()
    today_entry = my_diary.get_or_create_entry("2026-10-26")
    
    today_entry.add_meal(breakfast)
    today_entry.add_workout(morning_workout)

    print("=== ДЕННИЙ ЗВІТ (2026-10-26) ===")
    print(f"Спожито: {today_entry.get_consumed_calories()} ккал")
    print(f"Спалено: {today_entry.get_burned_calories()} ккал")
    print(f"Баланс: {today_entry.get_daily_balance()} ккал")
    print(f"Досягнення: {', '.join(today_entry.check_achievements())}")

    print("\n=== ЗАГАЛЬНА СТАТИСТИКА ===")
    stats = my_diary.get_statistics()
    print(f"Всього днів у щоденнику: {stats['total_days']}")
    print(f"Загалом спожито: {stats['total_consumed_kcal']} ккал")
    print(f"Загалом спалено: {stats['total_burned_kcal']} ккал")
    print(f"Середній щоденний баланс: {stats['avg_daily_balance']} ккал")

    my_diary.save_to_file("diary_data.json")
    print("\nДані успішно збережено у diary_data.json!")

if __name__ == "__main__":
    run_test()
