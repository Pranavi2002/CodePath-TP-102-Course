class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []

    def set_catchphrase(self, new_catchphrase):
        if len(new_catchphrase) < 20 and all(c.isalpha() or c.isspace() for c in new_catchphrase):
            self.catchphrase = new_catchphrase
            print("Catchphrase updated")
        else:
            print("Invalid catchphrase")

alice = Villager("Alice", "Koala", "guvnor")

alice.set_catchphrase("sweet dreams")
print(alice.catchphrase)

alice.set_catchphrase("#?!")
print(alice.catchphrase)
