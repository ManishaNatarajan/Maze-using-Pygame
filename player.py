''' This module creates the player.
    The player is the only user controlled sprite on screen.'''
import pygame
import constants

import levels
from spritesheet_function import SpriteSheet

class Player(pygame.sprite.Sprite):
    # This class represents the player
    walls = pygame.sprite.Group()

    #Speed control
    change_x = 0
    change_y = 0

    #This holds all the images for animated walk right/left
    walking_frames_l = []
    walking_frames_r = []
    walking_frames_u = []
    walking_frames_d = []
    
    # What direction is the player facing?
    direction = "R"
    

    def __init__(self):
        """ Constructor function """

        # Call the parent's constructor
        super().__init__()

        sprite_sheet = SpriteSheet("p1_walk.png")
        # Load all the right facing images into a list
        image = sprite_sheet.get_image(0, 0, 66, 90)
        self.walking_frames_r.append(image)
        self.walking_frames_u.append(image)
        self.walking_frames_d.append(image)
        image = sprite_sheet.get_image(66, 0, 66, 90)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(132, 0, 67, 90)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(0, 93, 66, 90)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(66, 93, 66, 90)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(132, 93, 72, 90)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(0, 186, 70, 90)
        self.walking_frames_r.append(image)

        # Load all the right facing images, then flip them
        # to face left.
        image = sprite_sheet.get_image(0, 0, 66, 90)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(66, 0, 66, 90)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(132, 0, 67, 90)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(0, 93, 66, 90)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(66, 93, 66, 90)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(132, 93, 72, 90)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(0, 186, 70, 90)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)

        # Set the image the player starts with
        self.image = self.walking_frames_r[0]

        # Set a referance to the image rect.
        self.rect = self.image.get_rect()
        #self.level = levels.wall_list

        
    def update(self, wall):
        """ Move the player. """
        
        # Move left/right
        self.rect.x += self.change_x
        self.rect.y += self.change_y
        pos = self.rect.x
        Pos = self.rect.y
        
        if self.direction == "R":
            frame = (pos // 30) % len(self.walking_frames_r)
            self.image = self.walking_frames_r[frame]
        elif self.direction == "L":
            frame = (pos // 30) % len(self.walking_frames_l)
            self.image = self.walking_frames_l[frame]
        

        block_hit_list = pygame.sprite.spritecollide(self, wall, False)
        for block in block_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right

        if self.direction == "U":
            self.image = self.walking_frames_u[0]
        elif self.direction == "D":
            self.image = self.walking_frames_d[0]

        #Move up/down
        self.rect.y += self.change_y
        
        block_hit_list = pygame.sprite.spritecollide(self, wall, False)
        for block in block_hit_list:

            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom

    

    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.change_x = -6
        self.direction = "L"

    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.change_x = 6
        self.direction = "R"

    def go_up(self):
        """ Called when the user hits the up arrow. """
        self.change_y = -6
        self.direction = "U"

    def go_down(self):
        """ Called when the user hits the down arrow. """
        self.change_y = 6
        self.direction = "D"

    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.change_x = 0
        self.change_y = 0





        
            
        
