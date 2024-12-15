from typing import Literal
from random import randint

from libraries.map import MAP


class Goblin:
    """Goblin object."""

    map = MAP
    name = "G"

    def __init__(self, name: str, x_axis: int = 0, y_axis: int = 0) -> None:
        """Initializing a goblin."""
        self.name = name
        self.health = 100
        self.attack = 10
        self.gold = 5
        self.x_axis, self.y_axis = x_axis, y_axis
        self.add_self_to_coordinates()

    def add_self_to_coordinates(self) -> None:
        """Use our own coordinates to insert ourselves in the map."""
        return self.map.add_object_in_position(self, self.x_axis, self.y_axis)

    def remove_self_from_coordinates(self) -> None:
        """Remove object located on our own coordinates."""
        return self.map.empty_position(self.x_axis, self.y_axis)

    def act(self):
        if False:
            pass
        else:
            self.roam()

    @property
    def surroundings(self):
        """Return the surrounding coordenates for a character."""
        return self.map.validate_coordinates(
            [(self.x_axis + i, self.y_axis + ii) for i in range(-1, 2) for ii in range(-1, 2)]
        )

    def roam(self) -> None:
        """Roam aimlessly throughout the map."""
        direction_int = randint(0, 3)
        self.move(direction_int)

    def move(self, direction: Literal["up", "down", "left", "right"] | Literal[0, 1, 2, 3]) -> None:
        """Logic for movement within the grid."""
        if isinstance(direction, int):
            if direction < 0 or direction > 3:
                raise ValueError("Direction int outside of allowed range")
            direction = ["up", "down", "left", "right"][direction]

        match direction:
            case "up":
                new_y = self.y_axis + 1
                object_in_new_position = self.map.get_object_in_position(self.x_axis, new_y)
                if object_in_new_position is None:
                    self.remove_self_from_coordinates()
                    self.y_axis = new_y
                    self.add_self_to_coordinates()
            case "down":
                new_y = self.y_axis - 1
                object_in_new_position = self.map.get_object_in_position(self.x_axis, new_y)
                if object_in_new_position is None:
                    self.remove_self_from_coordinates()
                    self.y_axis = new_y
                    self.add_self_to_coordinates()
            case "left":
                new_x = self.x_axis - 1
                object_in_new_position = self.map.get_object_in_position(new_x, self.y_axis)
                if object_in_new_position is None:
                    self.remove_self_from_coordinates()
                    self.x_axis = new_x
                    self.add_self_to_coordinates()
            case "right":
                new_x = self.x_axis + 1
                object_in_new_position = self.map.get_object_in_position(new_x, self.y_axis)
                if object_in_new_position is None:
                    self.remove_self_from_coordinates()
                    self.x_axis = new_x
                    self.add_self_to_coordinates()
            case _:
                raise ValueError("Invalid direction.")
        print((self.x_axis, self.y_axis))

    def __str__(self):
        """Basic representation of a goblin on screen."""
        return self.name
