import pygame

class Player:
    def __init__(self, name: str, max_health: int, curr_health:int, level: int, xp: int, quests: list, abilities: list ):
        self.name = name
        self.max_health = max_health
        self.curr_health = curr_health
        self.level = level
        self.xp = xp
        self.quests = quests
        self.abilities = abilities