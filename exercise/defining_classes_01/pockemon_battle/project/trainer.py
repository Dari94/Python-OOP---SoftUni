from defining_classes_01.pockemon_battle.project.pokemon import Pokemon


class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemon = []

    def add_pokemon(self, pokemon):
        if pokemon in self.pokemon:
            return f"This pokemon is already caught"
        self.pokemon.append(pokemon)
        return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, pokemon_name):
        # pokemon_list2 = [pokemon_name for pokemon_name in self.pokemon if pokemon == pokemon_name]
        pokemon_list = list(filter(lambda p: p.name == pokemon_name, self.pokemon))
        if not pokemon_list:
            return 'Pokemon is not caught'

        current_pokemon = pokemon_list[0]
        self.pokemon.remove(current_pokemon)
        return f'You have released {current_pokemon.name}'

    def trainer_data(self):
        info = f"Pokemon Trainer {self.name}\n"
        info += f"Pokemon count {len(self.pokemon)}\n"
        if self.pokemon:
            info += "\n".join([f'- {pokemon.pokemon_details()}' for pokemon in self.pokemon])
            info += "\n"
        return info


pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())
