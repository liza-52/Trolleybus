from exercise import Exercise


class CardioExercise(Exercise):

    def get_advice(self) -> str:
        return "Стежте за пульсом і пийте воду."


class FlexibilityExercise(Exercise):

    def get_advice(self) -> str:
        return "Робіть після основної частини, без ривків."


class StrengthExercise(Exercise):

    AFTERBURN = 1.1

    def calculate_calories(self, weight_kg: float, duration_min: float) -> dict:
        result = super().calculate_calories(weight_kg, duration_min)
        result["calories"] = round(result["calories"] * self.AFTERBURN, 2)
        return result

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
