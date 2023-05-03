# Abilities the player can use
class Ability:

    def used(self):
        self.usable = False
        self.cooldown_remaining = self.cooldown
    
    # Ticks down the cooldown of the ability and makes it usable if cooldown ends
    def run_cooldown(self):
        if self.cooldown_remaining == 0:
            self.usable = True
        self.cooldown_remaining -= 1

    def __init__(self, name: str, type:str, damage:int, healing: int, cooldown: int, usable: bool) -> None:
        self.name = name
        self.type = type
        self.damage = damage
        self.healing = healing
        self.cooldown = cooldown
        self.cooldown_remaining = 0
        self.usable = usable