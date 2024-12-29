from libraries.characters.base_class import Character


class Goblin(Character):
    """Goblin object."""

    name = "G"

    def __init__(self, name: str, x_axis: int = 0, y_axis: int = 0) -> None:
        """Initializing a goblin."""
        super().__init__(name, x_axis, y_axis)
        self.health = 500
        self.damage = 10
        self.gold = 5
