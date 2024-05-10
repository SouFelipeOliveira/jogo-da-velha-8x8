from consts import *

from game.board import Board
from game.ia import IA

class Game:
        
    def __init__(self):
        self.board = Board()
        self.ia = IA()
        self.player = 1
        self.gamemode = 'ia'
        self.running = True
        self.show_lines()


    #|------ DRAW METHODS ------|
    
    
    def show_lines(self):

        screen.fill(BG_COLOR)
        # DRAW LINES VERTICALLY
        for i in range(1, ROWS):
            pg.draw.line(screen, LINE_COLOR, (0, i * SQUARE_SIZE), (WIDTH, i * SQUARE_SIZE), LINE_WIDTH)
            pg.draw.line(screen, LINE_COLOR, (i * SQUARE_SIZE, 0), (i * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

        # DRAW LINES HORIZONTALLY
        for i in range(1, COLS):
            pg.draw.line(screen, LINE_COLOR, (0, i * SQUARE_SIZE), (WIDTH, i * SQUARE_SIZE), LINE_WIDTH)
            pg.draw.line(screen, LINE_COLOR, (i * SQUARE_SIZE, 0), (i * SQUARE_SIZE, HEIGHT), LINE_WIDTH)
    
    def draw_fig(self, row, col):
            
        if self.player == 1:
            #draw cross
            center = (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2)
            pg.draw.line(screen, CROSS_COLOR, (center[0] - RADIUS, center[1] - RADIUS), (center[0] + RADIUS, center[1] + RADIUS), CROSS_WIDTH)
            pg.draw.line(screen, CROSS_COLOR, (center[0] + RADIUS, center[1] - RADIUS), (center[0] - RADIUS, center[1] + RADIUS), CROSS_WIDTH)
        
        if self.player == 2:
            #draw circle
            center = (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2)
            pg.draw.circle(screen, CIRC_COLOR, center, RADIUS, CIRC_WIDTH)


        
    #|------ OTHER SOME METHODS ------|


    def make_move(self, row, col):
        self.board.mark_square(row, col, self.player)
        self.draw_fig(row, col)
        self.next_turn()

    def next_turn(self):
        self.player = self.player % 2 + 1

    def gameMode(self):
        self.gamemode = 'ia' if self.gamemode == 'pvp' else 'pvp'

    def over(self):
        return self.board.final_state(show=True) != 0 or self.board.is_full()

    def reset(self):
        self.__init__()

