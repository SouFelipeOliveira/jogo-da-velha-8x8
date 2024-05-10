from consts import *

class Board:
    
    def __init__(self):
        self.squares = np.zeros((ROWS, COLS))
        self.empty_square_array = self.squares
        self.marked_squares = 0


    def final_state(self, show=False):
        '''
        0: no winner
        1: player 1 wins
        2: player 2 wins
        '''

        #check rows
        for row in range(ROWS):
            for col in range(COLS - 3):
                if self.squares[row][col] == self.squares[row][col+1] == self.squares[row][col+2] == self.squares[row][col+3] != 0:
                    if show:
                        pg.draw.line(screen, LINE_RED, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), ((col+3) * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), LINE_WIDTH)
                    return self.squares[row][col]
                
        #check columns
        for col in range(COLS):
            for row in range(ROWS - 3):
                if self.squares[row][col] == self.squares[row+1][col] == self.squares[row+2][col] == self.squares[row+3][col] != 0:
                    if show:
                        pg.draw.line(screen, LINE_RED, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), (col * SQUARE_SIZE + SQUARE_SIZE // 2, (row+3) * SQUARE_SIZE + SQUARE_SIZE // 2), LINE_WIDTH)
                    return self.squares[row][col]

        #check diagonals
        for row in range(ROWS - 3):
            for col in range(COLS - 3):
                if self.squares[row][col] == self.squares[row+1][col+1] == self.squares[row+2][col+2] == self.squares[row+3][col+3] != 0:
                    if show:
                        pg.draw.line(screen, LINE_RED, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), ((col+3) * SQUARE_SIZE + SQUARE_SIZE // 2, (row+3) * SQUARE_SIZE + SQUARE_SIZE // 2), LINE_WIDTH)
                    return self.squares[row][col]

        for row in range(3, ROWS):
            for col in range(COLS - 3):
                if self.squares[row][col] == self.squares[row-1][col+1] == self.squares[row-2][col+2] == self.squares[row-3][col+3] != 0:
                    if show:
                        pg.draw.line(screen, LINE_RED, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), ((col+3) * SQUARE_SIZE + SQUARE_SIZE // 2, (row-3) * SQUARE_SIZE + SQUARE_SIZE // 2), LINE_WIDTH)
                    return self.squares[row][col]
        
        #no winner
        return 0


    def mark_square(self, row, col, player):
        self.squares[row][col] = player
        self.marked_squares += 1

    def empty_square(self, row, col):
        return self.empty_square_array[row][col] == 0
    
    def get_empty_squares(self):    
        empty_squares = []
        for row in range(ROWS):
            for col in range(COLS):
                if self.empty_square(row, col):
                    empty_squares.append((row, col))
        return empty_squares
    

    def is_full(self):
        return self.mark_square == ROWS * COLS
    
    def is_empty(self):
        return self.mark_square == 0