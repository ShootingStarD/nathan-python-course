from tests_class_exceptions.src.pokemon.pokemon import Pokemon


def test_damage_pokemon():
    salameche = Pokemon("Salamèche", 12, 8, 20)
    bulbizarre = Pokemon("Bulbi", 10, 10, 22)
    salameche.damage(bulbizarre)
    assert bulbizarre.health_points == 20


def test_always_inflict_at_least_1hp():
    salameche = Pokemon("Salamèche", 12, 8, 20)
    bulbizarre = Pokemon("Bulbi", 10, 14, 22)
    salameche.damage(bulbizarre)
    assert bulbizarre.health_points == 21
