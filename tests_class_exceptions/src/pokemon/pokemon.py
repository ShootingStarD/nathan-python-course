from __future__ import annotations


class Pokemon:
    name: str
    attack: int
    defense: int
    max_health_points: int
    health_points: int

    def __init__(self, name, attack, defense, max_health_points):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.health_points = max_health_points
        self.max_health_points = max_health_points

    def damage(self, target: Pokemon):
        """
        Damage another Pokemon.

        Damage output is calculated by subtracting target's defence from the attacking Pokemon's attack.
        Target's health is then reduced by this amount.

        Parameters
        ----------
        target : Pokemon on which we will inflict damage
        """
        damage_output = self.attack - target.defense
        damage_output = max(damage_output, 1)
        target.health_points -= damage_output
