''' There is a Levels parent class from which all levels inherit.
    This module is used to create different mazes in different levels'''


import pygame
import constants



class Wall(pygame.sprite.Sprite):
    ''' This class is used to create walls
        It will be called individually for different rooms'''
   
    def __init__(self, x, y, width, height, colour):

        # Call the parent's constructor
        super().__init__()
 
        # Make a blue wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(colour)

        # Make our top-left corner the  user passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

class Level(object):
    '''Each level has a set of walls, nos. and enemies'''
    wall_list = None
    #enemy_sprites = None !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    num_list = None
    def __init__(self):
        #Constructor. Creates a list of walls n other stuff in each level
        self.wall_list = pygame.sprite.Group()
        #self.enemy_sprites = pygame.sprite.Group()
        self.num_list = pygame.sprite.Group()

    def update(self):
        #Update everything in each level
        self.wall_list.update()
        #self.enemy_sprites.update()
        self.num_list.update()

    def draw(self, screen):
        screen.fill(constants.BLACK)
        self.wall_list.draw(screen)
        #self.enemy_sprites.draw(screen)
        self.num_list.draw(screen)
       

class Level_1(Level):
    ''' This creates all the walls and enemies in level 1'''
    def __init__(self):
        super().__init__()
        walls = [[0, 0, 10, 600 ],
                 [255, 10, 10, 90],
                 [255, 90, 245, 10],
                 [110, 150, 10, 250],
                 [265, 290, 245, 10],
                 [600, 200, 100, 10],
                 [410, 400, 190, 10],
                 [710, 300, 80, 10],
                 [600, 200, 10, 210],
                 [400, 550, 90, 10],
                 [490, 550, 10, 40],
                 [400, 400, 10, 150],
                 [500, 90, 10, 200],
                 [10, 590, 790, 10],
                 [790, 10, 10, 480],
                 [255, 200, 10, 300],
                 [10, 0, 790, 10],
                 [85, 490, 180, 10],
                 [10, 200, 100, 10]]
        #Now to create the walls.....
        for i in walls:
            wall = Wall(i[0], i[1], i[2], i[3], constants.BLUE)
            self.wall_list.add(wall)

class Level_2(Level):
    ''' This creates all the walls and enemies in level 2'''
    def __init__(self):
        super().__init__()
        walls = [[0, 0, 10, 600],
                 [110, 0, 690, 10],
                 [80,241,60,9],
                 [348,79,10,122],
                 [352,79,200,10],
                 [80, 190, 10, 55],
                 [220, 200, 200, 10],
                 [469,179,230,10],
                 [10, 590, 790, 10],
                 [11,347,100,10],
                 [130, 250, 10, 150],
                 [258,270,100,10],
                 [249,338,100,10],
                 [303,278,10,60],
                 [547,79,10,100],
                 [698,9,10,250],
                 [470, 350, 10, 100],
                 [470,502,10,95],
                 [470, 500, 100, 10],
                 [308,490,10,105],            
                 [620,308,70,10],
                 [110, 490, 200, 10],
                 [680,315,10,120],
                 [680,433,50,10],
                 [790,10,10,490]]
        for j in walls:
            wall = Wall(j[0], j[1], j[2], j[3], constants.RED)
            self.wall_list.add(wall)
    

        
class Level_3(Level):
    ''' This creates all the walls and enemies in level 3'''
    def __init__(self):
        super().__init__()
        walls = [[0, 0, 10, 600],
                 [110, 0, 690, 10],
                 [110, 10, 10, 20],
                 [790, 10, 10, 490],
                 [120, 120, 100, 10],
                 [120, 130, 10, 50],
                 [80, 180, 50, 10],
                 [80, 190, 10, 50],
                 [80, 240, 120, 10],
                 [200, 200, 10, 50],
                 [210, 200, 200, 10],
                 [300, 130, 10, 70],
                 [400, 200, 10, 100],
                 [410, 250, 100, 10],
                 [510, 210, 10, 50],
                 [520, 210, 100, 10],
                 [420, 10, 10, 100],
                 [430, 100, 50, 10],
                 [620, 100, 10, 120],
                 [10, 590, 790, 10],
                 [720, 130, 70, 10],
                 [130, 250, 10, 150],
                 [130, 400, 350, 10],
                 [260, 280, 10, 120],
                 [745, 450, 55, 10],
                 [470, 350, 10, 50],
                 [470, 350, 200, 10],
                 [570, 500, 10, 90],
                 [470, 500, 100, 10],
                 [340, 410, 10, 90],
                 [10, 530, 100, 10],
                 [700, 250, 90, 10],
                 [80, 350, 60, 10],
                 [110, 490, 100, 10],
                 [660, 350, 10, 240],
                 [745, 350, 10, 100]]
        for j in walls:
            wall = Wall(j[0], j[1], j[2], j[3], constants.GREEN)
            self.wall_list.add(wall)
  
