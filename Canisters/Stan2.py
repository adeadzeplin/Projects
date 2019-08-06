from classes import *
from pygame import *
from misc import *

class wall():       # A wall class that stores position, size, color, area,and center of block
    def __init__(self, xcoor, ycoor, width, height, color):
        # setup
        self.xcoor = xcoor
        self.ycoor = ycoor
        self.width = width
        self.height = height
        self.color = color
        self.area = pygame.Rect(self.xcoor, self.ycoor, self.width,self.height)
        self.cent = pygame.math.Vector2(self.xcoor + self.width/2, self.ycoor + self.height/2)


def render(list):       #Draws/Renders block in window
    for x in range (0, len(list)):
        pygame.draw.rect(WIN, white, list[x].area)
def Endscreen(inl):        #Funciton that displays Game Over on Window
    WIN.fill((1, 1, 1))
    draw_text(WIN, "Game Over!", 64, win_len / 2, win_ht / 4)
    draw_text(WIN, "Press a key to Quit ", 22, win_len / 2, win_ht / 2)
    pygame.display.flip()
    waiting = True

    while waiting:                                  #Waits for user to press a button, and once pressed the window willl quit and exit
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                pygame.quit()
                sys.exit()


def Winner():           #Function the displays Winner on Window
    WIN.fill((1, 1, 1))
    draw_text(WIN, "Winner!", 64, win_len / 2, win_ht / 4)
    draw_text(WIN, "Press a key to Quit", 22, win_len / 2, win_ht / 2)
    pygame.display.flip()
    waiting = True
    while waiting:                                  #Waits for user to press a button, and once pressed the window willl quit and exit
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                pygame.quit()
                sys.exit()


font_name = pygame.font.match_font('comicsanms')    #Initializes the font to be used when drawing words

def draw_text(surf, text, size, x, y):              #Funciton that prints text anywhere on window

    # font = pygame.font.Font(font_name, size)

    text_surface = font.render(text, True, white)

    text_rect = text_surface.get_rect()

    text_rect.midtop = (x, y)

    surf.blit(text_surface, text_rect)

def lvl_Logic(inVal):                               #Function that deals with rendering the level, with passing in the lvl value
    if inVal >= len(activelvl):                     #Check to see if the last level was reached, if true then display Winner
        Winner()

    render(activelvl[inVal])                        #Draws the selected level using the render function above

    draw_text(WIN, "Level=", 30,30,3)               #Draws the word 'level=' in the top left corner
    font = pygame.font.SysFont("comicsansms",30)   #Sets a font to a new variable
    text = font.render(str(inVal+1), 0, white)      # Sets the value of inVal+1 (which is the lvl value) to 'text'
    WIN.blit(text, (70, -10))                         # Prints the current level value in the window


def build_a_level(levelnum):
    wall_num = random.randint(2, (levelnum+2))
    new_level = []
    for x in range(0, wall_num):
        randx = random.randint(0, win_len - 100 )
        randy = random.randint(0, win_ht - 100 )
        randwt = random.randint(50, 400)
        randht = random.randint(50,  150)
        new_wall = wall(randx, randy, randwt, randht, white)
        new_level.append(new_wall)
    return new_level

total_level_num = 10
activelvl =[]        # Array with array of blocks placed within it
for x in range(0, total_level_num):
    temp_level = build_a_level(len(activelvl))
    activelvl.append(temp_level)





# activelvl.append(Level2)
# activelvl.append(Level3)
# activelvl.append(Level4)
# activelvl.append(Level5)


# wallA = wall(100,125,75,white) # level 1 Wall 1
# wallB = wall(100,225,75,white)
# wallC = wall(100,300,75,white)
# wallD = wall(100,375,75,white)
# wallE = wall(100,450,75,white)
# wallF = wall(100,625,75,white)
#
# wallG = wall(1025,125,75,white) # level 1 Wall 2
# wallH = wall(1025,225,75,white)
# wallI = wall(1025,300,75,white)
# wallJ = wall(1025,375,75,white)
# wallK = wall(1025,450,75,white)
# wallL = wall(1025,625,75,white)
#
# wallM = wall(500,200,200,white) # level 2 Wall 1
#
# wallN = wall(150,125,75,white) # Level 3 Wall 1
# wallO = wall(150,425,75,white) # Level 3 Wall 2
# wallP = wall(975,425,75,white) # Level 3 Wall 3
# wallQ = wall(975,125,75,white) # Level 3 Wall 4
#
# wallR = wall(200,win_ht/2,75,white) # Level 4 Wall 1
# wallS = wall(275,win_ht/2,75,white)
# wallT = wall(350,win_ht/2,75,white)
# wallU = wall(425,win_ht/2,75,white)
# wallV = wall(500,win_ht/2,75,white)
# wallW = wall(575,win_ht/2,75,white)
# wallX = wall(650,win_ht/2,75,white)
# wallY = wall(725,win_ht/2,75,white)
# wallZ = wall(800,win_ht/2,75,white)
# wallAA = wall(875,win_ht/2,75,white)
# wallBB = wall(950,win_ht/2,75,white)
#
# wallCC = wall(0,0,75,white)             # Level 5 Wall 1
# wallDD = wall(0,75,75,white)
# wallEE = wall(0,150,75,white)
# wallFF = wall(0,225,75,white)
# wallGG = wall(0,300,75,white)
# wallHH = wall(0,375,75,white)
# wallII = wall(0,450,75,white)
# wallJJ = wall(0,525,75,white)
#
# wallKK = wall(1125,0,75,white)             # Level 5 Wall 2
# wallLL = wall(1125,75,75,white)
# wallMM = wall(1125,150,75,white)
# wallNN = wall(1125,225,75,white)
# wallOO = wall(1125,300,75,white)
# wallPP = wall(1125,375,75,white)
# wallQQ = wall(1125,450,75,white)
# wallRR = wall(1125,525,75,white)
#
# wallSS = wall(75,0,75,white)             # Level 5 Wall 3
# wallTT = wall(150,0,75,white)
# wallUU = wall(225,0,75,white)
# wallVV = wall(300,0,75,white)
# wallWW = wall(375,0,75,white)
# wallXX = wall(450,0,75,white)
# wallYY = wall(525,0,75,white)
# wallZZ = wall(600,0,75,white)
# wallAAA = wall(675,0,75,white)
# wallBBB = wall(750,0,75,white)
# wallCCC = wall(825,0,75,white)
# wallDDD = wall(900,0,75,white)
# wallEEE = wall(975,0,75,white)
# wallFFF = wall(1050,0,75,white)
#
# wallGGG = wall(75,525,75,white)             # Level 5 Wall 4
# wallHHH = wall(150,525,75,white)
# wallIII = wall(225,525,75,white)
# wallJJJ = wall(300,525,75,white)
# wallKKK = wall(375,525,75,white)
# wallLLL = wall(450,525,75,white)
# wallMMM = wall(525,525,75,white)
# wallNNN = wall(600,525,75,white)
# wallOOO = wall(675,525,75,white)
# wallPPP = wall(750,525,75,white)
# wallQQQ = wall(825,525,75,white)
# wallRRR = wall(900,525,75,white)
# wallSSS = wall(975,525,75,white)
# wallTTT = wall(1050,525,75,white)
#
#
#
# Level1 =[]      # Array with blocks placed within it
# Level1.append(wallA)
# Level1.append(wallB)
# Level1.append(wallC)
# Level1.append(wallD)
# Level1.append(wallE)
# Level1.append(wallF)
# Level1.append(wallG)
# Level1.append(wallH)
# Level1.append(wallI)
# Level1.append(wallJ)
# Level1.append(wallK)
# Level1.append(wallL)
#
#
# Level2 =[]      # Array with blocks placed within it
# Level2.append(wallM)
#
# Level3 =[]      # Array with blocks placed within it
# Level3.append(wallN)
# Level3.append(wallO)
# Level3.append(wallP)
# Level3.append(wallQ)
#
# Level4 =[]      # Array with blocks placed within it
# Level4.append(wallR)
# Level4.append(wallS)
# Level4.append(wallT)
# Level4.append(wallU)
# Level4.append(wallV)
# Level4.append(wallW)
# Level4.append(wallX)
# Level4.append(wallY)
# Level4.append(wallZ)
# Level4.append(wallAA)
# Level4.append(wallBB)
#
#
# Level5 =[]       # Array with blocks placed within it
# Level5.append(wallCC)
# Level5.append(wallDD)
# Level5.append(wallEE)
# Level5.append(wallFF)
# Level5.append(wallGG)
# Level5.append(wallHH)
# Level5.append(wallII)
# Level5.append(wallJJ)
# Level5.append(wallKK)
# Level5.append(wallLL)
# Level5.append(wallMM)
# Level5.append(wallNN)
# Level5.append(wallOO)
# Level5.append(wallPP)
# Level5.append(wallQQ)
# Level5.append(wallRR)
#
#
# Level5.append(wallSS)
# Level5.append(wallTT)
# Level5.append(wallUU)
# Level5.append(wallVV)
# Level5.append(wallWW)
# Level5.append(wallXX)
# Level5.append(wallYY)
# Level5.append(wallZZ)
# Level5.append(wallAAA)
# Level5.append(wallBBB)
# Level5.append(wallCCC)
# Level5.append(wallDDD)
# Level5.append(wallEEE)
# Level5.append(wallFFF)
#
# Level5.append(wallGGG)
# Level5.append(wallHHH)
# Level5.append(wallIII)
# Level5.append(wallJJJ)
# Level5.append(wallKKK)
# Level5.append(wallLLL)
# Level5.append(wallMMM)
# Level5.append(wallNNN)
# Level5.append(wallOOO)
# Level5.append(wallPPP)
# Level5.append(wallQQQ)
# Level5.append(wallRRR)
# Level5.append(wallSSS)
# Level5.append(wallTTT)
#
#
# Level6 = []
#
#
#
#







