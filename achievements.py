class Achievement:
    def __init__(self, name: str, description: str, points: int) -> None:
        if not name or not name.strip():
            raise ValueError("Назва досягнення не може бути порожньою!")
        if points < 0:
            raise ValueError("Кількість балів не може бути від'ємною!")

        self.__name = name.strip()
        self.__description = description.strip()
        self.__points = int(points)

    def get_name(self) -> str:
        return self.__name

    def get_description(self) -> str:
        return self.__description

    def get_points(self) -> int:
        return self.__points

    def is_unlocked(self, entry) -> bool:
        raise NotImplementedError("Підклас має реалізувати метод is_unlocked()")

    def to_dict(self) -> dict:
        return {
            "type": self.__class__.__name__,
            "name": self.__name,
            "description": self.__description,
            "points": self.__points,
        }

    def __str__(self) -> str:
        return f"{self.__name} (+{self.__points} балів) — {self.__description}"


class BurnedCaloriesAchievement(Achievement):
    def __init__(self, name: str, min_calories: float, points: int = 50) -> None:
        super().__init__(
            name=name,
            description=f"Спалити щонайменше {min_calories} ккал за день",
            points=points,
        )
        self.__min_calories = float(min_calories)

    def is_unlocked(self, entry) -> bool:
        return entry.get_burned_calories() >= self.__min_calories


class WorkoutCountAchievement(Achievement):
    def __init__(self, name: str, min_workouts: int, points: int = 40) -> None:
        super().__init__(
            name=name,
            description=f"Провести щонайменше {min_workouts} тренувань за день",
            points=points,
        )
        self.__min_workouts = int(min_workouts)

    def is_unlocked(self, entry) -> bool:
        return len(entry.get_workouts()) >= self.__min_workouts


class ProteinGoalAchievement(Achievement):
    def __init__(self, name: str, min_protein_g: float, points: int = 30) -> None:
        super().__init__(
            name=name,
            description=f"Спожити щонайменше {min_protein_g} г білка за день",
            points=points,
        )
        self.__min_protein_g = float(min_protein_g)

    def is_unlocked(self, entry) -> bool:
        return entry.get_consumed_nutrition()["protein"] >= self.__min_protein_g


class CalorieDeficitAchievement(Achievement):
    def __init__(self, name: str, max_balance: float = 0.0, points: int = 60) -> None:
        super().__init__(
            name=name,
            description=f"Утримати денний баланс калорій не вище {max_balance} ккал",
            points=points,
        )
        self.__max_balance = float(max_balance)

    def is_unlocked(self, entry) -> bool:
        return (
            entry.get_consumed_calories() > 0
            and entry.get_daily_balance() <= self.__max_balance
        )
