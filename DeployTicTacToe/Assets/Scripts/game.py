import pygame, sys

# Initialize PyGame
pygame.init()

# Constants
LINE_WIDTH = 15
CIRCLE_WIDTH = 15
CIRCLE_RADIUS = 75
CROSS_WIDTH = 15
SPACE = 50
WINLINE_WIDTH = 200

# Colors
BG_COLOR = (88,107,164)
LINE_COLOR = (50,67,118)
CIRCLE_COLOR = (245,221,144)
CROSS_COLOR = (246,142,95)
WINLINE_COLOR = (247,108,94)



class StartGame:
    def __init__(self, board, BOARD_COLS, BOARD_ROWS, WIDTH, HEIGHT):
        self.BOARD_COLS = BOARD_COLS
        self.BOARD_ROWS = BOARD_ROWS
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.board = board

        # Initialize Screen
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Tic Tac Toe")
        self.screen.fill(BG_COLOR)


    def draw_lines(self):
        """ Draw Boarder """
        pygame.draw.line(self.screen, LINE_COLOR, (0,0), (0,self.HEIGHT), LINE_WIDTH)
        pygame.draw.line(self.screen, LINE_COLOR, (0,0), (self.WIDTH,0), LINE_WIDTH)
        pygame.draw.line(self.screen, LINE_COLOR, (self.WIDTH,0), (self.WIDTH,self.HEIGHT), LINE_WIDTH)
        pygame.draw.line(self.screen, LINE_COLOR, (0,self.HEIGHT), (self.WIDTH,self.HEIGHT), LINE_WIDTH)

        """ Draw Grid """
        # Horizontal 1
        pygame.draw.line(self.screen, LINE_COLOR, (0,int(self.WIDTH/3)), (self.WIDTH,int(self.WIDTH/3)), LINE_WIDTH)
        # Horizontal 2
        pygame.draw.line(self.screen, LINE_COLOR, (0,2*int(self.WIDTH/3)), (self.WIDTH,2*int(self.WIDTH/3)), LINE_WIDTH)
        
        # Vertical 1
        pygame.draw.line(self.screen, LINE_COLOR, (int(self.HEIGHT/3),0), (int(self.HEIGHT/3),self.HEIGHT), LINE_WIDTH)
        # Horizontal 2
        pygame.draw.line(self.screen, LINE_COLOR, (2*int(self.HEIGHT/3),0), (2*int(self.HEIGHT/3),self.HEIGHT), LINE_WIDTH)
        

    def draw_figures(self):
        for row in range(self.BOARD_ROWS):
            for col in range(self.BOARD_COLS):
                if self.board[row][col] == 1:
                    pygame.draw.circle(self.screen, CIRCLE_COLOR, (int(col*(self.WIDTH/3)+(self.WIDTH/6)), int(row*(self.HEIGHT/3)+(self.HEIGHT/6))), CIRCLE_RADIUS, CIRCLE_WIDTH)

                elif self.board[row][col] == 2:
                    pygame.draw.line(self.screen, CROSS_COLOR, (int(col*(self.WIDTH)/3)+SPACE, int(row*(self.HEIGHT/3)+(self.HEIGHT/3)-SPACE)), (int(col*(self.WIDTH/3)+(self.WIDTH/3)-SPACE), int(row*(self.HEIGHT/3)+SPACE)), CROSS_WIDTH)
                    pygame.draw.line(self.screen, CROSS_COLOR, (int(col*(self.WIDTH)/3)+SPACE, int(row*(self.HEIGHT/3)+SPACE)), (int(col*(self.WIDTH/3)+(self.WIDTH/3)-SPACE), int(row*(self.HEIGHT/3)+(self.HEIGHT/3)-SPACE)), CROSS_WIDTH)
                    

    def check_win(self, player):
        # Vertical win
        for col in range(self.BOARD_COLS):
            if self.board[0][col] == player and self.board[1][col] == player and self.board[2][col] == player:
                self.draw_vertical_win(col)
                return True
        
        # Horizontal win
        for row in range(self.BOARD_ROWS):
            if self.board[row][0] == player and self.board[row][1] == player and self.board[row][2] == player:
                self.draw_horizontal_win(row)
                return True
        
        # Diagonal Ascending Win
        if self.board[2][0] == player and self.board[1][1] == player and self.board[0][2] == player:
            self.draw_diagonal_desc_win()
            return True

        # Diagonal Descending Win
        if self.board[0][0] == player and self.board[1][1] == player and self.board[2][2] == player:
            self.draw_diagonal_asc_win()
            return True

        return False


    def draw_horizontal_win(self, col):
        posX = col * (self.HEIGHT/3) + (self.HEIGHT/6)
        pygame.draw.line(self.screen, WINLINE_COLOR, (15,posX), (self.HEIGHT - 15, posX), WINLINE_WIDTH)


    def draw_vertical_win(self, row):
        posY = row * (self.WIDTH/3) + (self.WIDTH/6)
        pygame.draw.line(self.screen, WINLINE_COLOR, (posY, 15), (posY, self.WIDTH - 15), WINLINE_WIDTH)


    def draw_diagonal_desc_win(self):
        pygame.draw.line(self.screen, WINLINE_COLOR, (15, self.HEIGHT - 15), (self.WIDTH - 15, 15), WINLINE_WIDTH)
        

    def draw_diagonal_asc_win(self):
        pygame.draw.line(self.screen, WINLINE_COLOR, (15, 15), (self.WIDTH - 15, self.HEIGHT - 15), WINLINE_WIDTH)
        
    def restart_game(self):
        self.screen.fill(BG_COLOR)
        for row in range(self.BOARD_ROWS):
            for col in range(self.BOARD_COLS):
                self.board[row][col] = 0

