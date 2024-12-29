from unittest.mock import patch
from unittest import TestCase

from libraries.map import MAP
from libraries.characters.base_class import Character
from libraries.dead_body import DeadBody


class CharacterTest(TestCase):
    MAP = MAP

    def setUp(self):
        """Setup method to initialize the environment for each test."""
        self.MAP.grid = [[None for _ in range(self.MAP.X_SIZE)] for _ in range(self.MAP.Y_SIZE)]

    @patch("libraries.characters.base_class.d20", side_effect=lambda: 5)  # Simulate a miss (d20 < 10)
    def test_character_attack_miss(self, mock_d20):
        """Test that a character attack can miss."""
        attacker = Character("Hero", x_axis=2, y_axis=3)
        target = Character("Goblin", x_axis=2, y_axis=4)
        target.health = 30  # Set initial health for the target
        attacker.damage = 10  # Set initial damage for the attacker

        attacker.attack(target)

        # Check that the target's health did not change (since the attack missed)
        self.assertEqual(target.health, 30)
        self.assertNotIsInstance(self.MAP.get_object_in_position(2, 4), DeadBody)

    @patch("libraries.characters.base_class.d20", side_effect=lambda: 15)  # Simulate a normal hit (d20 >= 10)
    @patch("libraries.characters.base_class.d6", side_effect=lambda: 1)  # Simulate a hit of 1 (total damage = 10)
    def test_character_attack_normal_hit(self, mock_d20, mock_d6):
        """Test that a character attack hits with normal damage."""
        attacker = Character("Hero", x_axis=2, y_axis=3)
        target = Character("Goblin", x_axis=2, y_axis=4)
        target.health = 30
        attacker.damage = 10

        attacker.attack(target)

        # Check that the target's health decreased
        self.assertLess(target.health, 30)
        # self.assertGreater(target.health, 20)  # Normal damage would reduce health by some value
        self.assertNotIsInstance(self.MAP.get_object_in_position(2, 4), DeadBody)

    @patch("libraries.characters.base_class.d20", side_effect=lambda: 20)  # Simulate a critical hit (d20 == 20)
    @patch("libraries.characters.base_class.d6", side_effect=lambda: 4)  # Simulate d6 roll for critical hit damage
    def test_character_attack_critical_hit(self, mock_d20, mock_d6):
        """Test that a character attack results in a critical hit."""
        attacker = Character("Hero", x_axis=2, y_axis=3)
        target = Character("Goblin", x_axis=2, y_axis=4)
        target.health = 30
        attacker.damage = 10

        attacker.attack(target)

        # Check that the target's health decreased significantly due to the critical hit
        self.assertLess(target.health, 30)
        self.assertIsInstance(self.MAP.get_object_in_position(2, 4), DeadBody)

    @patch("libraries.characters.base_class.d20", side_effect=lambda: 5)  # Simulate a miss
    def test_character_attack_kills_after_multiple_attacks(self, mock_d20):
        """Test that multiple attacks can kill the target and create a DeadBody."""
        attacker = Character("Hero", x_axis=2, y_axis=3)
        target = Character("Goblin", x_axis=2, y_axis=4)
        target.health = 30
        attacker.damage = 15  # Set damage enough to kill after a few attacks

        # First attack misses
        attacker.attack(target)
        self.assertEqual(target.health, 30)

        # Second attack hits
        with patch("libraries.characters.base_class.d20", side_effect=lambda: 12):  # Simulate a hit (d20 >= 10)
            attacker.attack(target)

        # Check that the target's health is reduced after the second attack
        self.assertLess(target.health, 30)

        # Third attack kills
        with patch(
            "libraries.characters.base_class.d20", side_effect=lambda: 20
        ):  # Simulate a critical hit (d20 == 20)
            attacker.attack(target)

        # Test that the target is dead and a DeadBody is created
        self.assertTrue(target.is_dead)
        self.assertIsInstance(self.MAP.get_object_in_position(2, 4), DeadBody)
