from pydantic import BaseModel

from .pokemon import Pokemon


class Item(BaseModel):
    name: str
    healing_power: int

    def heal(self, pokemon: Pokemon):
        pokemon.health_points += self.healing_power
        pokemon.health_points = min(pokemon.health_points, pokemon.max_health_points)
