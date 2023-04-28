class Mob:

    def get_name_color(self, hostile):
        if hostile:
            return 'red'
        return 'white'

    def __init__(self, hostile: bool, health: int, name: str, xp: int, quests, x: int, y: int, color ):
        self.hostile = hostile
        self.health = health
        self.name = name
        self.xp = xp
        self.quests = quests
        self.x = x
        self.y = y
        self.color = color
        self.name_color = self.get_name_color(hostile)