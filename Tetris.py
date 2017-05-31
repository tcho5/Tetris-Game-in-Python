import pygame, sys
from Board import *
from random import *

SPEED = 550

class Tetris:
    def __init__(self):
        pygame.init()

        pygame.mixer.music.load('tetrisb.mid')
        
        pygame.mixer.music.play(-1, 0.0)
        
        tetrisBoard = Board()

        screen = pygame.display.set_mode((30*tetrisBoard.COLS,\
                                          30*tetrisBoard.ROWS))
        
        self.color = (randint(0,255), randint(0, 255), randint(0, 255))

        ctr = 0

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        tetrisBoard.left()
                    if event.key == pygame.K_RIGHT:
                        tetrisBoard.right()
                    if event.key == pygame.K_UP:
                        tetrisBoard.up()
                    if event.key == pygame.K_DOWN:
                        tetrisBoard.down()
                    if event.key == pygame.K_SPACE:
                        tetrisBoard.hardDrop()
                    if event.key == pygame.K_LSHIFT:
                        tetrisBoard.hold()

            if ctr % SPEED == 0:
                tetrisBoard.down()                
                        
            screen.fill((255,255,255))

            for x, row in enumerate(tetrisBoard.board):
                for y, col in enumerate(row):
                    if col:
                        pygame.draw.rect(screen, tetrisBoard.color, \
                                         (y * 30, x * 30, 30, 30))
                    
            pygame.display.flip()
            ctr += 1
