import random

from consts import *

class IA:
    
    def __init__(self, player=2):
        self.player = player

    def iddfs(self, board, max_depth):
        best_move = None

        for depth in range(1, max_depth + 1):
            eval, move = self.minimax(board, depth)
            best_move = move
        return best_move

    def minimax(self, board, depth, alpha, beta, maximizing):
        # terminal case
        case = board.final_state()

        # player 1 wins
        if case == 1:
            return 1, None

        # player 2 wins
        if case == 2:
            return -1, None

        # draw or depth limit reached
        empty_squares = board.get_empty_squares()
        if not empty_squares or depth == 0:
            return 0, empty_squares[0] if empty_squares else None
        
        random.shuffle(empty_squares)

        if maximizing:
            max_eval = -100
            best_move = None

            for (row, col) in empty_squares:
                board.mark_square(row, col, 1)
                eval, _ = self.minimax(board, depth-1, alpha, beta, False)
                board.mark_square(row, col, 0)
                if eval > max_eval:
                    max_eval = eval
                    best_move = (row, col)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval, best_move

        else:
            min_eval = 100
            best_move = None

            for (row, col) in empty_squares:
                board.mark_square(row, col, self.player)
                eval, _ = self.minimax(board, depth-1, alpha, beta, True)
                board.mark_square(row, col, 0)
                if eval < min_eval:
                    min_eval = eval
                    best_move = (row, col)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval, best_move

    def eval(self, board):
        eval, move = self.minimax(board, 3, -np.inf, np.inf, True)
        print(f'AI has chosen to mark the square in pos {move} with an eval of: {eval}')
        return move