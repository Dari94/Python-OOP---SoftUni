from defining_classes_01.guild_system.project.player import Player
import unittest


class PlayerTest(unittest.TestCase):
    def test_info(self):
        player = Player("Pesho", 90, 90)
        player.add_skill("A", 3)
        message = player.player_info()
        expected = "Name: Pesho\nGuild: Unaffiliated\nHP: 90\nMP: 90\n===A - 3\n"
        self.assertEqual(message, expected)


if __name__ == '__main__':
    unittest.main()