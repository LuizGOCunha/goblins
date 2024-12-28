from __future__ import annotations
from typing import Literal, Any
from random import randint

from libraries.map import MAP
from libraries.dice import d6, d20
from libraries.dead_body import DeadBody


class Goblin:
    """Goblin object."""

    map = MAP
    name = "G"

    def __init__(self, name: str, x_axis: int = 0, y_axis: int = 0) -> None:
        """Initializing a goblin."""
        self.name = name
        self.health = 500
        self.damage = 10
        self.gold = 5
        self.x_axis, self.y_axis = x_axis, y_axis
        self.add_self_to_coordinates()
        self.being_attacked_by = []

    def add_self_to_coordinates(self) -> None:
        """Use our own coordinates to insert ourselves in the map."""
        return self.map.add_object_in_position(self, self.x_axis, self.y_axis)

    def remove_self_from_coordinates(self) -> None:
        """Remove object located on our own coordinates."""
        return self.map.empty_position(self.x_axis, self.y_axis)

    def add_object_to_my_coordinates(self, object: Any) -> None:
        """Adds a given object to our position."""
        return self.map.add_object_in_position(object, self.x_axis, self.y_axis)

    def act(self):
        if self.is_dead:
            return

        if object := self.has_object_in_vicinity("close", Goblin):
            self.attack(object)
        else:
            self.roam()

    @property
    def is_dead(self):
        return self.health <= 0

    @property
    def far_surroundings(self):
        """Return the far surrounding (7x7) coordenates for a character."""
        return self.map.validate_coordinates(
            [(self.x_axis + i, self.y_axis + ii) for i in range(-3, 4) for ii in range(-3, 4)]
        )

    @property
    def surroundings(self):
        """Return the surrounding (5x5) coordenates for a character."""
        return self.map.validate_coordinates(
            [(self.x_axis + i, self.y_axis + ii) for i in range(-2, 3) for ii in range(-2, 3)]
        )

    @property
    def close_surroundings(self):
        """Return the close surrounding (3x3) coordenates for a character."""
        return self.map.validate_coordinates(
            [(self.x_axis + i, self.y_axis + ii) for i in range(-1, 2) for ii in range(-1, 2)]
        )

    def has_object_in_vicinity(self, vicinity: Literal["close", "mid", "far"], type: type) -> Any | None:
        """Checks if there is an object in the vicinity of the goblin, returns the first one."""
        match vicinity:
            case "close":
                vicinity_coord = self.close_surroundings
            case "mid":
                vicinity_coord = self.surroundings
            case "far":
                vicinity_coord = self.far_surroundings

        # TODO: add something that returns the coordenates in order of closeness

        for x, y in vicinity_coord:
            area_object = self.map.get_object_in_position(x, y)
            if isinstance(area_object, type) and area_object is not self:
                return area_object

    def attack(self, target: Goblin) -> None:
        if self not in target.being_attacked_by:
            target.being_attacked_by.append(self)

        self._damage_target(target)

        if target.is_dead:
            target.add_object_to_my_coordinates(DeadBody(type(target)))

    def _damage_target(self, target: Goblin) -> None:
        """Damages target and logs the result."""
        damage, is_crit = self._calculate_damage()

        if damage is None:
            print(f"{self} tries to cleave {target} but misses.")
            return
        elif is_crit:
            print(f"{self} stabs {target} on his side. The wound is deep. <{damage} DAMAGE>")
        else:
            print(f"{self} slices into {target}, blood is flowing. <{damage} DAMAGE>")

        target.health -= damage

    def _calculate_damage(self) -> tuple[None | int, bool]:
        """Calculates the damage that will be given to the target."""
        accuracy = d20()
        damage = self.damage
        if accuracy == 20:
            # TODO: substitute the d6 with a weapon based roll
            return damage * 2 * d6(), True
        # TODO: add accuracy stat, will substitute the '10' bellow
        elif accuracy < 10:
            return None, False
        else:
            return damage * d6(), False

    def roam(self) -> None:
        """Roam aimlessly throughout the map, with a chance of not moving at all"""
        print(f"Goblin {self} is roaming...")
        direction_int = randint(0, 6)
        # Here we have a chance of not moving since the int can also be 4, 5 or 6
        if 0 <= direction_int < 4:
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

    def __str__(self):
        """Basic representation of a goblin on screen."""
        return self.name
