class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []

    def print_inventory(self):
        if not self.furniture:
            print("Inventory empty")
        else:
            inventory = {}
            for item in self.furniture:
                inventory[item] = inventory.get(item, 0) + 1
            output = ', '.join(f"{item}: {count}" for item, count in inventory.items())
            print(output)

alice = Villager("Alice", "Koala", "guvnor")

alice.print_inventory()

alice.furniture = ["acoustic guitar", "ironwood kitchenette", "kotatsu", "kotatsu"]
alice.print_inventory()