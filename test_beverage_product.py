import unittest
from beverage_product import BeverageProduct


class TestBeverageProduct(unittest.TestCase):

    def setUp(self) -> None:
        self.beverage = BeverageProduct(
            name="Milk",
            calories_per_100ml=64.0,
            protein_per_100ml=3.2,
            fat_per_100ml=3.6,
            carbs_per_100ml=4.8,
            is_carbonated=False,
        )

    def test_create_and_getters(self) -> None:
        self.assertEqual(self.beverage.get_name(), "Milk")
        self.assertEqual(self.beverage.get_calories_per_100ml(), 64.0)
        self.assertEqual(self.beverage.get_protein_per_100ml(), 3.2)
        self.assertEqual(self.beverage.get_fat_per_100ml(), 3.6)
        self.assertEqual(self.beverage.get_carbs_per_100ml(), 4.8)
        self.assertFalse(self.beverage.is_carbonated())

    def test_carbonated_flag(self) -> None:
        cola = BeverageProduct("Cola", 42.0, 0.0, 0.0, 10.6, is_carbonated=True)
        self.assertTrue(cola.is_carbonated())

    def test_calculate_nutrition(self) -> None:
        volume_ml = 250.0
        expected_nutrition = {
            "calories": 160.0,
            "protein": 8.0,
            "fat": 9.0,
            "carbs": 12.0,
        }
        self.assertEqual(
            self.beverage.get_nutrition(volume_ml),
            expected_nutrition,
        )

    def test_to_dict(self) -> None:
        expected_dict = {
            "type": "BeverageProduct",
            "name": "Milk",
            "calories_per_100ml": 64.0,
            "protein_per_100ml": 3.2,
            "fat_per_100ml": 3.6,
            "carbs_per_100ml": 4.8,
            "is_carbonated": False,
        }
        self.assertEqual(self.beverage.to_dict(), expected_dict)

    def test_invalid_name_raises_error(self) -> None:
        with self.assertRaises(ValueError):
            BeverageProduct("", 50.0, 1.0, 0.0, 10.0)
        with self.assertRaises(ValueError):
            BeverageProduct("   ", 50.0, 1.0, 0.0, 10.0)

    def test_invalid_macros_raises_error(self) -> None:
        with self.assertRaises(ValueError):
            BeverageProduct("Bad Drink", -10.0, 1.0, 0.0, 5.0)

    def test_invalid_volume_raises_error(self) -> None:
        with self.assertRaises(ValueError):
            self.beverage.get_nutrition(0.0)
        with self.assertRaises(ValueError):
            self.beverage.get_nutrition(-100.0)


if __name__ == "__main__":
    unittest.main()