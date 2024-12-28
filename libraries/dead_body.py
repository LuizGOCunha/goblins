from typing import Any


class DeadBody:
    """A dead body. TBI"""

    def __init__(self, creature_type: Any):
        from libraries.goblin import Goblin

        if creature_type is Goblin:
            self.pounds_of_meat = 50
        else:
            self.pounds_of_meat = 10

    def __str__(self):
        """Basic representation of a goblin on screen."""
        return "D"
