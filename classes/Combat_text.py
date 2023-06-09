# Rolling texts in screen for displaying
# Announcements or combat infor (damage done/taken, healing done)
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