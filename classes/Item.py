# Items player can equip to gain powers
class Item:
    def __init__(self, name, health, damage) -> None:
        self.name = name
        self.health = health
        self.damage = damage