class Exercise:

    def __init__(
        self,
        name: str,
        activity_type: str,
        met: float,
    ) -> None:

        if met <= 0:
            raise ValueError("Значення MET повинно бути додатним!")

        self.__name: str = name
        self.__activity_type: str = activity_type
        self.__met: float = float(met)

    def get_name(self) -> str:
        return self.__name

    def get_activity_type(self) -> str:
        return self.__activity_type

    def get_met(self) -> float:
        return self.__met

    def calculate_calories(self, weight_kg: float, duration_min: float) -> dict:
        if weight_kg <= 0:
            raise ValueError("Вага людини повинна бути більше 0!")

        if duration_min <= 0:
            raise ValueError("Тривалість тренування повинна бути більше 0!")

        hours = duration_min / 60.0
        calories = round(self.__met * weight_kg * hours, 2)

        return {
            "activity": self.__name,
            "type": self.__activity_type,
            "duration_min": duration_min,
            "calories": calories,
        }

    def to_dict(self) -> dict:
        return {"activity_type": self.__activity_type, "met": self.__met}

    def __str__(self) -> str:
        return f"{self.__name} ({self.__activity_type}, MET={self.__met})"
