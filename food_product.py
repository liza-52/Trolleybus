class food:

    def __init__(
        self,
        name: str,
        calories_per_100g: float,
        protein_per_100g: float,
        fat_per_100g: float,
        carbs_per_100g: float,
    ) -> None:
     
        if (
            calories_per_100g < 0
            or protein_per_100g < 0
            or fat_per_100g < 0
            or carbs_per_100g < 0
        ):
            raise ValueError("Від'ємне значення КБЖВ !")

        
        self.__name: str = name
        self.__calories_per_100g: float = float(calories_per_100g)
        self.__protein_per_100g: float = float(protein_per_100g)
        self.__fat_per_100g: float = float(fat_per_100g)
        self.__carbs_per_100g: float = float(carbs_per_100g)


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

    
    def calculate_nutrition_for_weight(self, weight_grams: float) -> dict:
        if weight_grams <= 0:
            raise ValueError("Вага порції менша за 0!")

        coeff = weight_grams / 100.0
        return {
            "calories": round(self.__calories_per_100g * coeff, 2),
            "protein": round(self.__protein_per_100g * coeff, 2),
            "fat": round(self.__fat_per_100g * coeff, 2),
            "carbs": round(self.__carbs_per_100g * coeff, 2),
        }