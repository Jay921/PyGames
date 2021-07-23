from math import inf
import numpy as np

class TicTacToe:
    def __init__(self, human, ai):
        self.human = human
        self.ai = ai

        start_board = np.array([['-', '-', '-'],['-', '-', '-'],['-', '-', '-']])

        scores = {
            'X':1,
            'O':-1,
            'tie':0
        }

        self.board = start_board
        self.scores = scores

        print(start_board)

    def startGame(self):
        winner = self.checkWinner()
        
        if self.human == 'O':
            move = self.bestMove(self.board)
            # Check if a player won
            if (winner != None):
                return self.won(winner)

            # Else make new move
            elif (move != None and winner == None):
                self.aIsTurn(move)

            # Check if there is a winner
            winner = self.checkWinner()
            if (winner != None):
                return self.won(winner)

            # Human's Turn
            self.humansTurn(winner)
        else:
            # Check if a player won
            winner = self.checkWinner()
            # move = self.bestMove(self.board)
            if (winner != None):
                return self.won(winner)

            # Human's Turn
            self.humansTurn(winner)

            # Check if there is a winner
            winner = self.checkWinner()
            move = self.bestMove(self.board)
            if (winner != None):
                return self.won(winner)

            # Else make new move
            elif (move != None and winner == None):
                self.aIsTurn(move)
            

    def aIsTurn(self, move):
        print("New Move:")
        print(f"Enemy Pos: {move}")
        self.board[move[0], move[1]] = self.ai
        print(self.board)

    def humansTurn(self, winner):
        pos = input("\nEnter Position (r = row, c = column) => Input Format: 'rc'\n    Input: ")

        # Make new move (Human)
        pos1 = int(pos[0])
        pos2 = int(pos[1])
        
        input_pos = (pos1, pos2)
        if (self.board[input_pos[0]][input_pos[1]] == '-'):
            self.board[input_pos[0]][input_pos[1]] = self.human
        else:
            print('Unavailable Cell')
        print(f"Input Pos: {input_pos}")
        print(self.board)

    def won(self, winner):
        """
            This function checks if the game is over 
            i.e. if a player won or if the game is tied
        """
        print(f"Game Over!")
        if (winner == 'X'):
            return (f"{winner} Won!")
        elif (winner == 'O'):
            return (f"{winner} Won!")
        else:
            return ("Its a Tie!")
            


    def bestMove(self, board):
        """
            This function returns the best move for the AI
        """

        if self.ai == 'X':
            best_score = -inf
            best_move = None
            for i in range(0,3):
                for j in range(0,3):
                    if (board[i][j] == '-'):
                        board[i][j] = self.ai
                        score = self.minimax(0, False)
                        board[i][j] = '-'
                        if (float(score) > float(best_score)):
                            best_score = score 
                            best_move = (i,j)
                    
            return best_move

        else:
            best_score = inf
            best_move = None
            for i in range(0,3):
                for j in range(0,3):
                    if (board[i][j] == '-'):
                        board[i][j] = self.ai
                        score = self.minimax(0, True)
                        board[i][j] = '-'
                        if (float(score) < float(best_score)):
                            best_score = score 
                            best_move = (i,j)
                    
            return best_move


    def checkWinner(self):
        """
            This function checks if there is a winner or if the game is tied
            Returns: 
                - None
                - 'X' or 'O'
                - 'tie'
        """
        winner = None

        # Horizontal
        for i in range(0,3):
            if (self.board[i][0] == self.board[i][1] and self.board[i][1] == self.board[i][2] and self.board[i][0] == self.board[i][2] and self.board[i][0] != '-'):
                winner = self.board[i][0]

        # Vertical
        for i in range(0,3):
            if (self.board[0][i] == self.board[1][i] and self.board[1][i] == self.board[2][i] and self.board[0][i] == self.board[2][i] and self.board[0][i] != '-'):
                winner = self.board[0][i]

        # Diagonal
        if (self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2] and self.board[0][0] == self.board[2][2] and self.board[0][0] != '-'):
            winner = self.board[0][0]
        if (self.board[2][0] == self.board[1][1] and self.board[1][1] == self.board[0][2] and self.board[2][0] == self.board[0][2] and self.board[2][0] != '-'):
            winner = self.board[2][0]

        open_spots = 0
        for i in range(0,3):
            for j in range(0,3):
                if (self.board[i][j] == '-'):
                    open_spots += 1

        if winner == None and open_spots == 0:
            return 'tie'
        else:
            return winner


    def minimax(self, depth, isMaximising):
        """
            This function calculates the minimax score (best score)
            for the AI to make the next best move using recursion.
        """
        result = self.checkWinner()

        if (result != None):
            score = self.scores[result]
            return score

        # Maximising player
        if (isMaximising):
            best_score = -inf
            for i in range(0,3):
                for j in range(0,3):
                    if (self.board[i][j] == '-'):
                        self.board[i][j] = self.ai
                        score = self.minimax(depth +1,  False) 
                        self.board[i][j] = '-'
                        best_score = max(score, best_score)
            return best_score 
        
        # Minimising Player
        else:
            best_score = inf
            for i in range(0,3):
                for j in range(0,3):
                    if (self.board[i][j] == '-'):
                        self.board[i][j] = self.human
                        score = self.minimax(depth +1,  True) 
                        self.board[i][j] = '-'
                        best_score = min(score, best_score) 
            return best_score  


def main():
    """
        This is the main function.
        This function starts the game by calling the class 'TicTacToe':
            - First sleect whether to play as 'X' or 'O'.
            - Then repeat the TicTacToe.startGame() function until the game is over.
    """
    

    

    user_input = input("Select Side (X or O): ")

    if (user_input.lower() in 'xo'):
        print(user_input)
        human = 'X'
        ai = 'O'

        if user_input.lower() == 'o':
            human = 'O'
            ai = 'X'

        initGame = TicTacToe(human, ai)
        while True:
            game = initGame.startGame()
            if (game != None):
                print(game)
                break
            else:
                game

    else:
        print("Invalid Input!")


if __name__ == "__main__":
    main()