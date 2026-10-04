from dish import Dish
from food_product import FoodProduct
from exercise import Exercise
from diary import Diary

def run_test():
    apple = FoodProduct(name="Яблуко", calories_per_100g=52, protein_per_100g=0.3, fat_per_100g=0.2, carbs_per_100g=13.8)
    oatmeal = Dish(name="Вівсянка з молоком", total_weight_grams=300, total_calories=350, total_protein=15, total_fat=10, total_carbs=50)
    running = Exercise(name="Ранкова пробіжка", activity_type="Кардіо", met=9.8)

    my_diary = Diary()
    
    today_entry = my_diary.get_or_create_entry("2026-10-04")
    
    today_entry.add_food(apple, 200)
    today_entry.add_food(oatmeal, 150)
    
    today_entry.add_exercise(running, duration_min=45, user_weight_kg=70)

    print("=== ДЕННИЙ ЗВІТ (2026-10-04) ===")
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