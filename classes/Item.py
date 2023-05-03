#Items player can equip that grant bonus based on item stats
#Currently only weapon damage is applied
class Item:
    def __init__(self, name, health, damage) -> None:
        self.name = name
        self.health = health
        self.damage = damage