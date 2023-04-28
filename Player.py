from Item import Item
from Ability import Ability

items = {
    'weapon': Item('Broken sword', 10, 15),
    'chest' : Item('Chainmail armor', 20, 0),
    'legs': Item('Rusty chainmail leggings', 15, 0)
}

class Player:

    def gain_xp(self, incoming_xp):
        self.xp += incoming_xp
        if self.xp >= self.xp_cap:
            self.xp -= self.xp_cap
            self.level += 1
            self.xp_cap += 10

    def die(self):
        self.damage = 0
        self.curr_health = 0
        self.alive = False
    
    def receive_damage(self, damage):
        if self.alive:
            self.curr_health -= damage
            if self.curr_health < 0:
                self.die()
    
    def receive_healing(self, amount):
        self.curr_health += amount
        if self.curr_health > self.max_health:
            self.curr_health = self.max_health

    def doAbility(self, ability: Ability):
        if not ability.usable:
            return
        if ability.type == 'heal':
            self.receive_healing(ability.healing)
        elif ability.type == 'dmg':
            self.damage_buff = True
            self.damage_buff_amount = ability.damage
        
        ability.used()
    
    def useAbility(self, name:str):
        print(name)
        for a in self.abilities:
            if a.name == name:
                self.doAbility(a)
                break
        

    def calc_damage(self):
        damage = items['weapon'].damage + (self.level*10)
        if self.damage_buff:
            damage += self.damage_buff_amount
            self.damage_buff_amount = 0
            self.damage_buff = False

        return damage

    def reduce_cooldowns(self):
        for cd in self.abilities:
            cd.run_cooldown()

    def __init__(self, name: str, max_health: int, curr_health:int, level: int, xp: int, quests: list, abilities: list, alive=True ):
        self.name = name
        self.max_health = max_health
        self.curr_health = curr_health
        self.level = level
        self.xp = xp
        self.quests = quests
        self.abilities = [
            Ability('Vitalize', 'heal', 0, 35, 5, True),
            Ability('Slash', 'dmg', 25, 0, 7, True)
        ]
        self.xp_cap = 100
        self.items = items
        self.alive = alive
        self.damage_buff = False
        self.damage_buff_amount = 0


