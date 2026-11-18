from abc import ABC, abstractmethod


class NutritionItem(ABC):


    @abstractmethod
    def get_name(self) -> str:

        pass

    @abstractmethod
    def get_nutrition(self, amount: float) -> dict:

        pass