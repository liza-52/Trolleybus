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

    def add_part(self, part_name: str) -> WorkoutPart:
        part = WorkoutPart(part_name)
        self.__parts.append(part)
        return part

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
            total += part.calculate_calories(self.__weight_kg)
        return round(total, 2)

    def get_parts_info(self) -> list:
        info = []
        for part in self.__parts:
            info.append(
                {
                    "part": part.get_name(),
                    "exercises": part.get_exercise_names(),
                    "duration_min": part.get_duration_min(),
                    "calories": part.calculate_calories(self.__weight_kg),
                }
            )
        return info

    def __str__(self) -> str:
        return f"Тренування '{self.__name}': частин - {len(self.__parts)}"
