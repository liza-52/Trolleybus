class Meal:

    def __init__(self, name: str) -> None:
        if not name or not isinstance(name, str) or not name.strip():
            raise ValueError("Назва прийому їжі не може бути порожньою!")

        self.__name = name.strip()
        self.__items = [] 

    def get_name(self) -> str:
        return self.__name

    def add_item(self, item, weight_grams: float) -> None:
        if item is None:
            raise ValueError("Об'єкт продукту або страви не може бути порожнім!")

        if not hasattr(item, "get_name") or not callable(getattr(item, "get_name")):
            raise TypeError("Об'єкт має реалізовувати метод get_name()!")

        if not hasattr(item, "calculate_nutrition_for_weight") and not hasattr(
            item, "get_nutrition_per_serving"
        ):
            raise TypeError("Об'єкт повинен мати метод розрахунку КБЖВ!")

        if weight_grams <= 0:
            raise ValueError("Вага порції має бути більшою за 0!")

        self.__items.append({"item": item, "weight_grams": float(weight_grams)})

    def remove_item(self, item_name: str) -> bool:
        if not item_name or not isinstance(item_name, str):
            return False

        target_name = item_name.strip().lower()
        for i, entry in enumerate(self.__items):
            if entry["item"].get_name().lower() == target_name:
                self.__items.pop(i)
                return True
        return False

    def get_items_count(self) -> int:
        return len(self.__items)

    def get_items(self) -> list:
 
        return [
            {
                "name": entry["item"].get_name(),
                "weight_grams": entry["weight_grams"],
                "nutrition": self._get_entry_nutrition(entry),
            }
            for entry in self.__items
        ]

    def get_total_nutrition(self) -> dict:
        total = {"calories": 0.0, "protein": 0.0, "fat": 0.0, "carbs": 0.0}

        for entry in self.__items:
            nutrition = self._get_entry_nutrition(entry)
            total["calories"] += nutrition["calories"]
            total["protein"] += nutrition["protein"]
            total["fat"] += nutrition["fat"]
            total["carbs"] += nutrition["carbs"]

        return {
            "calories": round(total["calories"], 2),
            "protein": round(total["protein"], 2),
            "fat": round(total["fat"], 2),
            "carbs": round(total["carbs"], 2),
        }

    def get_total_calories(self) -> float:
        return self.get_total_nutrition()["calories"]

    def _get_entry_nutrition(self, entry: dict) -> dict:
        item = entry["item"]
        weight = entry["weight_grams"]

        if hasattr(item, "calculate_nutrition_for_weight"):
            return item.calculate_nutrition_for_weight(weight)
        elif hasattr(item, "get_nutrition_per_serving"):
            return item.get_nutrition_per_serving(weight)
        else:
            raise TypeError("Невідомий тип елемента прийому їжі!")