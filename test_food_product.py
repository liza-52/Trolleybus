import unittest
from food_product import FoodProduct


class TestFoodProduct(unittest.TestCase):

    def setUp(self) -> None:
        self.product = FoodProduct(
            name="Banana",
            calories_per_100g=89.0,
            protein_per_100g=1.1,
            fat_per_100g=0.3,
            carbs_per_100g=22.8,
        )

    def test_create_and_getters(self) -> None:
        self.assertEqual(self.product.get_name(), "Banana")
        self.assertEqual(self.product.get_calories_per_100g(), 89.0)
        self.assertEqual(self.product.get_protein_per_100g(), 1.1)
        self.assertEqual(self.product.get_fat_per_100g(), 0.3)
        self.assertEqual(self.product.get_carbs_per_100g(), 22.8)

    def test_calculate_nutrition(self) -> None:
        weight = 150.0
        expected_nutrition = {
            "calories": 133.5,
            "protein": 1.65,
            "fat": 0.45,
            "carbs": 34.2,
        }
        self.assertEqual(
            self.product.calculate_nutrition_for_weight(weight),
            expected_nutrition,
        )

    def test_invalid_weight(self) -> None:
        with self.assertRaises(ValueError):
            self.product.calculate_nutrition_for_weight(-50.0)


if __name__ == "__main__":
    unittest.main()