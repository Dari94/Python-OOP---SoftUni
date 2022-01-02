from project.card.card import Card
from project.card.magic_card import MagicCard


class CardRepository:
    def __init__(self):
        self.cards = []

    @property
    def count(self):
        return len(self.cards)

    def add(self, card):
        #if card in [c.name for c in self.cards]
        if any(c.name == card.name for c in self.cards):
            raise ValueError(f"Card {card.name} already exists!")
        self.cards.append(card)

    def remove(self, card):
        if card == "":
            raise ValueError("Card cannot be an empty string!")
        found_card = self.find(card)
        self.cards.remove(found_card)

    def find(self, name: str):
        found_card = [card for card in self.cards if card.name == name][0]
        return found_card


# cr = CardRepository()
# card = MagicCard("Magic")
# card_1 = MagicCard("trr")
# cr.add(card)
# cr.add(card_1)


#print(cr.__dict__)
