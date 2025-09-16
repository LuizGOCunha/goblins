from __future__ import annotations
from typing import Literal
from random import randint

from libraries.characters.base_class import Character
from libraries.word_lists import INSULTING_ADJECTIVES, INSULTING_NOUNS
from libraries.dice import d6


class Goblin(Character):
    """Goblin object."""

    name = "G"

    def __init__(self, name: str, x_axis: int = 0, y_axis: int = 0) -> None:
        """Initializing a goblin."""
        super().__init__(name, x_axis, y_axis)
        self.health = 500
        self.damage = 10
        self.gold = 5
        self.aggression = 0

    def act(self) -> None:
        if self.is_dead:
            return

        elif object := self.has_object_in_vicinity("close", Goblin):
            if self.aggression > 100:
                self.attack(object)
            else:
                self.ostracize(object, 3)

        elif object := self.has_object_in_vicinity("mid", Goblin):
            self.ostracize(object, 2)
            self.roam(logging=False)

        elif object := self.has_object_in_vicinity("far", Goblin):
            self.ostracize(object, 1)
            self.roam(logging=False)

        else:
            self.roam()

    def ostracize(self, target: Goblin, aggression_level: Literal[1, 2, 3]) -> None:
        """Elevates the aggression level of a goblin nearby."""
        aggravation = d6() * aggression_level

        target.aggression += aggravation
        print(f"{self} calls {target} a '{INSULTING_ADJECTIVES[randint(0, 34)]} {INSULTING_NOUNS[randint(0, 34)]}'")
