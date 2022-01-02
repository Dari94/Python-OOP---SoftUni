from project.player.advanced import Advanced

import unittest


class AdvancedPlayer(unittest.TestCase):
    def test_initPlayerAttributes(self):
        p_username = 'Pesho'
        player = Advanced(p_username)
        self.assertEqual(player.card_repository.__class__.__name__, "CardRepository")
        self.assertEqual(player.username, p_username)
        self.assertEqual(player.health, 250)

    def test_beginner_inherit_player(self):
        self.assertTrue("Player" == Advanced.__bases__[0].__name__)


if __name__ == "__main__":
    unittest.main()
