import pygame, sys
import Assets.Scripts.ticTacToeLogic as TicTacToe
import Assets.Scripts.game as Game

# Initialize PyGame
pygame.init()

# Constants
WIDTH = 720
HEIGHT = 720
BOARD_ROWS = 3
BOARD_COLS = 3


# Initialize Board
board = TicTacToe.TicTacToePVP(BOARD_ROWS, BOARD_COLS)


# Initialize Game
startGame = Game.StartGame(board.board, BOARD_COLS,BOARD_ROWS,WIDTH,HEIGHT)


# game Variables
player = 1
game_over = False


def initializeGame(player,game_over, board, startGame):
    startGame.draw_lines()
    # Main Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                mouseX = event.pos[0]
                mouseY = event.pos[1]
                
                clicked_row = int(mouseY // (HEIGHT/3))
                clicked_col = int(mouseX // (WIDTH/3))
                
                if board.square_available(clicked_row, clicked_col):
                    if player == 1:
                        board.mark_square(clicked_row, clicked_col, 1)
                        if startGame.check_win(player):
                            game_over = True
                        player = 2

                    elif player == 2:
                        board.mark_square(clicked_row, clicked_col, 2)
                        if startGame.check_win(player):
                            game_over = True
                        player = 1

                    startGame.draw_figures()


        pygame.display.update()





def main():
    initializeGame(player,game_over, board, startGame)


if __name__ == "__main__":
    main()