import unittest
from dish import Dish


class TestDish(unittest.TestCase):

    def setUp(self) -> None:
        self.dish = Dish(
            name="Omelet",
            total_weight_grams=200.0,
            total_calories=300.0,
            total_protein=20.0,
            total_fat=20.0,
            total_carbs=10.0,
        )

    def test_getters_and_creation(self) -> None:
        self.assertEqual(self.dish.get_name(), "Omelet")
        self.assertEqual(self.dish.get_total_weight_grams(), 200.0)
        self.assertEqual(self.dish.get_total_calories(), 300.0)
        self.assertEqual(self.dish.get_total_protein(), 20.0)
        self.assertEqual(self.dish.get_total_fat(), 20.0)
        self.assertEqual(self.dish.get_total_carbs(), 10.0)

    def test_calories_per_100g(self) -> None:
        self.assertEqual(self.dish.get_calories_per_100g(), 150.0)

    def test_nutrition_per_serving(self) -> None:
        expected = {
            "calories": 150.0,
            "protein": 10.0,
            "fat": 10.0,
            "carbs": 5.0,
        }
        self.assertEqual(self.dish.get_nutrition_per_serving(100.0), expected)

    def test_macro_ratios(self) -> None:
        ratios = self.dish.get_macro_ratios()
        self.assertEqual(ratios["protein"], 40.0)
        self.assertEqual(ratios["fat"], 40.0)
        self.assertEqual(ratios["carbs"], 20.0)

    def test_invalid_weight_raises_error(self) -> None:
        with self.assertRaises(ValueError):
            Dish("Invalid Dish", 0.0, 100.0, 5.0, 5.0, 10.0)

    def test_invalid_macros_raises_error(self) -> None:
        with self.assertRaises(ValueError):
            Dish("Magic Dish", 100.0, 100.0, -5.0, 5.0, 10.0)

    def test_invalid_serving_weight_raises_error(self) -> None:
        with self.assertRaises(ValueError):
            self.dish.get_nutrition_per_serving(-50.0)

    def test_macro_ratios_with_zero_macros(self) -> None:
        water = Dish("Water", 500.0, 0.0, 0.0, 0.0, 0.0)
        ratios = water.get_macro_ratios()
        self.assertEqual(ratios["protein"], 0.0)
        self.assertEqual(ratios["fat"], 0.0)
        self.assertEqual(ratios["carbs"], 0.0)


if __name__ == "__main__":
    unittest.main()