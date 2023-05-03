from classes.Player import Player
from typing import List

# Quests that friendly npc can give to player
# completing quests grants rewards currently only xp (experience)
class Quest:

    def update_count(self, count=1):
        self.current_count += count
        if self.current_count >= self.object_count:
            self.completed = True
            self.current_count = self.object_count
    
    # Checks if questline required for starting the quest
    # is completed so that the
    # Quest can be given to the player
    def quest_line_completed(self, quests: List[str]):
        ok = True
        for quest in self.quest_line:
            if quest not in quests:
                ok = False
        return ok
    
    def quest_aivailable(self, player: Player):
        if len(self.quest_line) == 0 and player.level >= self.lvl_requirement:
            return True
        elif player.level >= self.lvl_requirement:
            return self.quest_line_completed(player.completed_quests)
        return False
    
    def __init__(self, title: str, type: str, information: str, object: str, xp: int, object_count: int, object_target: str, lvl_requirement=1, current_count = 0, completed=False, quest_line = []) -> None:
        self.title = title
        self.type = type
        self.information = information
        self.object = object
        self.xp = xp
        self.object_count = object_count
        self.current_count = current_count
        self.object_target = object_target
        self.completed = completed
        self.lvl_requirement = lvl_requirement
        self.quest_line = quest_line
    
    def __repr__(self) -> str:
        return f'{self.title}, completed: {self.completed}'