class Quest:

    def update_count(self, count=1):
        self.current_count += count
        if self.current_count >= self.object_count:
            self.completed = True
            self.current_count = self.object_count

    def __init__(self, title: str, type: str, information: str, object: str, xp: int, object_count: int, object_target: str, lvl_requirement=1, current_count = 0, completed=False) -> None:
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