from exercise import Exercise


class CardioExercise(Exercise):

    def get_target_heart_rate(self, age: int) -> dict:
        if age <= 0 or age > 120:
            raise ValueError("Вік повинен бути від 1 до 120!")

        max_pulse = 220 - age
        return {"min": round(max_pulse * 0.6), "max": round(max_pulse * 0.85)}

    def calculate_distance_km(self, speed_kmh: float, duration_min: float) -> float:
        if speed_kmh <= 0 or duration_min <= 0:
            raise ValueError("Швидкість і тривалість повинні бути більше 0!")

        return round(speed_kmh * duration_min / 60.0, 2)

    def get_recommended_duration_min(self) -> int:
        return 30

    def get_advice(self) -> str:
        return "Стежте за пульсом і пийте воду."


class FlexibilityExercise(Exercise):

    HOLD_TIME_SEC = 30

    def get_hold_time_sec(self) -> int:
        return self.HOLD_TIME_SEC

    def get_intensity_level(self) -> str:
        return "низька"

    def get_recommended_duration_min(self) -> int:
        return 15

    def get_advice(self) -> str:
        return "Робіть після основної частини, без ривків."


class StrengthExercise(Exercise):

    AFTERBURN = 1.1
    REST_TIME_SEC = 90

    def calculate_calories(self, weight_kg: float, duration_min: float) -> dict:
        result = super().calculate_calories(weight_kg, duration_min)
        result["calories"] = round(result["calories"] * self.AFTERBURN, 2)
        return result

    def calculate_volume(self, sets: int, reps: int, load_kg: float) -> float:
        if sets <= 0 or reps <= 0 or load_kg <= 0:
            raise ValueError("Підходи, повтори і вага повинні бути більше 0!")

        return sets * reps * load_kg

    def get_rest_time_sec(self) -> int:
        return self.REST_TIME_SEC

    def get_recommended_duration_min(self) -> int:
        return 45

    def get_advice(self) -> str:
        return "Відпочивайте 1-2 хвилини між підходами."


def create_exercise(name: str, activity_type: str, met: float) -> Exercise:
    kind = activity_type.lower()

    if kind == "кардіо":
        return CardioExercise(name, activity_type, met)
    if kind == "розтяжка":
        return FlexibilityExercise(name, activity_type, met)
    if kind == "сила":
        return StrengthExercise(name, activity_type, met)

    return Exercise(name, activity_type, met)
