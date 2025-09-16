from unittest import TestCase

from libraries.items.base_class import Item
from libraries.inventory import Inventory

class InventoryTest(TestCase):

    def test_adding_item_to_inventory(self):
        item = Item()
        inventory = Inventory()

        inventory.add_item(item)
        assert item is inventory.contents[0]