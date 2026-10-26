import unittest
from food_product import FoodProduct
from dish import Dish
from meal import Meal


class TestMeal(unittest.TestCase):

    def setUp(self) -> None:
        self.meal = Meal("Сніданок")

        self.banana = FoodProduct(
            name="Банан",
            calories_per_100g=89.0,
            protein_per_100g=1.1,
            fat_per_100g=0.3,
            carbs_per_100g=22.8,
        )

        self.omelet = Dish(
            name="Омлет",
            total_weight_grams=200.0,
            total_calories=300.0,
            total_protein=20.0,
            total_fat=22.0,
            total_carbs=4.0,
        )

    def test_init_valid_name(self) -> None:
        self.assertEqual(self.meal.get_name(), "Сніданок")

    def test_init_invalid_name(self) -> None:
        with self.assertRaises(ValueError):
            Meal("")
        with self.assertRaises(ValueError):
            Meal("   ")

    def test_add_item_valid(self) -> None:
        self.meal.add_item(self.banana, 150.0)
        self.assertEqual(self.meal.get_items_count(), 1)

        self.meal.add_item(self.omelet, 100.0)
        self.assertEqual(self.meal.get_items_count(), 2)

    def test_add_item_invalid_weight(self) -> None:
        with self.assertRaises(ValueError):
            self.meal.add_item(self.banana, -10.0)
        with self.assertRaises(ValueError):
            self.meal.add_item(self.banana, 0.0)

    def test_add_item_invalid_object(self) -> None:
        with self.assertRaises(ValueError):
            self.meal.add_item(None, 100.0)
        with self.assertRaises(TypeError):
            self.meal.add_item("не об'єкт", 100.0)

    def test_remove_item(self) -> None:
        self.meal.add_item(self.banana, 150.0)
        self.meal.add_item(self.omelet, 100.0)

        removed = self.meal.remove_item("Банан")
        self.assertTrue(removed)
        self.assertEqual(self.meal.get_items_count(), 1)

        removed_again = self.meal.remove_item("Яблуко")
        self.assertFalse(removed_again)
        self.assertEqual(self.meal.get_items_count(), 1)

    def test_empty_meal_nutrition(self) -> None:
        expected = {"calories": 0.0, "protein": 0.0, "fat": 0.0, "carbs": 0.0}
        self.assertEqual(self.meal.get_total_nutrition(), expected)
        self.assertEqual(self.meal.get_total_calories(), 0.0)

    def test_total_nutrition_calculation(self) -> None:
        # Банан 150г + Омлет 100г
        self.meal.add_item(self.banana, 150.0)
        self.meal.add_item(self.omelet, 100.0)

        expected_total = {
            "calories": 283.5,  # 133.5 + 150.0
            "protein": 11.65,   # 1.65 + 10.0
            "fat": 11.45,       # 0.45 + 11.0
            "carbs": 36.2,      # 34.2 + 2.0
        }

        self.assertEqual(self.meal.get_total_nutrition(), expected_total)
        self.assertEqual(self.meal.get_total_calories(), 283.5)


if __name__ == "__main__":
    unittest.main()