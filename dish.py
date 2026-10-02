class Dish:

    def __init__(
        self,
        name: str,
        total_weight_grams: float,
        total_calories: float,
        total_protein: float,
        total_fat: float,
        total_carbs: float,) -> None:
        
        if total_weight_grams <= 0:
            raise ValueError("Загальна вага страви менша за 0")

        if (
            total_calories < 0
            or total_protein < 0
            or total_fat < 0
            or total_carbs < 0
        ):
            raise ValueError("Від'ємне значення КБЖВ")

        self.__name = name
        self.__total_weight_grams = float(total_weight_grams)
        self.__total_calories = float(total_calories)
        self.__total_protein = float(total_protein)
        self.__total_fat = float(total_fat)
        self.__total_carbs = float(total_carbs)

   
    def get_name(self) -> str:
        return self.__name

    def get_total_weight_grams(self) -> float:
        return self.__total_weight_grams

    def get_total_calories(self) -> float:
        return self.__total_calories

    def get_total_protein(self) -> float:
        return self.__total_protein

    def get_total_fat(self) -> float:
        return self.__total_fat

    def get_total_carbs(self) -> float:
        return self.__total_carbs


    def get_calories_per_100g(self) -> float:
        return round((self.__total_calories / self.__total_weight_grams) * 100.0, 2)

    def get_nutrition_per_serving(self, serving_weight_grams: float) -> dict:
        if serving_weight_grams <= 0:
            raise ValueError("Вага порції менша за 0")

        coefficient = serving_weight_grams / self.__total_weight_grams
        return {
            "calories": round(self.__total_calories * coefficient, 2),
            "protein": round(self.__total_protein * coefficient, 2),
            "fat": round(self.__total_fat * coefficient, 2),
            "carbs": round(self.__total_carbs * coefficient, 2),
        }

    def get_macro_ratios(self) -> dict:
        total_macros = self.__total_protein + self.__total_fat + self.__total_carbs
        if total_macros == 0:
            return {"protein": 0.0, "fat": 0.0, "carbs": 0.0}

        return {
            "protein": round((self.__total_protein / total_macros) * 100, 1),
            "fat": round((self.__total_fat / total_macros) * 100, 1),
            "carbs": round((self.__total_carbs / total_macros) * 100, 1),
        }