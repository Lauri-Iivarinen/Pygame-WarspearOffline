
from classes.Mob import Mob
from classes.Quest import Quest

def round_coord(num):
    return round(num/40)*40

connected = {
    '1': {
        'n': 0,
        'w': 2,
        's': 0,
        'e': 0
    },
    '2': {
        'n': 3,
        'w': 0,
        's': 0,
        'e': 1
    },
    '3': {
        'n': 0,
        'w': 0,
        's': 2,
        'e': 0
    }
    }

maps = {
    '1': [
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X', 'X'],
        ['X', 'X', 'X', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X', 'X'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X', 'X'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X', 'X'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X', 'X'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X', 'X'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X', 'X'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X', 'X'],
        ['X', 'X', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X', 'X'],
        ['X', 'X', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X', 'X'],
        ['X', 'X', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ],
    '2':[
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'O', 'O', 'O', 'O', 'O', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'O', 'O', 'O', 'O', 'O', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X', 'X', 'X'],
        ['X', 'X', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X', 'X', 'X'],
        ['X', 'X', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X', 'X', 'X'],
        ['X', 'X', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['X', 'X', 'X', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['X', 'X', 'X', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['X', 'X', 'X', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['X', 'X', 'X', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['X', 'X', 'X', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['X', 'X', 'X', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X', 'X'],
        ['X', 'X', 'X', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X', 'X'],
        ['X', 'X', 'X', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ],
    '3':[
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'O', 'O', 'O', 'O', 'O', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'O', 'O', 'O', 'O', 'O', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ],
}

quests = {
    'One Eyed Jack': [
        Quest('Mystery island', 'lvl', 'You need to have more experience.\nExplore the island and get familiar\nwith its creatures. Only then can I tell you about\nthe secret of the island', 'Reach level 5.', 95, 5, '',1,1),
        Quest('Booze thiefs', 'kill', 'These slimey green idiots must have\nstolen my booze and drank it all.\n*hick*\nCan you punish these goblins for *hick*\nstealing my booze *hick*?', 'Kill 5 goblins.', 65, 5, ' Goblin'),
        Quest('Love of my life', 'find', 'Please find my wife, Henneck\nShe is the love of my life.', 'Find Henneck.', 30, 1, 'Henneck',1,0),
        Quest('Mystery revealed', 'autocomplete', 'Its all a dream', 'Oh no...', 95, 1, '',5,1)
    ],
    'Henneck': [
        Quest('Pirates ahoy', 'kill', "I can't stand these nasty pirates\nPlease reduce their numbers for me.", 'Kill 4 pirates.', 85, 4, 'Pirate'),
        Quest('No food for you!', 'find', 'Please tell Jack that I will not\ncome back untill he has sobered up.\nFurthermore I will not be cooking for him either', 'Return to Jack', 30, 1, 'One Eyed Jack', 1, 0, False, ['Love of my life'])
    ]
}

in_process = {
    'Henneck' : [
        Quest('Love of my life', 'find', 'Please find my wife, Henneck\nShe is the love of my life.', 'Find Henneck.', 30, 1, 'Henneck',1,0),
    ],
    'One Eyed Jack': [
        Quest('No food for you!', 'find', 'Please tell Jack that I will not\ncome back untill he has sobered up.\nFurthermore I will not be cooking for him either', 'Return to Jack', 30, 1, 'One Eyed Jack', 1, 0, False, ['Love of my life'])
    ]
}

mobs = {
    '1': [
        Mob(False, 1000, 1000, 'One Eyed Jack', 0, quests['One Eyed Jack'], round_coord(560), round_coord(450), (100,100,255),'Unagh....\nHello you...\nhave you seen my booze?',200, True, in_process['One Eyed Jack']),
        Mob(True, 80, 80,' Goblin', 25, [], round_coord(570), round_coord(110), (50,150,50)),
        Mob(True, 80, 80,' Goblin', 25, [], round_coord(150), round_coord(450), (50,150,50)),
        Mob(True, 80, 80,' Goblin', 25, [], round_coord(250), round_coord(75), (50,150,50)),
        Mob(True, 80, 80,' Goblin', 25, [], round_coord(300), round_coord(50), (50,150,50)),
        Mob(True, 80, 80,' Goblin', 25, [], round_coord(250), round_coord(400), (50,150,50)),
        Mob(True, 80, 80,' Goblin', 25, [], round_coord(400), round_coord(80), (50,150,50)),
        Mob(True, 80, 80,' Goblin', 25, [], round_coord(100), round_coord(300), (50,150,50)),
    ],
    '2':[
        Mob(True, 80, 80,' Goblin', 25, [], round_coord(200), round_coord(200), (50,150,50)),
        Mob(True, 80, 80,' Goblin', 25, [], round_coord(150), round_coord(150), (50,150,50)),
        Mob(True, 110, 110, 'Pirate', 30, [], round_coord(600), round_coord(450), (0,0,0), '', 25),
        Mob(True, 110, 110, 'Pirate', 30, [], round_coord(550), round_coord(400), (0,0,0), '', 25),
        Mob(True, 110, 110, 'Pirate', 30, [], round_coord(500), round_coord(400), (0,0,0), '', 25),
        Mob(True, 110, 110, 'Pirate', 30, [], round_coord(400), round_coord(450), (0,0,0), '', 25),
        Mob(True, 110, 110, 'Pirate', 30, [], round_coord(550), round_coord(50), (0,0,0), '', 25),
        Mob(True, 110, 110, 'Pirate', 30, [], round_coord(620), round_coord(100), (0,0,0), '', 25),
    ],
    '3': [
        Mob(False, 1000, 1000, 'Henneck', 0, quests['Henneck'], round_coord(260), round_coord(450), (100,100,255),'Is Jack still drunk?\n \n ',200, True, in_process['Henneck']),
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
    
    def enter_new_map(self, x:int, y:int):
        num = 0
        if x<=40:
            num = self.connected['w']
        elif x>=760:
            num = self.connected['e']
        elif y<=40:
            num = self.connected['n']
        else:
            num = self.connected['s']
        
        if num != 0:
            self.map = self.get_map(num)
            self.mobs = getMobs(num)
            self.connected = connected[f'{num}']
            self.map_num = num
        pass

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
        self.map_num = mapNum