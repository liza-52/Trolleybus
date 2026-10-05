import json
import os

from exercise import Exercise

DEFAULT_EXERCISES = {
    "Біг": {"activity_type": "кардіо", "met": 9.8},
    "Ходьба": {"activity_type": "кардіо", "met": 3.5},
    "Велосипед": {"activity_type": "кардіо", "met": 7.5},
    "Плавання": {"activity_type": "кардіо", "met": 8.0},
    "Йога": {"activity_type": "розтяжка", "met": 2.5},
    "Силове тренування": {"activity_type": "сила", "met": 6.0},
}


class ExerciseCatalog:
    def __init__(self, filename: str = "met_values.json") -> None:
        self.__filename = filename
        self.__exercises: dict[str, Exercise] = {}
        self.__load_from_file()

    def __load_from_file(self) -> None:
        if not os.path.exists(self.__filename):
            self.__save_data(DEFAULT_EXERCISES)

        with open(self.__filename, "r", encoding="utf-8") as f:
            raw_data = json.load(f)

        for name, info in raw_data.items():
            self.__exercises[name] = Exercise(name, info["activity_type"], info["met"])

    def __save_data(self, data: dict) -> None:
        with open(self.__filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def get_exercise(self, name: str) -> Exercise:
        if name not in self.__exercises:
            raise ValueError(f"Вправу '{name}' не знайдено у каталозі")
        return self.__exercises[name]

    def list_exercises(self) -> list:
        return list(self.__exercises.keys())

    def add_exercise(self, name: str, activity_type: str, met: float) -> None:
        if name in self.__exercises:
            raise ValueError(f"Вправа '{name}' вже існує у каталозі")

        new_exercise = Exercise(name, activity_type, met)
        self.__exercises[name] = new_exercise

        data_to_save = {ex.get_name(): ex.to_dict() for ex in self.__exercises.values()}
        self.__save_data(data_to_save)

    def calculate_calories_for(self, name: str, weight_kg: float, duration_min: float) -> dict:
        exercise = self.get_exercise(name)
        return exercise.calculate_calories(weight_kg, duration_min)
