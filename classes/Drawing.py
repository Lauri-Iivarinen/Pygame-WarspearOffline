import pygame
from classes.Mob import Mob
from classes.Player import Player
from classes.Quest import Quest
from classes.Combat_text import Combat_text

class Drawing:
    WINDOW_WDTH = 800 #20x15 movable area
    WINDOW_HGHT = 600
    #self.WINDOW = pygame.display.set_mode((self.WINDOW_WDTH,self.WINDOW_HGHT))
    #pygame.display.set_caption('Warspear offline')
    PLAYER_WDTH = 20
    PLAYER_HGHT = 50
    PLAYER_VELOCITY = 5
    CURSOR_SIZE = 20
    CURSOR_THICKNESS = 3
    
    def roundCursorPos(self,cursor: tuple):
        x = round(cursor[0]/40)
        y = round(cursor[1]/40)
        return (x * 40, y * 40)

    def clear_opened_quest(self):
        if len(self.open_quest) > 0:
            self.open_quest.pop()
    
    def draw_menu(self):
        self.WINDOW.fill((145,150,50))
        title = self.LARGEFONT.render('WARSPER OFFLINE', 1, 'black')
        self.WINDOW.blit(title, (75,75))
        play_frame = pygame.Rect(75, 130, 100, 50)
        play_txt = self.BIGFONT.render('PLAY', 1, 'black')
        self.WINDOW.blit(play_txt, (100,140))
        pygame.draw.rect(self.WINDOW, 'black', play_frame, 1)
        pygame.display.update()
    
    def get_text_pos(self,x,y,length):
        y -= 22
        x -= length*3
        return (x,y)
    
    def get_quest_icon(self, mob: Mob, player: Player) -> str:
        quests = self.get_completed_quests(mob, player)
        if len(quests) > 0:
            return "?"
        elif mob.is_aivailable_quests(player.level):
            return "!"
        return ""

    def get_quest_icon_pos(self, pos, icon):
        if icon == '!': return pos-2
        else: return pos-4

    def draw_mobs(self, player: Player):
        for mob in self.map.mobs:
            name:str = mob.name
            npc = pygame.transform.scale(pygame.image.load(f'assets/mobs/{name.strip()}.png'), (self.PLAYER_WDTH, self.PLAYER_HGHT))
            npc_name = self.FONT.render(mob.name, 1, mob.name_color)
            npc_pos = self.roundCursorPos((mob.x, mob.y))
            if mob.alive:
                npc_name_pos = self.get_text_pos(npc_pos[0]-10, npc_pos[1], len(mob.name))
                #npc = pygame.Rect(npc_pos[0]-10, npc_pos[1], self.PLAYER_WDTH, self.PLAYER_HGHT)
                self.WINDOW.blit(npc_name, npc_name_pos)
                #pygame.draw.rect(self.WINDOW, mob.color, npc)
                if not mob.hostile:
                    icon = self.get_quest_icon(mob, player)
                    quest_icon = self.LARGEFONT.render(icon, 1, 'yellow')
                    self.WINDOW.blit(quest_icon, (self.get_quest_icon_pos(npc_pos[0], icon), npc_name_pos[1]-30))
            else:
                #pygame.draw.circle(self.WINDOW, 'red', (npc_pos[0], npc_pos[1]+40), 20)
                npc = pygame.transform.rotate(npc, -90)
                npc_pos = (npc_pos[0], npc_pos[1]+30)
                blood = pygame.Rect(npc_pos[0]-10, npc_pos[1]+5, self.PLAYER_HGHT, self.PLAYER_WDTH)
                pygame.draw.ellipse(self.WINDOW, 'red', blood)

            self.WINDOW.blit(npc, (npc_pos[0]-10, npc_pos[1]))
    

    def draw_UI(self,player: Player):
        bg = pygame.Rect(0,0,150,60)
        pygame.draw.rect(self.WINDOW, (255,215,128), bg)
        pygame.draw.rect(self.WINDOW, (194, 132, 0), bg, 2)
        name = self.FONT.render(player.name, 1, 'black')
        health_bar_frame = pygame.Rect(3,25, 102, 7)
        pygame.draw.rect(self.WINDOW, 'black', health_bar_frame)
        health_bar = pygame.Rect(4,26, round((player.curr_health/player.max_health)*100), 5)
        pygame.draw.rect(self.WINDOW, 'red', health_bar)
        xp_bar_frame = pygame.Rect(3,33, 102, 7)
        pygame.draw.rect(self.WINDOW, 'black', xp_bar_frame)
        xp_bar = pygame.Rect(4,34, round((player.xp/100)*100), 5)
        pygame.draw.rect(self.WINDOW, 'yellow', xp_bar)
        pygame.draw.circle(self.WINDOW, 'black', (128,25), self.CURSOR_SIZE, self.CURSOR_THICKNESS)
        level = self.FONT.render(f'{player.level}', 1, 'black')
        self.WINDOW.blit(name, (5,5))
        self.WINDOW.blit(level, (125,15))
        #BG (255,215,128)
        #frame (194, 132, 0)


    def draw_target_UI(self,player: Mob):
        bg = pygame.Rect(160,0,150,60)
        pygame.draw.rect(self.WINDOW, (255,215,128), bg)
        pygame.draw.rect(self.WINDOW, (194, 132, 0), bg, 2)
        name = self.FONT.render(player.name, 1, 'black')
        hp_txt = self.FONT.render(f'{player.curr_health}/{player.max_health}', 1, 'black')
        health_bar_frame = pygame.Rect(163,25, 102, 7)
        pygame.draw.rect(self.WINDOW, 'black', health_bar_frame)
        health_bar = pygame.Rect(164,26, round((player.curr_health/player.max_health)*100), 5)
        pygame.draw.rect(self.WINDOW, 'red', health_bar)
        self.WINDOW.blit(name, (162,5))
        self.WINDOW.blit(hp_txt, (165, 32))


    def draw_ability_bar(self,abilities: list):
        x = 250
        y = 550
        bg = pygame.Rect(x,y,300,50)
        #pygame.draw.rect(self.WINDOW, (255,215,128), bg)
        pygame.draw.rect(self.WINDOW, (194, 132, 0), bg, 2)
        y += 15
        x += 10
        for ability in abilities:
            txt:str = ability.name
            if len(ability.name) >= 6:
                txt = txt[0:5]+'..'
            name = self.SMALLFONT.render(txt, 1, 'black')
            
            if ability.usable:
                img = pygame.image.load(f'assets/icons/{ability.name}.png')
                icon = pygame.Rect(x,555,30,10)#Replace with icon
                pygame.draw.rect(self.WINDOW, (255,215,128) , icon)
                self.WINDOW.blit(img, (x,y))
            else:
                cd = self.FONT.render(f'{ability.cooldown_remaining}', 1, 'black')
                icon = pygame.Rect(x,y,30,30)
                pygame.draw.rect(self.WINDOW, (0,0,0), icon, 1) 
                self.WINDOW.blit(cd, (x+12, 570))
            self.WINDOW.blit(name, (x,552))
            x += 50

    def draw_announcement(self):
        for txt in self.announcement:
            text = self.BIGFONT.render(txt.txt, 1, txt.color)
            self.WINDOW.blit(text, (txt.x, txt.y))
            txt.update_pos(1)#Text velocity
            if txt.lifetime <= 0:
                index = self.announcement.index(txt)
                self.announcement.pop(index)

    def draw_combat_text(self):
        for txt in self.combat_txt:
            text = self.FONT.render(txt.txt, 1, txt.color)
            self.WINDOW.blit(text, (txt.x, txt.y))
            txt.update_pos(2)#Text velocity
            if txt.lifetime <= 0:
                index = self.combat_txt.index(txt)
                self.combat_txt.pop(index)

    def draw_opened_quest(self,quest: Quest, cursor, player: Player,x: int, y: int, completing_quest, target: Mob):
        bg = pygame.Rect(x,y,280,280)
        pygame.draw.rect(self.WINDOW, (255,215,128), bg)
        frame = pygame.Rect(x,y,280,280)
        pygame.draw.rect(self.WINDOW, 'black', frame, 1)
        title = self.FONT.render(quest.title, 1, 'black')
        self.WINDOW.blit(title, (x+10,y))
        info_txt = quest.information.split('\n')
        txt_y = y+20
        for txt in info_txt:
            information = self.SMALLFONT.render(txt, 1, 'black')
            self.WINDOW.blit(information, (x+10,txt_y))
            txt_y += 10
        object = self.SMALLFONT.render(quest.object, 1, 'black')
        self.WINDOW.blit(object, (x+10, 370))
        if completing_quest:
            txt_frame = pygame.Rect(x+10,390,70,40)
            pygame.draw.rect(self.WINDOW, 'black', txt_frame, 1)
            object = self.FONT.render('Complete', 1, 'black')
            self.WINDOW.blit(object, (x+15,400))
        else:
            txt_frame = pygame.Rect(x+10,390,70,40)
            pygame.draw.rect(self.WINDOW, 'black', txt_frame, 1)
            object = self.FONT.render('Accept', 1, 'black')
            dcl_frame = pygame.Rect(x+90,390,70,40)
            pygame.draw.rect(self.WINDOW, 'black', dcl_frame, 1)
            decline = self.FONT.render('Decline', 1, 'black')
            self.WINDOW.blit(object, (x+15,400))
            self.WINDOW.blit(decline, (x+95, 400))
    

    def get_quests(self,target: Mob, player: Player):
        quests = []
        quest_count = 0
        for quest in target.quests:
            if quest.lvl_requirement <= player.level:
                quests.append(quest)
                quest_count += 1
            if quest_count == 3:
                break
        return quests

    def accept_quest(self,player: Player, target: Mob):
        if len(self.open_quest) == 1:
            if player.accept_quest(self.open_quest[0]):
                target.quest_accepted(self.open_quest[0])
                print('QUEST ACCEPTED')
                self.announcement.append(Combat_text('QUEST ACCEPTED', 'white', 300, 75))
                self.clear_opened_quest()

    def get_completed_quests(self,target: Mob, player: Player):
        quests = []
        for quest in target.quests_in_process:
            for player_quest in player.quests:
                if quest==player_quest and player_quest.completed:
                    quests.append(player_quest)
        return quests

    def draw_text_box(self,target: Mob, player: Player):
        text_x = 260
        text_y = 110
        bg = pygame.Rect(250, 100, 300, 400)
        pygame.draw.rect(self.WINDOW, (255,215,128), bg)
        frame = pygame.Rect(250, 100, 300, 400)
        pygame.draw.rect(self.WINDOW, (194, 132, 0), frame, 4)
        completed_quests = self.get_completed_quests(target, player)

        txt = target.on_speak_text.split('\n')
        for str in txt:
            greeting = self.FONT.render(str, 1, 'black')
            self.WINDOW.blit(greeting, (text_x,text_y))
            text_y += 15

        if len(completed_quests) > 0:
            mouse = pygame.mouse.get_pressed()
            y = 10+text_y
            self.draw_opened_quest(completed_quests[0], (0,0), player, text_x, 10+text_y, True, target)
            if mouse[0]:
                cursor = pygame.mouse.get_pos()
                if cursor[0] >= text_x and cursor[0] <= text_x+280 and cursor[1] >= 450 and cursor[1] <= 500:
                    self.clear_opened_quest()
                if cursor[0] >= text_x+10 and cursor[0] <= text_x+80 and cursor[1] >= 390 and cursor[1] <= 430:#accept button
                    player.complete_quest(completed_quests[0])
                    self.announcement.append(Combat_text('Quest completed', 'white', 300, 75))
        else:
            quests = self.get_quests(target, player)
            #draw_quests(target, text_x, text_y, player)
            cursor = (0,0)
            mouse = pygame.mouse.get_pressed()
            y = 10+text_y
            if mouse[0]:
                cursor = pygame.mouse.get_pos()
                if cursor[0] >= text_x and cursor[0] <= text_x+280 and cursor[1] >= 450 and cursor[1] <= 500:
                    self.clear_opened_quest()
                if cursor[0] >= text_x+90 and cursor[0] <= text_x+160 and cursor[1] >= 390 and cursor[1] <= 430:#decline button
                    self.clear_opened_quest()
                if cursor[0] >= text_x+10 and cursor[0] <= text_x+80 and cursor[1] >= 390 and cursor[1] <= 430:#accept button
                    self.accept_quest(player, target)
            if len(self.open_quest) == 0:
                for quest in quests:
                    if cursor[0] >= text_x and cursor[0] <= text_x+280 and cursor[1]>=y and cursor[1] <= y+50:
                        self.open_quest.append(quest)
                        break
                    frame = pygame.Rect(text_x,y,280,50)
                    pygame.draw.rect(self.WINDOW, 'black', frame, 1)
                    object = self.FONT.render(f'{quest.xp}xp - {quest.title}!', 1, 'black')
                    self.WINDOW.blit(object, (text_x+10, y+10))
                    y += 60
            else:
                self.draw_opened_quest(self.open_quest[0], (0,0), player, text_x, y, False, target)

    def draw_quest_tracker(self,player: Player):
        x = 700
        y = 0
        bg = pygame.Rect(x,y,100,150)
        pygame.draw.rect(self.WINDOW, (255,215,128), bg)
        pygame.draw.rect(self.WINDOW, (194, 132, 0), bg, 2)
        text = self.FONT.render(f'Quests {len(player.quests)}/3:', 1, 'black')
        self.WINDOW.blit(text, (x+5, y+10))
        y += 35
        for quest in player.quests:
            obj = self.SMALLFONT.render(quest.object, 1, 'black')
            if quest.completed:
                count = self.FONT.render('Completed!', 1, 'black')
            else:
                count = self.FONT.render(f'{quest.current_count}/{quest.object_count}', 1, 'black')
            self.WINDOW.blit(obj, (x+10,y))
            self.WINDOW.blit(count, (x+10, y+10))
        
            y += 25


        # draw a single frame
    def draw(self,player, cursor, cursor_color, player_info: Player, active_target, speaking: bool, accepting_quest=False):
        BG = pygame.image.load(f'assets/background/map{self.map.map_num}.png')
        self.WINDOW.blit(BG, (0,0))
        if not speaking:
            pygame.draw.circle(self.WINDOW, cursor_color, cursor, self.CURSOR_SIZE, self.CURSOR_THICKNESS) #Cursor
        self.draw_mobs(player_info)
        self.draw_UI(player_info)
        if active_target:
            self.draw_target_UI(active_target)
        self.draw_ability_bar(player_info.abilities)
        self.draw_combat_text()
        self.draw_announcement()
        self.draw_quest_tracker(player_info)
        pygame.draw.rect(self.WINDOW, (255,255,255), player)#Player model
        if speaking and active_target:
            self.draw_text_box(active_target, player_info)
        pygame.display.update()
    
    def update_map(self,map):
        self.map = map

    def __init__(self, WINDOW, map) -> None:
        pygame.init()
        pygame.font.init()
        self.combat_txt = []
        self.announcement = []
        self.open_quest=[]
        self.WINDOW = WINDOW
        self.map = map
        self.FONT = pygame.font.SysFont('comicsans', 15, True, italic=False)
        self.SMALLFONT = pygame.font.SysFont('comicsans', 10, True, italic=False)
        self.BIGFONT = pygame.font.SysFont('comicsans', 20, True, italic=False)
        self.LARGEFONT = pygame.font.SysFont('comicsans', 30, True, italic=False)