class Map_room:
    
    def generate_map(self):
        playMapRow = []
        playMap = []
        for i in  range(0,21):
            if i==0 or i== 20:
                playMapRow.append(False)
            else:
                playMapRow.append(True)
        for i in range(0,16):
            if i==0 or i==15:
                row=[]
                for a in range(0,21):
                    row.append(False)
                playMap.append(row)
            else:
                playMap.append(playMapRow)
        return playMap
    

    def print_map(self):
        for i in self.map:
            string = ''
            for a in i:
                if a:
                    string += ' '
                else:
                    string += 'X'
            print(string)

    def __init__(self):
        self.map = self.generate_map()