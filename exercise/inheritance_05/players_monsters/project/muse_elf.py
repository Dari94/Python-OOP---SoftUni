from inheritance_05.players_monsters.project.elf import Elf


class MuseElf(Elf):
    def __init__(self, username, level):
        super().__init__(username,level)