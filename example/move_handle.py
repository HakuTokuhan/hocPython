from tkinter import Y
import pygame
import os

WIDTH, HEIGHT = 900, 500  # set width and height of the game screen
WIN = pygame.display.set_mode((WIDTH, HEIGHT))  # initiate the game window
pygame.display.set_caption("My first pygame game")  # change the title

WHITE = (255, 255, 255)  # set constant value for white color

FPS = 60  # set the frame rate

CHARACTER_WIDTH = 50
CHARACTER_HEIGHT = 50

VELOCITY = 10

RAIDEN_IMAGE =  pygame.image.load(
    os.path.join('raiden.png'))
RAIDEN = pygame.transform.scale(RAIDEN_IMAGE, (75, 75))

YAE_IMAGE =  pygame.image.load(
    os.path.join('yae.png'))
YAE = pygame.transform.scale(YAE_IMAGE, (75, 75))

def draw_window(player_raiden, player_yae):
    """function to update pygame window"""
    WIN.fill(WHITE)  # set the background color for pygame window
    WIN.blit(RAIDEN, (player_raiden.x, player_raiden.y))  # display the object with give coordinate
    WIN.blit(YAE, (player_yae.x, player_yae.y))  # display the object with give coordinate
    pygame.display.update()  # update display

def raiden_movement_handle(keys_pressed, player_raiden):
    if keys_pressed[pygame.K_a]:  # check a key pressed
        player_raiden.x -= VELOCITY  # move left
    if keys_pressed[pygame.K_d]:  # check d key pressed
        player_raiden.x += VELOCITY  # move right
    if keys_pressed[pygame.K_w]:  # check w key pressed
        player_raiden.y -= VELOCITY  # move up
    if keys_pressed[pygame.K_s]:  # check s key pressed
        player_raiden.y += VELOCITY  # move down
        
def yae_movement_handle(keys_pressed, player_yae):
    if keys_pressed[pygame.K_j]:  # check a key pressed
        player_yae.x -= VELOCITY  # move left
    if keys_pressed[pygame.K_l]:  # check d key pressed
        player_yae.x += VELOCITY  # move right
    if keys_pressed[pygame.K_i]:  # check w key pressed
        player_yae.y -= VELOCITY  # move up
    if keys_pressed[pygame.K_k]:  # check s key pressed
        player_yae.y += VELOCITY  # move down
        
        
def main():
    # create pygame rectangle objects to control the characters
    player_raiden = pygame.Rect(50, 50, 50, 50)  # instantiate a pygame Rect (X, Y, width, height)
    player_yae = pygame.Rect(50, 50, 50, 50)  # instantiate a pygame Rect (X, Y, width, height)

    clock = pygame.time.Clock()  # initiate the clock variable for controlling frame rate
    run = True
    while run:
        clock.tick(FPS)  # control the frame rate
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()
        raiden_movement_handle(keys_pressed, player_raiden)
        yae_movement_handle(keys_pressed, player_yae)
        draw_window(player_yae, player_raiden)

    pygame.quit()


if __name__ == "__main__":
    main()