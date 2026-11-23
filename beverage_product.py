from nutrition_item import NutritionItem


class BeverageProduct(NutritionItem):

    def __init__(
        self,
        name: str,
        calories_per_100ml: float,
        protein_per_100ml: float,
        fat_per_100ml: float,
        carbs_per_100ml: float,
        is_carbonated: bool = False,
    ) -> None:
        if not name or not isinstance(name, str) or not name.strip():
            raise ValueError("Назва напою не може бути порожньою!")

        if (
            calories_per_100ml < 0
            or protein_per_100ml < 0
            or fat_per_100ml < 0
            or carbs_per_100ml < 0
        ):
            raise ValueError("Харчова цінність напою не може бути від'ємною!")

        self.__name = name.strip()
        self.__calories_per_100ml = float(calories_per_100ml)
        self.__protein_per_100ml = float(protein_per_100ml)
        self.__fat_per_100ml = float(fat_per_100ml)
        self.__carbs_per_100ml = float(carbs_per_100ml)
        self.__is_carbonated = bool(is_carbonated)

    def get_name(self) -> str:
        return self.__name

    def is_carbonated(self) -> bool:
        return self.__is_carbonated

    def get_calories_per_100ml(self) -> float:
        return self.__calories_per_100ml

    def get_protein_per_100ml(self) -> float:
        return self.__protein_per_100ml

    def get_fat_per_100ml(self) -> float:
        return self.__fat_per_100ml

    def get_carbs_per_100ml(self) -> float:
        return self.__carbs_per_100ml

    def get_nutrition(self, volume_ml: float) -> dict:
        if volume_ml <= 0:
            raise ValueError("Об'єм напою має бути більшим за 0 ml!")

        factor = volume_ml / 100.0
        return {
            "calories": round(self.__calories_per_100ml * factor, 2),
            "protein": round(self.__protein_per_100ml * factor, 2),
            "fat": round(self.__fat_per_100ml * factor, 2),
            "carbs": round(self.__carbs_per_100ml * factor, 2),
        }

    def to_dict(self) -> dict:
        return {
            "type": "BeverageProduct",
            "name": self.get_name(),
            "calories_per_100ml": self.__calories_per_100ml,
            "protein_per_100ml": self.__protein_per_100ml,
            "fat_per_100ml": self.__fat_per_100ml,
            "carbs_per_100ml": self.__carbs_per_100ml,
            "is_carbonated": self.__is_carbonated,
        }