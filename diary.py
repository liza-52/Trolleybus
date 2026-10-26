import json
from meal import Meal
from workout import Workout

class DiaryEntry:
    def __init__(self, date_str: str) -> None:
        self.__date = date_str
        self.__meals = []      
        self.__workouts = []   

    def get_date(self) -> str:
        return self.__date

    def add_meal(self, meal: Meal) -> None:
        if meal is None:
            raise ValueError("Прийом їжі не може бути порожнім")
        self.__meals.append(meal)

    def add_workout(self, workout: Workout) -> None:
        if workout is None:
            raise ValueError("Тренування не може бути порожнім")
        self.__workouts.append(workout)

    def get_consumed_calories(self) -> float:
        return round(sum(meal.get_total_calories() for meal in self.__meals), 2)

    def get_burned_calories(self) -> float:
        return round(sum(workout.get_total_calories() for workout in self.__workouts), 2)

    def get_daily_balance(self) -> float:
        return round(self.get_consumed_calories() - self.get_burned_calories(), 2)

    def check_achievements(self) -> list:
        achievements = []
        burned = self.get_burned_calories()
        if burned >= 500:
            achievements.append("Спалювач калорій (більше 500 ккал за день)")
        if len(self.__workouts) >= 2:
            achievements.append("Подвійний удар (2+ тренування за день)")
        return achievements


class Diary:
    def __init__(self) -> None:
        self.__entries = {}

    def get_or_create_entry(self, date_str: str) -> DiaryEntry:
        if date_str not in self.__entries:
            self.__entries[date_str] = DiaryEntry(date_str)
        return self.__entries[date_str]

    def get_sorted_entries(self, reverse: bool = True) -> list:
        sorted_dates = sorted(self.__entries.keys(), reverse=reverse)
        return [self.__entries[date] for date in sorted_dates]

    def get_statistics(self) -> dict:
        if not self.__entries:
            return {"total_days": 0, "avg_balance": 0.0}

        total_consumed = sum(entry.get_consumed_calories() for entry in self.__entries.values())
        total_burned = sum(entry.get_burned_calories() for entry in self.__entries.values())
        total_days = len(self.__entries)

        return {
            "total_days": total_days,
            "total_consumed_kcal": round(total_consumed, 2),
            "total_burned_kcal": round(total_burned, 2),
            "avg_daily_balance": round((total_consumed - total_burned) / total_days, 2)
        }

    def save_to_file(self, filename: str) -> None:
        data_to_save = {}
        for date, entry in self.__entries.items():
            data_to_save[date] = {
                "consumed_kcal": entry.get_consumed_calories(),
                "burned_kcal": entry.get_burned_calories(),
                "balance": entry.get_daily_balance(),
                "achievements": entry.check_achievements()
            }
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data_to_save, f, ensure_ascii=False, indent=4)
