from unittest import TestCase
from unittest.mock import patch
from random import randint

from libraries.characters.goblin import Goblin


class GoblinTest(TestCase):

    @patch("libraries.characters.base_class.d20", side_effect=lambda: 15)  # Control d20 roll
    @patch("libraries.characters.base_class.d6", side_effect=lambda: 4)  # Control d6 roll
    def test_goblin_attack_when_aggression_high(self, mock_d6, mock_d20):
        # Arrange
        goblin_1 = Goblin("Goblin 1", x_axis=1, y_axis=2)
        goblin_2 = Goblin("Goblin 2", x_axis=1, y_axis=3)
        goblin_1.aggression = 150  # Set aggression above 100 to force an attack

        # Act: Goblin 1 should attack Goblin 2
        goblin_1.act()

        # Assert: Goblin 1 should attack Goblin 2 because aggression > 100
        self.assertEqual(goblin_2.health, 500 - (goblin_1.damage * 4))  # Goblin 2 should take damage

    @patch("libraries.characters.goblin.d6", side_effect=lambda: 2)  # Control d6 roll
    def test_goblin_ostracize_when_aggression_low(self, mock_d6):
        # Arrange
        goblin_1 = Goblin("Goblin 1", x_axis=1, y_axis=2)
        goblin_2 = Goblin("Goblin 2", x_axis=1, y_axis=3)
        goblin_2.aggression = 50  # Set aggression below 100 to trigger ostracize

        # Act: Goblin 1 should ostracize Goblin 2
        goblin_1.act()

        # Assert: Goblin 2's aggression should increase due to ostracize
        self.assertEqual(goblin_2.aggression, 50 + (2 * 3))  # Aggression should increase by d6 * 3

    @patch("libraries.characters.goblin.d6", side_effect=lambda: 3)  # Control d6 roll
    def test_goblin_ostracize_action(self, mock_d6):
        # Arrange
        goblin_1 = Goblin("Goblin 1", x_axis=1, y_axis=2)
        goblin_2 = Goblin("Goblin 2", x_axis=1, y_axis=3)

        # Act: Goblin 1 ostracizes Goblin 2 at aggression level 1
        goblin_1.ostracize(goblin_2, aggression_level=1)

        # Assert: Goblin 2's aggression should increase by d6 * 1
        self.assertEqual(goblin_2.aggression, 3)  # Aggression should increase by 3

    @patch("libraries.characters.base_class.randint", side_effect=lambda x, y: 3)
    def test_roam_moves_goblin(self, mock_randint):
        # Test the case when the randint produces a value between 0 and 3 (goblin moves)
        mock_randint.return_value = 3  # Within the range [0, 3], should trigger move

        goblin = Goblin("Goblin1", 0, 0)
        initial_x, initial_y = goblin.x_axis, goblin.y_axis  # Save initial coordinates
        goblin.roam(logging=False)  # Disable logging for cleaner output in tests

        # Ensure that the goblin has moved (coordinates should change)
        self.assertNotEqual((goblin.x_axis, goblin.y_axis), (initial_x, initial_y))

    @patch("libraries.characters.base_class.randint", side_effect=lambda x, y: 5)
    def test_roam_does_not_move(self, mock_randint):
        # Test the case when the randint produces a value between 4 and 6 (goblin does not move)

        goblin = Goblin("Goblin1", 0, 0)
        initial_x, initial_y = goblin.x_axis, goblin.y_axis  # Save initial coordinates
        goblin.roam(logging=False)

        # Ensure that the goblin has not moved (coordinates should stay the same)
        self.assertEqual((goblin.x_axis, goblin.y_axis), (initial_x, initial_y))

    @patch("libraries.characters.goblin.d6", side_effect=lambda: 6)  # Max d6 roll
    def test_goblin_aggression_increases_on_ostracize(self, mock_d6):
        # Arrange
        goblin_1 = Goblin("Goblin 1", x_axis=1, y_axis=2)
        goblin_2 = Goblin("Goblin 2", x_axis=1, y_axis=3)

        # Act: Goblin 1 ostracizes Goblin 2 with aggression level 2
        goblin_1.ostracize(goblin_2, aggression_level=2)

        # Assert: Goblin 2's aggression should increase by 6 (d6) * 2
        self.assertEqual(goblin_2.aggression, 12)
