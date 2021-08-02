import numpy as np
import math

class TicTacToePVP:
    def __init__(self, BOARD_ROWS, BOARD_COLS):
        self.BOARD_ROWS = BOARD_ROWS
        self.BOARD_COLS = BOARD_COLS
        self.board = np.zeros((BOARD_ROWS,BOARD_COLS))
        
    def mark_square(self, row, col, player):
        self.board[row][col] = player

    def square_available(self, row, col):
        return self.board[row][col] == 0

    def is_board_full(self):
        return 0 not in self.board

    