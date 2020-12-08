#Jogo da Velha
#Aluno: Joao Pedro de Paula Oliveira do Amaral / TIA: 32049390
#Aluno: Eric Felipeli Cesar Dias / TIA: 41911296
#Aluno: João Vitor Lima Lipert / TIA: 32088876
#Aluno: Thiago de Oliveira Aguirre / TIA: 32089589
#Aluno: Cássio Luis Junqueira Mellem Filho / TIA: 32089694

import pygame
import pygame_menu
from time import sleep

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
screen.fill(white)

pygame.font.init()
font = pygame.font.SysFont('Arial', 30)
#lista das coordenadas das areas
coords = [[215, 285, 165, 215], [285, 355, 165, 215], [355, 425, 165, 215], 
          [215, 285, 215, 265], [285, 355, 215, 265], [355, 425, 215, 265],
          [215, 285, 265, 315], [285, 355, 265, 315], [355, 425, 265, 315]]

#função que mostra quem ganha
def win(tab):
    #check row
    for row in range (3):
        if tab[row][0] == tab[row][1] == tab[row][2]:
            if tab[row][0] == 0:
                print("X ganhou")
                text = font.render('Jogador X ganhou', True, red)
                screen.blit(text, (215, 50))
                return False
            elif tab[row][0] == 1:
                print('O ganhou')
                text = font.render('Jogador O ganhou', True, red)
                screen.blit(text, (215, 50))
                return False

    #check column
    for col in range (3):
        if tab[0][col] == tab[1][col] == tab[2][col]:
            if tab[0][col] == 0:
                print("X ganhou")
                text = font.render('Jogador X ganhou', True, red)
                screen.blit(text, (215, 50))
                return False
            elif tab[0][col] == 1:
                print('O ganhou')
                text = font.render('Jogador O ganhou', True, red)
                screen.blit(text, (215, 50))
                return False

    #check main diagonal
    if tab[0][0] == tab[1][1] == tab[2][2]:
        if tab[0][0] == 0:
            print("X ganhou")
            text = font.render('Jogador X ganhou', True, red)
            screen.blit(text, (215, 50))
            return False
        elif tab[0][0] == 1:
            print('O ganhou')
            text = font.render('Jogador O ganhou', True, red)
            screen.blit(text, (215, 50))
            return False

    #check reverse diagonal
    if tab[0][2] == tab[1][1] == tab[2][0]:
        if tab[0][2] == 0:
            print("X ganhou")
            text = font.render('Jogador X ganhou', True, red)
            screen.blit(text, (215, 50))
            return False
        elif tab[0][2] == 1:
            print('O ganhou')
            text = font.render('Jogador O ganhou', True, red)
            screen.blit(text, (215, 50))
            return False

#função que cria a grade
def hashtag(color, screen):
    pygame.draw.line(screen, color, (215, 215), (425, 215), 5) #linha superior
    pygame.draw.line(screen, color, (215, 265), (425, 265), 5) #linha inferior
    pygame.draw.line(screen, color, (285, 165), (285, 315), 5) #linha da esquerda
    pygame.draw.line(screen, color, (355, 165), (355, 315), 5) #linha da direita

#função que faz o x
def xis(color, screen, x, y):
    pygame.draw.line(screen, color, (x, y), (x + 70, y + 50), 4)
    pygame.draw.line(screen, color, (x, y + 50), (x + 70, y), 4)
    
#função que faz o circulo
def circle(color, screen, x, y):
    pygame.draw.circle(screen, color, (x, y), 20, 4)

#função que mostra as regras do jogo
def regras():
    menu = pygame_menu.Menu(480, 640, 'Regras', theme=pygame_menu.themes.THEME_DARK)
    Regrastext = 'Dois jogadores escolhem uma marcação cada um, geralmente um círculo (O) e um xis (X).\n Os jogadores jogam alternadamente, uma marcação por vez, numa lacuna que esteja vazia.\n O objectivo é conseguir três círculos ou três xis em linha, quer horizontal, vertical ou diagonal , e ao mesmo tempo, quando possível, impedir o adversário de ganhar na próxima jogada.\n Quando um jogador conquista o objetivo, costuma-se riscar os três símbolos.'
    menu.add_label(Regrastext, max_char=-1, font_size=20)
    menu.add_button('Voltar', pygame_menu.events.BACK)
    menu.mainloop(screen)

#função que mostra o grupo criador do jogo
def grupo():
    menu = pygame_menu.Menu(480, 640, 'Grupo', theme=pygame_menu.themes.THEME_DARK)
    grupos = 'Joao Pedro de Paula Oliveira do Amaral - 32049390\n João Vitor Lima Lipert - 32088876\n Cássio Luis Junqueira Mellem Filho - 32089694\n Thiago de Oliveira Aguirre - 32089589\n Eric Felipeli Cesar Dias - 41911296'
    menu.add_label(grupos, max_char=-1, font_size=20)
    menu.add_button('Voltar', pygame_menu.events.BACK)
    menu.mainloop(screen)

#função que inicia o jogo
def game():
    screen.fill(white)
    pygame.display.flip()

    continuar = True
    moderator = 0
    quadrados_usados = 0

    #lista que represeta a tabela do jogo
    tab = [[None, None, None],
       [None, None, None],
       [None, None, None]]

    while continuar == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                button1 = pygame.mouse.get_pressed()[0]
                mousex, mousey = pygame.mouse.get_pos()

                for i in range(len(coords)):
                    if button1 == True and (mousex > coords[i][0] and mousex < coords[i][1]) and (mousey > coords[i][2] and mousey < coords[i][3]):
                        if moderator == 0:
                            moderator = 1
                            quadrados_usados += 1
                            xis(blue, screen, coords[i][0], coords[i][2])
                            print('X')

                            if i <= 2:
                                tab[0][i] = 0
                            elif i >= 3 and i <= 5:
                                a = i - 3
                                tab[1][a] = 0
                            elif i >= 6 and i <= 8:
                                a = i - 6
                                tab[2][a] = 0
                        elif moderator == 1:
                            moderator = 0
                            quadrados_usados += 1
                            circle(green, screen, coords[i][0]+35, coords[i][2]+25)
                            print('O')

                            if i <= 2:
                                tab[0][i] = 1
                            elif i >= 3 and i <= 5:
                                a = i - 3
                                tab[1][a] = 1
                            elif i >= 6 and i <= 8:
                                a = i - 6
                                tab[2][a] = 1

                print(tab)
                if win(tab) == False:
                    continuar = False
                elif quadrados_usados == 9:
                    continuar = False
                    print('Empate')
                    text = font.render('Empate', True, red)
                    screen.blit(text, (225, 50))

        hashtag(black, screen)            
        pygame.display.flip()
    sleep(3)

###MAIN
menu = pygame_menu.Menu(480, 640, 'bem-vindo', theme=pygame_menu.themes.THEME_DARK)

p1 = menu.add_text_input('Player 1: ', default='John')
p2 = menu.add_text_input('Player 2: ', default='Steve')
menu.add_button('Play', game)
menu.add_button('Grupo', grupo)
menu.add_button('Regras', regras)
#menu.add_button('Ranking', game)
menu.add_button('Quit', pygame_menu.events.EXIT)
menu.mainloop(screen)