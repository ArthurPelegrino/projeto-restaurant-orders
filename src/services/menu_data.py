# import sys
import csv
from src.models.dish import Dish
from src.models.ingredient import Ingredient

# Req 3


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.source_path = source_path
        self.dishes = set()
        self.menu_data(source_path)

    def menu_data(self, source_path):
        with open(source_path, newline="") as file:
            reader = csv.reader(file)
            next(reader)

            dish_dict = {}

            for row in reader:
                dish_name = row[0]
                dish_price = float(row[1])
                ingredient_name = row[2]
                ingredient_amount = int(row[3])

                if dish_name not in dish_dict:
                    dish_dict[dish_name] = Dish(dish_name, dish_price)

                dish_dict[dish_name].add_ingredient_dependency(
                    Ingredient(ingredient_name), ingredient_amount
                )

                self.dishes = set(dish_dict.values())
