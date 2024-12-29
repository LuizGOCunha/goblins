from typing import Any


class DeadBody:
    """A dead body. TBI"""

    def __init__(self, creature_type: Any):
        from libraries.characters.goblin import Goblin
        from libraries.characters.base_class import Character

        if creature_type is Goblin:
            self.pounds_of_meat = 50
        elif creature_type is Character:
            self.pounds_of_meat = 10
        else:
            self.pounds_of_meat = 0

    @property
    def is_depleted(self):
        """Checks if the amount of meat in a corpse is depleted."""
        return self.pounds_of_meat <= 0

    def __str__(self):
        """Basic representation of a goblin on screen."""
        return "D"
