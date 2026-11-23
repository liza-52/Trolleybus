from nutrition_item import NutritionItem


class FoodProduct(NutritionItem):

    def __init__(
        self,
        name: str,
        calories_per_100g: float,
        protein_per_100g: float,
        fat_per_100g: float,
        carbs_per_100g: float,
    ) -> None:
        if not name or not isinstance(name, str) or not name.strip():
            raise ValueError("Назва продукту не може бути порожньою!")

        if (
            calories_per_100g < 0
            or protein_per_100g < 0
            or fat_per_100g < 0
            or carbs_per_100g < 0
        ):
            raise ValueError("Харчова цінність не може бути від'ємною!")

        self.__name = name.strip()
        self.__calories_per_100g = float(calories_per_100g)
        self.__protein_per_100g = float(protein_per_100g)
        self.__fat_per_100g = float(fat_per_100g)
        self.__carbs_per_100g = float(carbs_per_100g)

    def get_name(self) -> str:
        return self.__name

    def get_calories_per_100g(self) -> float:
        return self.__calories_per_100g

    def get_protein_per_100g(self) -> float:
        return self.__protein_per_100g

    def get_fat_per_100g(self) -> float:
        return self.__fat_per_100g

    def get_carbs_per_100g(self) -> float:
        return self.__carbs_per_100g

    def get_nutrition(self, weight_grams: float) -> dict:
        if weight_grams <= 0:
            raise ValueError("Вага порції має бути більшою за 0!")

        factor = weight_grams / 100.0
        return {
            "calories": round(self.__calories_per_100g * factor, 2),
            "protein": round(self.__protein_per_100g * factor, 2),
            "fat": round(self.__fat_per_100g * factor, 2),
            "carbs": round(self.__carbs_per_100g * factor, 2),
        }

    def to_dict(self) -> dict:
        return {
            "type": "FoodProduct",
            "name": self.get_name(),
            "calories_per_100g": self.__calories_per_100g,
            "protein_per_100g": self.__protein_per_100g,
            "fat_per_100g": self.__fat_per_100g,
            "carbs_per_100g": self.__carbs_per_100g,
        }