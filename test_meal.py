import unittest
from food_product import FoodProduct
from dish import Dish
from beverage_product import BeverageProduct
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

        self.milk = BeverageProduct(
            name="Молоко",
            calories_per_100ml=64.0,
            protein_per_100ml=3.2,
            fat_per_100ml=3.6,
            carbs_per_100ml=4.8,
            is_carbonated=False,
        )

    def test_init_valid_name(self) -> None:
        self.assertEqual(self.meal.get_name(), "Сніданок")

    def test_init_invalid_name(self) -> None:
        with self.assertRaises(ValueError):
            Meal("")
        with self.assertRaises(ValueError):
            Meal("   ")

    def test_add_item_polymorphic_subclasses(self) -> None:
        self.meal.add_item(self.banana, 150.0)
        self.meal.add_item(self.omelet, 100.0)
        self.meal.add_item(self.milk, 200.0)
        self.assertEqual(self.meal.get_items_count(), 3)

    def test_add_item_invalid_type_not_nutrition_item(self) -> None:
        class InvalidItem:
            pass

        with self.assertRaises(TypeError):
            self.meal.add_item("рядок замість об'єкта", 100.0)
        with self.assertRaises(TypeError):
            self.meal.add_item(InvalidItem(), 100.0)

    def test_add_item_invalid_weight(self) -> None:
        with self.assertRaises(ValueError):
            self.meal.add_item(self.banana, -10.0)
        with self.assertRaises(ValueError):
            self.meal.add_item(self.banana, 0.0)

    def test_remove_item(self) -> None:
        self.meal.add_item(self.banana, 150.0)
        self.meal.add_item(self.omelet, 100.0)

        removed = self.meal.remove_item("Банан")
        self.assertTrue(removed)
        self.assertEqual(self.meal.get_items_count(), 1)

        removed_again = self.meal.remove_item("Яблуко")
        self.assertFalse(removed_again)
        self.assertEqual(self.meal.get_items_count(), 1)

    def test_search_items_by_name(self) -> None:
        self.meal.add_item(self.banana, 150.0)
        self.meal.add_item(self.omelet, 100.0)
        self.meal.add_item(self.milk, 200.0)

        results = self.meal.search_items_by_name("бан")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["name"], "Банан")

        empty_results = self.meal.search_items_by_name("кава")
        self.assertEqual(len(empty_results), 0)

    def test_get_sorted_items_by_calories(self) -> None:
        self.meal.add_item(self.banana, 150.0)
        self.meal.add_item(self.omelet, 100.0)
        self.meal.add_item(self.milk, 200.0)

        sorted_desc = self.meal.get_sorted_items_by_calories(reverse=True)
        self.assertEqual(sorted_desc[0]["name"], "Омлет")    # 150.0 ккал
        self.assertEqual(sorted_desc[1]["name"], "Банан")    # 133.5 ккал
        self.assertEqual(sorted_desc[2]["name"], "Молоко")   # 128.0 ккал

    def test_total_nutrition_polymorphic_calculation(self) -> None:
        self.meal.add_item(self.banana, 150.0)
        self.meal.add_item(self.omelet, 100.0)
        self.meal.add_item(self.milk, 200.0)

        expected_calories = 411.5
        self.assertEqual(self.meal.get_total_calories(), expected_calories)


if __name__ == "__main__":
    unittest.main()