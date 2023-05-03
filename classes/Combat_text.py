#Floating combat text that previews damage done healing received
#can also be used as anouncement base for quest completion etc
class Combat_text:
    def update_pos(self, amount):
        self.y -= amount
        self.lifetime -= 1 

    def __init__(self, txt: str, color: str, x: int, y: int, lifetime=45, speed=1) -> None:
        self.txt = txt
        self.lifetime = lifetime
        self.color = color
        self.x = x
        self.y = y
        self.speed = speed