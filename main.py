''' This is the main module. It is used to run the game.
    All the different modules are called here.
    Music: Payday by Jason Farham
    Player graphic: art by Kenney from opengameart.org '''
import pygame
import constants
import levels
from player import Player
import tkinter 
from tkinter import messagebox
from tkinter import ttk
from tkinter.messagebox import *
import time



def over():
    # Called when the game is over and asks for restart
    window = tkinter.Tk()    
    window.wm_withdraw()
    if askyesno('Restart','Do want to restart??'):
        main()
    else:
        pygame.quit()
        quit()
    
    
def level_ch():
    # Asks user if they want to proceed to next level
    window = tkinter.Tk()    
    window.wm_withdraw()
    if askyesno('Level Change','Do you want to go to next level?'):
        return
    else:
        over()
    

    
def time():
    #To display if its time up
    window = tkinter.Tk()    
    window.wm_withdraw()
    showerror('Timer','Time up!!!!')
    pygame.display.update()
    main()

    
    
def main():
    ''' Main Program'''
    pygame.init()

    # Set the height and width of the screen
    size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("A-maze-ing Game")

    # Create the player
    player = Player()

    # Create all the levels
    level_list = []
    level_list.append(levels.Level_1())
    level_list.append(levels.Level_2())
    level_list.append(levels.Level_3())

    # Set the current level
    current_level_no = 0
    current_level = level_list[current_level_no]

    active_sprite_list = pygame.sprite.Group()
    

    player.rect.x = 50
    player.rect.y = 50
    active_sprite_list.add(player)

    #Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    #font
    font = pygame.font.Font(None, 25)

    #Timer
    frame_count = 0
    frame_rate = 60
    start_time = 90
    
    #Music
    pygame.mixer.init()
    pygame.mixer.music.load("Payday - Jason Farnham - Bright Mood Pop Instrumental Music.mp3")
    pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
    pygame.mixer.music.play()
    if pygame.mixer.music.get_busy() == True:
        pygame.mixer.music.play()
        
    
    
    
    while not done:
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                done = True # Flag that we are done so we exit this loop

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.go_right()
                if event.key == pygame.K_UP:
                    player.go_up()
                if event.key == pygame.K_DOWN:
                    player.go_down()
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.stop()
                if event.key == pygame.K_UP and player.change_y < 0:
                    player.stop()
                if event.key == pygame.K_DOWN and player.change_y > 0:
                    player.stop()
            

            
          #Not needed. I was just checking the co-ordinates..
            if event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                print(position[0])
                print(position[1])

                

        # Update the player.
        player.update(current_level.wall_list)

        # Update items in the level
        current_level.update()

        if player.rect.x < 0 or player.rect.y < 0:
            player.rect.x = 0
            player.rect.y = 0
            player.stop()
            

        if player.rect.x > 801 or player.rect.y > 601:
            if current_level_no == 0:
                level_ch()
                current_level_no = 1
                current_level = level_list[current_level_no]
                player.rect.x = 50
                player.rect.y = 50
                start_time = 70
            elif current_level_no == 1:
                level_ch()
                current_level_no = 2
                current_level = level_list[current_level_no]
                player.rect.x = 50
                player.rect.y = 50
                start_time = 50
            else:
                over()
                
                
        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        
        screen.fill(constants.BLACK)         

        current_level.draw(screen)
        
        active_sprite_list.draw(screen)
        
        # Calculate total seconds
        total_seconds = start_time - (frame_count // frame_rate)
        if total_seconds < 0 or total_seconds == 0:
          time()  
 
        # Divide by 60 to get total minutes
        minutes = total_seconds // 60
     
        # Use modulus (remainder) to get seconds
        seconds = total_seconds % 60
     
        # Use python string formatting to format in leading zeros
        output_string = "Time left: {0:02}:{1:02}".format(minutes, seconds)
     
        # Blit to the screen
        text = font.render(output_string, True, constants.WHITE)   
        screen.blit(text,[635,620])
        
        #level indicator
        level_output = "Level: {0:02}".format(current_level_no+1) 
        text = font.render(level_output, True, constants.WHITE)   
        screen.blit(text,[20,620])
        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
        frame_count += 1
        
        # Limit to 60 frames per second
        # Limit to 20 frames per second
        clock.tick(frame_rate)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()

if __name__ == "__main__":
    main()


            


    
