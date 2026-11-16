import json
from meal import Meal
from workout import Workout
from food_product import FoodProduct
from exercise import Exercise
from achievements import (
    Achievement,
    BurnedCaloriesAchievement,
    WorkoutCountAchievement,
    ProteinGoalAchievement,
    CalorieDeficitAchievement,
)


class DiaryEntry:
    def __init__(self, date_str: str) -> None:
        self.__date = date_str
        self.__meals: list[Meal] = []
        self.__workouts: list[Workout] = []

    def get_date(self) -> str:
        return self.__date

    def get_meals(self) -> list[Meal]:
        return list(self.__meals)

    def get_workouts(self) -> list[Workout]:
        return list(self.__workouts)

    def add_meal(self, meal: Meal) -> None:
        if meal is None:
            raise ValueError("Прийом їжі не може бути порожнім!")
        self.__meals.append(meal)

    def add_workout(self, workout: Workout) -> None:
        if workout is None:
            raise ValueError("Тренування не може бути порожнім!")
        self.__workouts.append(workout)

    def get_consumed_nutrition(self) -> dict:
        total = {"calories": 0.0, "protein": 0.0, "fat": 0.0, "carbs": 0.0}
        for meal in self.__meals:
            nutrition = meal.get_total_nutrition()
            total["calories"] += nutrition["calories"]
            total["protein"] += nutrition["protein"]
            total["fat"] += nutrition["fat"]
            total["carbs"] += nutrition["carbs"]

        return {
            "calories": round(total["calories"], 2),
            "protein": round(total["protein"], 2),
            "fat": round(total["fat"], 2),
            "carbs": round(total["carbs"], 2),
        }

    def get_consumed_calories(self) -> float:
        return self.get_consumed_nutrition()["calories"]

    def get_burned_calories(self) -> float:
        return round(sum(workout.get_total_calories() for workout in self.__workouts), 2)

    def get_total_workout_duration(self) -> float:
        return round(sum(workout.get_total_duration() for workout in self.__workouts), 2)

    def get_daily_balance(self) -> float:
        return round(self.get_consumed_calories() - self.get_burned_calories(), 2)

    def evaluate_achievements(self, achievements: list[Achievement]) -> list[Achievement]:
        return [ach for ach in achievements if ach.is_unlocked(self)]

    def get_bonus_points(self, achievements: list[Achievement]) -> int:
        return sum(ach.get_points() for ach in self.evaluate_achievements(achievements))

    def check_achievements(self, achievements: list[Achievement] | None = None) -> list[str]:
        if achievements is None:
            achievements = [
                BurnedCaloriesAchievement("Спалювач калорій", min_calories=500, points=50),
                WorkoutCountAchievement("Подвійний удар", min_workouts=2, points=40),
            ]
        return [str(ach) for ach in self.evaluate_achievements(achievements)]


class Diary:
    def __init__(self) -> None:
        self.__entries: dict[str, DiaryEntry] = {}
        self.__achievements: list[Achievement] = [
            BurnedCaloriesAchievement("Спалювач калорій", min_calories=500, points=50),
            WorkoutCountAchievement("Подвійний удар", min_workouts=2, points=40),
            ProteinGoalAchievement("Білковий баланс", min_protein_g=80, points=30),
            CalorieDeficitAchievement("Контроль балансу", max_balance=1200, points=60),
        ]

    def add_achievement(self, achievement: Achievement) -> None:
        if achievement is None:
            raise ValueError("Досягнення не може бути порожнім!")
        self.__achievements.append(achievement)

    def get_achievements(self) -> list[Achievement]:
        return list(self.__achievements)

    def get_or_create_entry(self, date_str: str) -> DiaryEntry:
        if date_str not in self.__entries:
            self.__entries[date_str] = DiaryEntry(date_str)
        return self.__entries[date_str]

    def find_entry_by_date(self, date_str: str) -> DiaryEntry | None:
        return self.__entries.get(date_str)

    def filter_entries_by_burned_calories(self, min_calories: float) -> list[DiaryEntry]:
        return [
            entry
            for entry in self.get_sorted_entries(by="date", reverse=False)
            if entry.get_burned_calories() >= min_calories
        ]

    def filter_entries_with_achievements(self) -> list[DiaryEntry]:
        return [
            entry
            for entry in self.get_sorted_entries(by="date", reverse=False)
            if len(entry.evaluate_achievements(self.__achievements)) > 0
        ]

    def get_sorted_entries(self, by: str = "date", reverse: bool = True) -> list[DiaryEntry]:
        entries = list(self.__entries.values())
        key_map = {
            "date": lambda e: e.get_date(),
            "burned": lambda e: e.get_burned_calories(),
            "consumed": lambda e: e.get_consumed_calories(),
            "balance": lambda e: e.get_daily_balance(),
            "points": lambda e: e.get_bonus_points(self.__achievements),
        }
        if by not in key_map:
            raise ValueError(f"Невідомий критерій сортування: {by}")

        return sorted(entries, key=key_map[by], reverse=reverse)

    def get_statistics(self) -> dict:
        if not self.__entries:
            return {
                "total_days": 0,
                "total_consumed_kcal": 0.0,
                "total_burned_kcal": 0.0,
                "avg_daily_consumed": 0.0,
                "avg_daily_burned": 0.0,
                "avg_daily_balance": 0.0,
                "avg_daily_protein": 0.0,
                "total_workout_min": 0.0,
                "total_bonus_points": 0,
            }

        total_days = len(self.__entries)
        total_consumed = sum(e.get_consumed_calories() for e in self.__entries.values())
        total_burned = sum(e.get_burned_calories() for e in self.__entries.values())
        total_protein = sum(e.get_consumed_nutrition()["protein"] for e in self.__entries.values())
        total_duration = sum(e.get_total_workout_duration() for e in self.__entries.values())
        total_points = sum(e.get_bonus_points(self.__achievements) for e in self.__entries.values())

        return {
            "total_days": total_days,
            "total_consumed_kcal": round(total_consumed, 2),
            "total_burned_kcal": round(total_burned, 2),
            "avg_daily_consumed": round(total_consumed / total_days, 2),
            "avg_daily_burned": round(total_burned / total_days, 2),
            "avg_daily_balance": round((total_consumed - total_burned) / total_days, 2),
            "avg_daily_protein": round(total_protein / total_days, 2),
            "total_workout_min": round(total_duration, 2),
            "total_bonus_points": total_points,
        }

    def visualize_statistics(self, bar_width: int = 20) -> str:
        if not self.__entries:
            return "Щоденник порожній — немає даних для візуалізації."

        sorted_entries = self.get_sorted_entries(by="date", reverse=False)
        max_kcal = max(
            max(e.get_consumed_calories(), e.get_burned_calories())
            for e in sorted_entries
        )
        max_kcal = max(max_kcal, 1.0)

        lines = ["=== ВІЗУАЛІЗАЦІЯ АКТИВНОСТІ ПО ДНЯХ ==="]
        for entry in sorted_entries:
            consumed = entry.get_consumed_calories()
            burned = entry.get_burned_calories()
            points = entry.get_bonus_points(self.__achievements)

            c_len = int((consumed / max_kcal) * bar_width)
            b_len = int((burned / max_kcal) * bar_width)

            c_bar = "█" * c_len + "░" * (bar_width - c_len)
            b_bar = "▓" * b_len + "░" * (bar_width - b_len)

            lines.append(f"\nДата: {entry.get_date()} | Бонуси: +{points} балів")
            lines.append(f"  Спожито : [{c_bar}] {consumed} ккал")
            lines.append(f"  Спалено : [{b_bar}] {burned} ккал")

        return "\n".join(lines)

    def save_to_file(self, filename: str) -> None:
        data_to_save = {}
        for entry in self.get_sorted_entries(by="date", reverse=False):
            date = entry.get_date()
            nutrition = entry.get_consumed_nutrition()
            data_to_save[date] = {
                "nutrition": nutrition,
                "burned_kcal": entry.get_burned_calories(),
                "workout_duration_min": entry.get_total_workout_duration(),
                "balance": entry.get_daily_balance(),
                "bonus_points": entry.get_bonus_points(self.__achievements),
                "achievements": entry.check_achievements(self.__achievements),
                "meals_summary": [
                    {"name": m.get_name(), "nutrition": m.get_total_nutrition()}
                    for m in entry.get_meals()
                ],
                "workouts_summary": [
                    {
                        "name": w.get_name(),
                        "weight_kg": w.get_weight_kg(),
                        "duration_min": w.get_total_duration(),
                        "calories": w.get_total_calories(),
                    }
                    for w in entry.get_workouts()
                ],
            }

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data_to_save, f, ensure_ascii=False, indent=4)

    def load_from_file(self, filename: str) -> None:
        with open(filename, "r", encoding="utf-8") as f:
            loaded_data = json.load(f)

        self.__entries.clear()
        for date_str, record in loaded_data.items():
            entry = self.get_or_create_entry(date_str)

            for m_data in record.get("meals_summary", []):
                nut = m_data["nutrition"]
                meal = Meal(m_data["name"])
                if nut["calories"] > 0 or nut["protein"] > 0 or nut["fat"] > 0 or nut["carbs"] > 0:
                    restored_food = FoodProduct(
                        name=f"{m_data['name']} (відновлено)",
                        calories_per_100g=nut["calories"],
                        protein_per_100g=nut["protein"],
                        fat_per_100g=nut["fat"],
                        carbs_per_100g=nut["carbs"],
                    )
                    meal.add_item(restored_food, 100.0)
                entry.add_meal(meal)

            for w_data in record.get("workouts_summary", []):
                weight = w_data.get("weight_kg", 70.0)
                duration = w_data.get("duration_min", 0.0)
                calories = w_data.get("calories", 0.0)

                workout = Workout(w_data["name"], weight)
                if duration > 0 and calories > 0:
                    met = (calories * 60.0) / (weight * duration)
                    part = workout.add_part("Відновлена частина")
                    restored_ex = Exercise(
                        name=f"{w_data['name']} (відновлено)",
                        activity_type="Відновлено",
                        met=round(met, 4),
                    )
                    part.add_exercise(restored_ex, duration)
                entry.add_workout(workout)
