class Combat_text:
    def update_pos(self, amount):
        self.y -= amount
        self.lifetime -= 1 

    def __init__(self, txt: str, color: str, x: int, y: int, lifetime=45) -> None:
        self.txt = txt
        self.lifetime = lifetime
        self.color = color
        self.x = x
        self.y = y