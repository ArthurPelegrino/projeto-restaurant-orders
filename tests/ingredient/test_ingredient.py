from src.models.ingredient import Ingredient  # noqa: F401, E261, E501
from src.models.ingredient import Restriction  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    presunto = Ingredient("presunto")
    salmão = Ingredient("salmão")

    assert presunto.name == "presunto"
    assert presunto.restrictions == {
        Restriction.ANIMAL_MEAT,
        Restriction.ANIMAL_DERIVED,
    }
    assert presunto.__repr__() == "Ingredient('presunto')"

    assert presunto.__eq__(salmão) is False
    assert presunto.__eq__(presunto) is True

    assert presunto.__hash__() == presunto.__hash__()
    assert presunto.__hash__() != salmão.__hash__()
