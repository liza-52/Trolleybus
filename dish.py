from nutrition_item import NutritionItem


class Dish(NutritionItem):

    def __init__(
        self,
        name: str,
        total_weight_grams: float,
        total_calories: float,
        total_protein: float,
        total_fat: float,
        total_carbs: float,
    ) -> None:
        if not name or not isinstance(name, str) or not name.strip():
            raise ValueError("Назва страви не може бути порожньою!")

        if total_weight_grams <= 0:
            raise ValueError("Загальна вага страви має бути більшою за 0!")

        if (
            total_calories < 0
            or total_protein < 0
            or total_fat < 0
            or total_carbs < 0
        ):
            raise ValueError("Харчова цінність не може бути від'ємною!")

        self.__name = name.strip()
        self.__total_weight_grams = float(total_weight_grams)
        self.__total_calories = float(total_calories)
        self.__total_protein = float(total_protein)
        self.__total_fat = float(total_fat)
        self.__total_carbs = float(total_carbs)

    def get_name(self) -> str:
        return self.__name

    def get_total_weight_grams(self) -> float:
        return self.__total_weight_grams

    def get_macro_ratios(self) -> dict:
        """Обчислює відсоткове співвідношення БЖВ у страві."""
        total_macros = self.__total_protein + self.__total_fat + self.__total_carbs
        if total_macros == 0:
            return {"protein": 0.0, "fat": 0.0, "carbs": 0.0}

        return {
            "protein": round((self.__total_protein / total_macros) * 100, 2),
            "fat": round((self.__total_fat / total_macros) * 100, 2),
            "carbs": round((self.__total_carbs / total_macros) * 100, 2),
        }

    def get_nutrition(self, serving_weight_grams: float) -> dict:

        if serving_weight_grams <= 0:
            raise ValueError("Вага порції має бути більшою за 0!")

        factor = serving_weight_grams / self.__total_weight_grams
        return {
            "calories": round(self.__total_calories * factor, 2),
            "protein": round(self.__total_protein * factor, 2),
            "fat": round(self.__total_fat * factor, 2),
            "carbs": round(self.__total_carbs * factor, 2),
        }