from project.player.beginner import Beginner

import unittest
class BeginnerPlayer(unittest.TestCase):
    def test_initPlayerAttributes(self):
        p_username = 'Pesho'
        player = Beginner(p_username)
        self.assertEqual(player.card_repository.__class__.__name__, "CardRepository")
        self.assertEqual(player.username, p_username)
        self.assertEqual(player.health, 50)

    def test_beginner_inherit_player(self):
        self.assertTrue("Player" == Beginner.__bases__[0].__name__)

    def test_emptyStringUsername_ShouldRaiseError(self):
        p_username = 'Pesho'
        player = Beginner(p_username)
        with self.assertRaises(ValueError) as context:
            player.username = ""
        self.assertEqual(str(context.exception), "Player's username cannot be an empty string.")

    def test_setNewUsername_ShouldChangeUsername(self):
        p_username = 'Pesho'
        player = Beginner(p_username)
        player.username = 'Gosho'
        self.assertEqual(player.username,'Gosho')

    def test_whenHealthBellow0_shouldRaiseError(self):
        p_username = 'Pesho'
        player = Beginner(p_username)
        with self.assertRaises(ValueError) as context:
            player.health = -5
        self.assertEqual(str(context.exception), "Player's health bonus cannot be less than zero.")

    def test_setHealthSuccess(self):
        p_username = 'Pesho'
        player = Beginner(p_username)
        player.health = 10
        self.assertEqual(player.health, 10)




if __name__ == "__main__":
    unittest.main()