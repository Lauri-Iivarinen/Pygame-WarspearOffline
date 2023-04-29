
from Mob import Mob
from Quest import Quest

def round_coord(num):
    return round(num/40)*40

connected = {
    '1': {
        'n': 0,
        'w': 2,
        's': 0,
        'e': 0
    }
}

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

quests = {
    'One Eyed Jack': [
        Quest('Booze thiefs', 'kill', 'These slimey green idiots must have\nstolen my booze and drank it all.\n*hick*\nCan you punish these goblins for *hick*\nstealing my booze *hick*?', 'Kill 4 goblins.', 85, 4, ' Goblin'),
        Quest('Gain experience', 'level', 'Reach level 2.', 'Level up.', 85, 2, '',1,1),
    ]
}

mobs = {
    '1': [
        Mob(False, 1000, 1000, 'One Eyed Jack', 0, quests['One Eyed Jack'], 200, 80, (100,100,255),'Unagh....\nHello you...\nhave you seen my booze?',200),
        Mob(True, 80, 80,' Goblin', 35, [], round_coord(600), round_coord(410), (50,150,50)),
        Mob(True, 80, 80,' Goblin', 35, [], round_coord(500), round_coord(350), (50,150,50)),
        Mob(True, 80, 80,' Goblin', 35, [], round_coord(400), round_coord(300), (50,150,50)),
        Mob(True, 80, 80,' Goblin', 35, [], round_coord(300), round_coord(250), (50,150,50)),
        Mob(True, 80, 80,' Goblin', 35, [], round_coord(200), round_coord(200), (50,150,50)),
        Mob(True, 80, 80,' Goblin', 35, [], round_coord(100), round_coord(150), (50,150,50)),
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
        self.connected = connected[f'{mapNum}']
        #self.editMap()