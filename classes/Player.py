from classes.Item import Item
from classes.Ability import Ability

# Current items in posession of the player
# Only weapon stats affect gameplay
items = {
    'weapon': Item('Broken sword', 10, 15),
    'chest' : Item('Chainmail armor', 20, 0),
    'legs': Item('Rusty chainmail leggings', 15, 0)
}

# Stats of the player itself, currently does not affect movement, 
# it needs to be implemented as a superclass later
class Player:

    #Check if leveling up grants rewards
    def lvl_up_reward(self):
        if self.level == 2:
            self.abilities.append(Ability('Smash', 'dmg', 45, 0, 10, True))

    #Any time player gains xp check for level up
    def gain_xp(self, incoming_xp):
        self.xp += incoming_xp
        if self.xp >= self.xp_cap:
            self.xp -= self.xp_cap
            self.level += 1
            self.xp_cap += 10
            self.lvl_up_reward()

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
            return False
        if ability.type == 'heal':
            self.receive_healing(self.calc_healing(ability.healing))
        elif ability.type == 'dmg':
            self.damage_buff = True
            self.damage_buff_amount = ability.damage
        
        ability.used()
        return True
    
    #Find correct ability from the player and use it, could be later turned into dict
    def useAbility(self, name:str):
        print(name)
        for a in self.abilities:
            if a.name == name:
                return self.doAbility(a)
        
        return False

    def ability_usable(self, name: str):
        for ability in self.abilities:
            if ability.name == name:
                return ability.usable
        
        return False
    
    # Calculate amount of healing done with an ability based on level
    def calc_healing(self, heal):
        return heal + (self.level * 12)

    # Calculate amount of damage done with an ability based on level
    def calc_damage(self):
        damage = items['weapon'].damage + (self.level*10)
        if self.damage_buff:
            damage += self.damage_buff_amount
            self.damage_buff_amount = 0
            self.damage_buff = False

        return damage

    def get_ability(self, name) -> Ability:
        for ability in self.abilities:
            if ability.name == name:
                return ability

    def reduce_cooldowns(self):
        for cd in self.abilities:
            cd.run_cooldown()

    def accept_quest(self, quest):
        if quest not in self.quests and len(self.quests) <=3:
            self.quests.append(quest)
            return True
        return False
    
    def complete_quest(self, quest):
        if quest in self.quests:
            self.quests.remove(quest)
            self.completed_quests.append(quest.title)
            self.gain_xp(quest.xp)

    def __init__(self, name: str, max_health: int, curr_health:int, level: int, xp: int, quests: list, abilities: list, alive=True):
        self.name = name
        self.max_health = max_health
        self.curr_health = curr_health
        self.level = level
        self.xp = xp
        self.quests = quests
        self.abilities = [
            Ability('Vitalize', 'heal', 0, 35, 5, True),
            Ability('Slash', 'dmg', 25, 0, 7, True),
        ]
        self.xp_cap = 100
        self.items = items
        self.alive = alive
        self.damage_buff = False
        self.damage_buff_amount = 0
        self.completed_quests = []


