from defining_classes_01.guild_system.project.player import Player
from defining_classes_01.guild_system.project.guild import Guild

import unittest


class GuildTest(unittest.TestCase):

    def test_info(self):
        guild = Guild("GGXrd")
        player = Player("Pesho", 90, 90)
        guild.assign_player(player)
        message = guild.guild_info()
        expected = "Guild: GGXrd\nName: Pesho\nGuild: GGXrd\nHP: 90\nMP: 90\n"
        self.assertEqual(message, expected)


if __name__ == '__main__':
    unittest.main()