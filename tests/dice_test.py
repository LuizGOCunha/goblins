from unittest import TestCase
from libraries.dice import d6, d10, d20


class DiceTest(TestCase):
    """Tests for the dice functions."""

    def test_d6(self):
        d6_list = []
        for _ in range(10000):
            d6_list.append(d6())
        self.assertEqual({1, 2, 3, 4, 5, 6}, set(d6_list))

    def test_d10(self):
        d10_list = []
        for _ in range(10000):
            d10_list.append(d10())
        self.assertEqual({1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, set(d10_list))

    def test_d20(self):
        d20_list = []
        for _ in range(10000):
            d20_list.append(d20())
        self.assertEqual({1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}, set(d20_list))
