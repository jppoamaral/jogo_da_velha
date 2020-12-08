import pygame
import pygame_menu

#colors
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)

#init
pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Tic-Tac-Toe')
screen.fill((255, 255, 255))
continuar = True
moderator = 0
quadrados_usados = 0
def game():
    pass
menu = pygame_menu.Menu(480, 640, 'Welcome', theme=pygame_menu.themes.THEME_BLUE)

menu.add_text_input('Name :', default='John Doe')
menu.add_button('Play', game)
menu.add_button('Quit', pygame_menu.events.EXIT)   



menu.mainloop(screen)