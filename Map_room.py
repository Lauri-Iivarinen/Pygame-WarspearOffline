
from Mob import Mob


maps = {
    '1': [
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X'],
        ['X', 'X', 'X', 'X', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X'],
        ['X', 'X', 'X', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X'],
        ['X', 'X', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X'],
        ['X', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X'],
        ['X', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X'],
        ['X', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X'],
        ['X', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X'],
        ['X', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X'],
        ['X', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X'],
        ['X', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X'],
        ['X', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X'],
        ['X', 'X', 'X', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
]
}

mobs = {
    '1': [
        Mob(False, 1000, 1000, 'One Eyed Jack', 0, [], 200, 80, (100,100,255),200),
        Mob(True, 80, 80,' Goblin', 35, [], 600, 410, (50,150,50)),
        Mob(True, 80, 80,' Goblin', 35, [], 650, 450, (50,150,50)),
        Mob(True, 80, 80,' Goblin', 35, [], 500, 480, (50,150,50)),
        Mob(True, 80, 80,' Goblin', 35, [], 400, 300, (50,150,50)),
        Mob(True, 80, 80,' Goblin', 35, [], 300, 500, (50,150,50)),
        Mob(True, 80, 80,' Goblin', 35, [], 350, 420, (50,150,50)),
    ]
}

def getMobs(roomNum):
    return mobs[f'{roomNum}']

def getRoom(roomNum):
    return maps[f'{roomNum}']


class Map_room:

    def get_map(self, mapNum):
        mapStr = getRoom(mapNum)
        map = []
        for rows in mapStr:
            row = []
            for col in rows:
                if col == 'X':
                    row.append(False)
                else:
                    row.append(True)
            map.append(row)
        
        return map

    def print_map(self):
        for i in self.map:
            string = ''
            for a in i:
                if a:
                    string += ' '
                else:
                    string += 'X'
            print(string)


    def __init__(self, mapNum):
        self.map = self.get_map(mapNum)
        self.mobs = getMobs(mapNum)
        #self.editMap()