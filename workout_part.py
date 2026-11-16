from exercise import Exercise


class WorkoutPart:

    def __init__(self, name: str) -> None:
        self.__name: str = name
        self.__items: list[tuple[Exercise, float]] = []

    def get_name(self) -> str:
        return self.__name

    def add_exercise(self, exercise: Exercise, duration_min: float) -> None:
        if duration_min <= 0:
            raise ValueError("Тривалість вправи повинна бути більше 0!")

        self.__items.append((exercise, float(duration_min)))

    def get_exercises_count(self) -> int:
        return len(self.__items)

    def get_exercise_names(self) -> list:
        names = []
        for exercise, duration in self.__items:
            names.append(exercise.get_name())
        return names

    def get_duration_min(self) -> float:
        total = 0.0
        for exercise, duration in self.__items:
            total += duration
        return total

    def calculate_calories(self, weight_kg: float) -> float:
        total = 0.0
        for exercise, duration in self.__items:
            total += exercise.calculate_calories(weight_kg, duration)["calories"]
        return round(total, 2)
