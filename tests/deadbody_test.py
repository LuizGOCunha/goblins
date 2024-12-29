import unittest

from libraries.characters.goblin import Goblin
from libraries.characters.base_class import Character
from libraries.dead_body import DeadBody


class TestDeadBody(unittest.TestCase):
    def test_initializes_with_50_pounds_for_goblin(self):
        body = DeadBody(Goblin)
        self.assertEqual(body.pounds_of_meat, 50)

    def test_initializes_with_10_pounds_for_character(self):
        body = DeadBody(Character)
        self.assertEqual(body.pounds_of_meat, 10)

    def test_initializes_with_0_pounds_for_unknown_type(self):
        class UnknownCreature:
            pass

        body = DeadBody(UnknownCreature)
        self.assertEqual(body.pounds_of_meat, 0)

    def test_is_depleted_returns_true_when_meat_is_zero(self):
        body = DeadBody(Character)
        body.pounds_of_meat = 0
        self.assertTrue(body.is_depleted)

    def test_is_depleted_returns_false_when_meat_is_nonzero(self):
        body = DeadBody(Goblin)
        self.assertFalse(body.is_depleted)

    def test_str_representation(self):
        body = DeadBody(Goblin)
        self.assertEqual(str(body), "D")


if __name__ == "__main__":
    unittest.main()
