"""Contains Inventory class."""

from libraries.items.base_class import Item

class Inventory:
    """Inventory object for holding and manipulating items."""
    def __init__(self, *args) -> None:
        """Initializing Inventory class."""
        self.contents = list(args)

    def add_item(self, item: Item) -> None:
        self.contents.append(item)