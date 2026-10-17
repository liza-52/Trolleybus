from exercise import Exercise

class WorkoutPart:
    def __init__(self, exercise: Exercise, duration_min: float) -> None:
        if duration_min <= 0:
            raise ValueError("Тривалість частини тренування повинна бути більше 0!")

        self.__exercise: Exercise = exercise
        self.__duration_min: float = float(duration_min)

    def get_exercise(self) -> Exercise:
        return self.__exercise

    def get_duration_min(self) -> float:
        return self.__duration_min

    def calculate_calories(self, weight_kg: float) -> dict:
        return self.__exercise.calculate_calories(weight_kg, self.__duration_min)
