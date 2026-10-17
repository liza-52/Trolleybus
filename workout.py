from exercise import Exercise
from workout_part import WorkoutPart


class Workout:
    def __init__(self, name: str, weight_kg: float) -> None:
        if weight_kg <= 0:
            raise ValueError("Вага людини повинна бути більше 0!")

        self.__name: str = name
        self.__weight_kg: float = float(weight_kg)
        self.__parts: list[WorkoutPart] = []

    def get_name(self) -> str:
        return self.__name

    def get_weight_kg(self) -> float:
        return self.__weight_kg

    def add_part(self, exercise: Exercise, duration_min: float) -> None:
        part = WorkoutPart(exercise, duration_min)
        self.__parts.append(part)

    def get_parts_count(self) -> int:
        return len(self.__parts)

    def get_total_duration(self) -> float:
        total = 0.0
        for part in self.__parts:
            total += part.get_duration_min()
        return total

    def get_total_calories(self) -> float:
        total = 0.0
        for part in self.__parts:
            total += part.calculate_calories(self.__weight_kg)["calories"]
        return round(total, 2)

    def get_parts_info(self) -> list:
        info = []
        for part in self.__parts:
            result = part.calculate_calories(self.__weight_kg)
            info.append(
                {
                    "activity": result["activity"],
                    "duration_min": result["duration_min"],
                    "calories": result["calories"],
                }
            )
        return info

    def __str__(self) -> str:
        return f"Тренування '{self.__name}': частин - {len(self.__parts)}"
