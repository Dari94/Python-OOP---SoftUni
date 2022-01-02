from project.battle_field import BattleField
from project.card.magic_card import MagicCard
from project.player.beginner import Beginner
import unittest


class testBattleField(unittest.TestCase):
    def test_fight_withDeadPlayer_raiseValueError(self):
        bf = BattleField()
        p1 = Beginner('Peter')
        p2 = Beginner('George')
        p1.health = 0
        with self.assertRaises(ValueError) as context:
            bf.fight(p1, p2)
        self.assertEqual(str(context.exception), "Player is dead!")

    def test_attackerBeginner_shouldIncreaseHealth(self):
        bf = BattleField()
        mg1 = MagicCard("Magic One")
        mg2 = MagicCard("Magic Two")
        p1 = Beginner("Peter")
        p2 = Beginner("George")
        p1.card_repository.add(mg1)
        p1.card_repository.add(mg2)

        bf.fight(p1, p2)
        self.assertEqual(p1.health, 250)

    def test_enemyBeginner_shouldIncreaseHealth(self):
        bf = BattleField()
        mg1 = MagicCard("Magic One")
        mg2 = MagicCard("Magic Two")
        p1 = Beginner("Peter")
        p2 = Beginner("George")
        p2.card_repository.add(mg1)
        p2.card_repository.add(mg2)
        bf.fight(p1,p2)
        self.assertEqual(p2.health,250)

    def test_player_dies_in_fight(self):
        bf = BattleField()
        mg1 = MagicCard("Magic One")
        mg2 = MagicCard("Magic Two")
        p1 = Beginner("Peter")
        p2 = Beginner("George")
        p1.card_repository.add(mg1)
        p1.card_repository.add(mg2)
        bf.fight(p1, p2)
        with self.assertRaises(ValueError) as context:
            bf.fight(p1, p2)
        self.assertEqual(str(context.exception), "Player's health bonus cannot be less than zero.")



if __name__ == "__main__":
    unittest.main()

