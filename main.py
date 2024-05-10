import sys
import pygame as pg

from consts import *
from game.game import Game


pg.init()
pg.display.set_caption('Jogo da Velha 8x8')
screen.fill(BG_COLOR)

def main():

    game = Game()
    board = game.board
    ia = game.ia
    while True:

        for event in pg.event.get():
            
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            if event.type == pg.KEYDOWN:

                # g-gamemode
                if event.key == pg.K_g:
                    game.gameMode()

                # r-restart
                if event.key == pg.K_r:
                    game.reset()
                    board = game.board
                    ia = game.ia

            # click event
            if event.type == pg.MOUSEBUTTONDOWN:
                pos = event.pos
                row = pos[1] // SQUARE_SIZE
                col = pos[0] // SQUARE_SIZE
                
                # human mark sqr
                if board.empty_square(row, col) and game.running:
                    game.make_move(row, col)

                    if game.over():
                        game.running = False


        # AI initial call
        if game.gamemode == 'ia' and game.player == 2 and game.running:
            
            pg.display.update()

            result = ia.eval(board)
            if result is not None:
                row, col = result
                game.make_move(row, col)

                if game.over():
                    game.running = False

        pg.display.update()


main()
