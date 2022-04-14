import pygame
import os


WIDTH, HEIGHT = 900, 500  # set width and heigh of the game screen
WIN = pygame.display.set_mode((WIDTH, HEIGHT))  # initiate the game window
pygame.display.set_caption("My first pygame game")  # change the title

WHITE = (255, 255, 255)  # set constant value for white color

def draw_window():
    'function to update pygame window'
    WIN.fill(WHITE)  # set the background color for pygame window
    WIN.blit(RAIDEN_IMAGE, (150 , 150))  # display the object with give coordinate
    pygame.display.update()  # update display

FPS = 60  # set the frame rate

RAIDEN_IMAGE =  pygame.image.load(
    os.path.join('raiden.png'))
RAIDEN = pygame.transform.scale(RAIDEN_IMAGE, (75, 75))

YAE_IMAGE =  pygame.image.load(
    os.path.join('yae.png'))
YAE = pygame.transform.scale(YAE_IMAGE, (75, 75))


def draw_window():
    """function to update pygame window"""
    WIN.fill(WHITE)  # set the background color for pygame window
    WIN.blit(RAIDEN, (150, 150))  # display the object with give coordinate
    WIN.blit(YAE, (150, 150))
    pygame.display.update()  # update display
    

def main():
    
    clock = pygame.time.Clock()  # initiate the clock variable for controling framerate
    run = True
    while run:
        clock.tick(FPS)  # control the framerate
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window()

    pygame.quit()


if __name__ == "__main__":
    main()