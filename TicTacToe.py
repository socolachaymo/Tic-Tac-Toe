import pygame
import logic
import random
from time import sleep

pygame.init()
window = pygame.display.set_mode((255,255))
pygame.display.set_caption('Tic Tac Toe')

screen = 255
player1 = pygame.image.load('Images/x.png')
player = player1.copy()
player = pygame.transform.scale(player, (60,60))
computer1 = pygame.image.load('Images/o.png')
computer = computer1.copy()
computer = pygame.transform.scale(computer, (60,60))
bg_board = pygame.image.load('Images/board.gif')
won = pygame.image.load('Images/win.jpg')
win = won.copy()
win = pygame.transform.scale(win, (screen,screen))
lost = pygame.image.load('Images/lose.png')
lose = lost.copy()
lose = pygame.transform.scale(lose, (screen,screen))

board = logic.start_game()

window.fill((255,255,255))
window.blit(bg_board, (13,13))
pygame.display.flip()

played = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()
            r = y//85
            c = x//85
            if board[r][c] == ' ':
                board[r][c] = 'X'
                played = True
            if played == True:
                window.blit(player, (c*85+13,r*85+13))
                pygame.display.update()
                status = logic.current_state(board)
                if status == 'Next turn':
                    pass 
                else:
                    sleep(1)
                    if status == 'You Win':
                        window.blit(win, (0,0))
                        pygame.display.flip()
                    else:
                        window.blit(lose, (0,0))
                        pygame.display.flip()
                    sleep(1)
                    running = False
                r = random.randint(0,2)
                c = random.randint(0,2)
                while board[r][c] != ' ':
                    r = random.randint(0,2)
                    c = random.randint(0,2)
                board[r][c] = 'O'
                window.blit(computer, (c*85+13,r*85+13))
                pygame.display.update()
                played = False
                status = logic.current_state(board)
                if status == 'Next turn':
                    pass 
                else:
                    sleep(1)
                    if status == 'You Win':
                        window.blit(win, (0,0))
                        pygame.display.flip()
                    else:
                        window.blit(lose, (0,0))
                        pygame.display.flip()
                    sleep(1)
                    running = False