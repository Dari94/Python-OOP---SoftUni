from inheritance_05.players_monsters.project.hero import Hero


class Wizard(Hero):
    def __init__(self, username, level):
        super().__init__(username,level)