from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Restriction  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient  # noqa: F401, E261, E501
import pytest


# Req 2
def test_dish():
    myDish = Dish("Prato do Arthur", 25.00)
    myDish2 = Dish("Prato do Arthur2", 30.00)

    assert myDish.name == "Prato do Arthur"

    myDish.add_ingredient_dependency(Ingredient("presunto"), 2)

    assert myDish.get_ingredients() == {Ingredient("presunto")}

    assert (hash(myDish) == hash(myDish2)) is False
    assert (hash(myDish) == hash(myDish)) is True

    assert myDish.__eq__(myDish2) is False
    assert myDish.__eq__(myDish) is True

    assert str(myDish) == "Dish('Prato do Arthur', R$25.00)"

    assert myDish.get_restrictions() == {
        Restriction.ANIMAL_MEAT,
        Restriction.ANIMAL_DERIVED,
    }

    with pytest.raises(TypeError, match="Dish price must be float."):
        Dish("a", "a")
    valueError = "Dish price must be greater then zero."
    with pytest.raises(ValueError, match=valueError):
        Dish("a", -1)
