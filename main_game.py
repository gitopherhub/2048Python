from game_logic import App2048
import sys
import json
import pygame
from pygame.locals import *

# set up pygame for main gameplay
pygame.init()
pygame.font.init()

#this file contains all the formats, font, and colors for 
#the game in a dictionary in a json file
file = open("formats.json", mode = "r")
formats = json.load(file)

#setting up the screen and font for the game, creating the main board
screen = pygame.display.set_mode((formats["size_y"], formats["size_x"]))
my_font = pygame.font.SysFont(formats["font"], formats["game_font_size"], bold=True)
sidebar_font = pygame.font.SysFont(formats["font"], formats["sidebar_font_size"], bold=True)
title_controls_font = pygame.font.SysFont(formats["font"], int(formats["sidebar_font_size"]/1.15), bold=True)
controls_font = pygame.font.SysFont(formats["font"], int(formats["sidebar_font_size"]/1.25), bold=False)
gameover_font = pygame.font.SysFont(formats["font"], formats["gameover_font_size"])
global over
over = False

'''whenever the code is run and this function is called
there will be a new game'''
def newGame():
    #creating a global variable for the board that we can call anywhere in the code
    #this variable is an object in the App2048 class that can be modified
    global game1
    game1 = App2048()
    game1.preGameSetUp()
    display(game1, over)

'''creating a function that updates the display after every move. There will be some animations using sprite module in python'''
def display(boardnum, over_check):
    pygame.display.set_caption('2048 Game by Sai Chanda, Chris Siems, and Sam Szymanski')
    board_copy = boardnum.copy()
    #creates background for game, box size per cube, and gets the padding from that json file
    screen.fill(tuple(formats["colors"]["background"]))
    box = formats["size_x"] // 4
    padding = formats["padding"]
    #creating the box for each cube, filling it with the color based on the rgb values from json file
    for y in range(4):
        for x in range(4):
            color = tuple(formats["colors"][str(boardnum.board[y][x])])
            pygame.draw.rect(screen, color, (x * box + padding,
                                             y * box + padding,
                                             box - 2 * padding,
                                             box - 2 * padding), 0)
            if boardnum.board[y][x] == 0:
                text_color = color
            elif boardnum.board[y][x] in (2,4):
                text_color = formats["colors"]["text"]
            else:
                text_color = tuple((255,255,255))
            screen.blit(my_font.render('{:>3}'.format(boardnum.board[y][x]), True, text_color), (x * box + 4 * padding, y * box + 7 * padding))

    pygame.draw.rect(screen, formats['colors']['sidebar'],  (905, 10, formats['size_x'] - 620 , formats['size_y'] - 320), 0)

    score_text = sidebar_font.render('Score:', True, formats["colors"]["text"])
    score_count = sidebar_font.render(str(boardnum.score), True, formats["colors"]["text"])
    move_text = sidebar_font.render('Your Move: ' + boardnum.move_name, True, formats["colors"]["text"])
    game_controls_text = title_controls_font.render('Game Controls:', True, formats["colors"]["text"])
    w_control = controls_font.render('W or ^:            Up', True, formats["colors"]['text'])
    a_control = controls_font.render('A or <:            Left', True, formats["colors"]['text'])
    s_control = controls_font.render('S or v:            Down', True, formats["colors"]['text'])
    d_control = controls_font.render('D or >:            Right', True, formats["colors"]['text'])
    q_control = controls_font.render('Q:                 Quit', True, formats["colors"]['text'])
    

    score_textRect = score_text.get_rect()
    score_countRect = score_count.get_rect()
    move_textRect = move_text.get_rect()
    game_controls_textRect = game_controls_text.get_rect()
    w_controlRect = w_control.get_rect()
    a_controlRect = s_control.get_rect()
    s_controlRect = s_control.get_rect()
    d_controlRect = d_control.get_rect()
    q_controlRect = q_control.get_rect()

    score_textRect.topleft = (920, 100)
    score_countRect.topleft = (920, 150)
    move_textRect.topleft = (920, 250)
    game_controls_textRect.topleft = (940, 400)
    w_controlRect.topleft = (950, 450)
    a_controlRect.topleft = (950, 475)
    s_controlRect.topleft = (950, 500)
    d_controlRect.topleft = (950, 525)
    q_controlRect.topleft = (950, 550)

    screen.blit(game_controls_text,game_controls_textRect)
    screen.blit(score_text, score_textRect)
    screen.blit(score_count, score_countRect)
    screen.blit(move_text, move_textRect)
    screen.blit(w_control, w_controlRect)
    screen.blit(a_control, a_controlRect)
    screen.blit(s_control, s_controlRect)
    screen.blit(d_control, d_controlRect)
    screen.blit(q_control, q_controlRect)
    
    if over_check:
        size_x = formats['size_x']
        size_y = formats['size_y']
        s = pygame.Surface((size_x, size_y), pygame.SRCALPHA)
        s.fill(formats["colors"]["game_over"])
        screen.blit(s, (0, 0))
        gameOverText = gameover_font.render('Game Over', True, formats["colors"]["text"])
        gameOverTextRect = gameOverText.get_rect()
        gameOverTextRect.center = ((900-90)/2 + 50,400)
        screen.blit(gameOverText,gameOverTextRect)

    pygame.display.update()

def playGame(boardnum):
    running  = True
    while running :
        for event in pygame.event.get():
            over = False
            if event.type == QUIT or event.type == pygame.KEYDOWN and event.key == K_q:
                    running = False
            elif event.type == pygame.KEYDOWN and str(event.key) not in formats['''buttons''']:
                continue
            elif event.type == pygame.KEYDOWN and not over:
                key = formats['buttons'][str(event.key)]
                if key == 'w':
                    c = boardnum.copy()
                    boardnum.fullUp()
                    if c.board != boardnum.board:
                        boardnum.pickTwoOrFour()
                    display(boardnum, over)
                elif key == 'a':
                    c = boardnum.copy()
                    boardnum.fullLeft()
                    if c.board != boardnum.board:
                        boardnum.pickTwoOrFour()
                    display(boardnum, over)
                elif key == 's':
                    c = boardnum.copy()
                    boardnum.fullDown()
                    if c.board != boardnum.board:
                        boardnum.pickTwoOrFour()
                    display(boardnum, over)
                elif key == 'd':
                    c = boardnum.copy()
                    boardnum.fullRight()
                    if c.board != boardnum.board:
                        boardnum.pickTwoOrFour()
                    display(boardnum, over)
                #checking status of the game
                if boardnum.check():
                    continue
                else:
                    over = True
                    display(boardnum, over)
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if str(event.key) not in formats['buttons']:
                                key == formats['buttons'][str(event.key)]
                                if key == 'n':
                                    pygame.quit()
                                    sys.exit()
                                elif key == 'y':
                                    boardnum.define([[0] * 4, [0] * 4, [0] * 4,  [0] * 4])

                                    display(game1)
                                    playGame(game1)

                                

if __name__ == '__main__':
    json.load(open('formats.json', mode = 'r'))
    file.close()
    pygame.init()
    newGame()
    playGame(game1)