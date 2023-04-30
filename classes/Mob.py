class Mob:

    def get_name_color(self, hostile):
        if hostile:
            return 'red'
        return 'white'

    def die(self):
        self.damage = 0
        self.curr_health = 0
        self.alive = False
    
    def receive_damage(self, damage):
        if self.alive:
            self.curr_health -= damage
            if self.curr_health < 0:
                self.die()
    
    def quest_accepted(self, quest):
        index = self.quests.index(quest)
        self.quests.pop(index)
        self.quests_in_process.append(quest)

    def __init__(self, hostile: bool, max_health: int, curr_health: int, name: str, xp: int, quests: list, x: int, y: int, color, on_speak_text = '', damage=15, alive=True ):
        self.hostile = hostile
        self.max_health = max_health
        self.curr_health = curr_health
        self.name = name
        self.xp = xp
        self.quests = quests
        self.x = x
        self.y = y
        self.color = color
        self.name_color = self.get_name_color(hostile)
        self.damage = damage
        self.alive = alive
        self.on_speak_text = on_speak_text
        self.quests_in_process = []