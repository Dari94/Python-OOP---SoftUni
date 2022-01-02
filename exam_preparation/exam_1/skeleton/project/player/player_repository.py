from project.player.player import Player


class PlayerRepository:
    def __init__(self):
        self.players = []
        #self.count = 0

    @property
    def count(self):
        return len(self.players)

    def add(self, player):
        if any(p.username == player.usename for p in self.players):
            raise ValueError(f"Player {player.username} already exists!")
        self.players.append(player)

    def remove(self, player):
        if player == "":
            raise ValueError("Player cannot be an empty string!")
        found_player = self.find(player)
        self.players.remove(found_player)

    def find(self, username):
        found_player = [player for player in self.players if player.username == username][0]
        #found_player = list(filter(lambda p: p.username == username, self.players))[0]
        return found_player
