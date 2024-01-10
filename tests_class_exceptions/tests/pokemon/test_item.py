import pytest

from tests_class_exceptions.src.pokemon.item import Item
from tests_class_exceptions.src.pokemon.pokemon import Pokemon


@pytest.fixture
def potion():
    return Item(name="Potion", healing_power=20)


def test_item_creation(potion: Item):
    assert potion.name == "Potion"
    assert potion.healing_power == 20


def test_item_heal(potion: Item):
    pikachu = Pokemon("Pikachu", 8, 6, 50)
    pikachu.health_points -= 26
    potion.heal(pikachu)
    assert pikachu.health_points == 44


def test_item_heal_max_health(potion: Item):
    pikachu = Pokemon("Pikachu", 8, 6, 20)
    pikachu.health_points -= 1
    potion.heal(pikachu)
    assert pikachu.health_points == 20
