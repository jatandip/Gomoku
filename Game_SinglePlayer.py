class Game_SinglePlayer:

    def __init__(self):
        self.gameBoard = [
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']]


    #Method that just returns the current board state
    def Board(self):
        return self.gameBoard



    '''
    The play method places the a white or black piece on the board depending on whos move it is 
    It then checks if the bot or player has won, if white wins it return "White" and if black wins
    it returns "Black", if their is no winners it returns "None"


    '''
    def play(self, color, move):
        x = move[0] - 1
        y = move[1] - 1
        if color == "b":
            self.gameBoard[x][y] = "b"
        if color == "w":
            self.gameBoard[x][y] = "w"

        if color == "w":
            for i in range(15):
                for j in range(15):
                    # Horizontal win check
                    if self.gameBoard[i][j] == 'w':
                        if self.gameBoard[i][j + 1] == 'w':
                            if self.gameBoard[i][j + 2] == 'w':
                                if self.gameBoard[i][j + 3] == 'w':
                                    if self.gameBoard[i][j + 4] == 'w':
                                        return "White"
                    # Vertical win check
                    if self.gameBoard[i][j] == 'w':
                        if self.gameBoard[i + 1][j] == 'w':
                            if self.gameBoard[i + 2][j] == 'w':
                                if self.gameBoard[i + 3][j] == 'w':
                                    if self.gameBoard[i + 4][j] == 'w':
                                        return "White"

                    # Diagonal win check
                    # down and right???
                    if self.gameBoard[i][j] == 'w':
                        if self.gameBoard[i + 1][j + 1] == 'w':
                            if self.gameBoard[i + 2][j + 2] == 'w':
                                if self.gameBoard[i + 3][j + 3] == 'w':
                                    if self.gameBoard[i + 4][j + 4] == 'w':
                                        return "White"
                    # up and right
                    if i >= 4:
                        if self.gameBoard[i][j] == 'w':
                            if self.gameBoard[i - 1][j + 1] == 'w':
                                if self.gameBoard[i - 2][j + 2] == 'w':
                                    if self.gameBoard[i - 3][j + 3] == 'w':
                                        if self.gameBoard[i - 4][j + 4] == 'w':
                                            return "White"
                    if i >= 4 and j >= 4:
                        if self.gameBoard[i][j] == 'w':
                            if self.gameBoard[i + 1][j - 1] == 'w':
                                if self.gameBoard[i + 2][j - 2] == 'w':
                                    if self.gameBoard[i + 3][j - 3] == 'w':
                                        if self.gameBoard[i + 4][j - 4] == 'w':
                                            return "White"

        elif color == "b":
            for i in range(15):
                for j in range(15):
                    # Horizontal win check
                    if self.gameBoard[i][j] == 'b':
                        if self.gameBoard[i][j + 1] == 'b':
                            if self.gameBoard[i][j + 2] == 'b':
                                if self.gameBoard[i][j + 3] == 'b':
                                    if self.gameBoard[i][j + 4] == 'b':
                                        return "Black"
                    # Vertical win check
                    if self.gameBoard[i][j] == 'b':
                        if self.gameBoard[i + 1][j] == 'b':
                            if self.gameBoard[i + 2][j] == 'b':
                                if self.gameBoard[i + 3][j] == 'b':
                                    if self.gameBoard[i + 4][j] == 'b':
                                        return "Black"

                    # Diagonal win check
                    # down and right???
                    if self.gameBoard[i][j] == 'b':
                        if self.gameBoard[i + 1][j + 1] == 'b':
                            if self.gameBoard[i + 2][j + 2] == 'b':
                                if self.gameBoard[i + 3][j + 3] == 'b':
                                    if self.gameBoard[i + 4][j + 4] == 'b':
                                        return "Black"
                    # up and right
                    if i >= 4:
                        if self.gameBoard[i][j] == 'b':
                            if self.gameBoard[i - 1][j + 1] == 'b':
                                if self.gameBoard[i - 2][j + 2] == 'b':
                                    if self.gameBoard[i - 3][j + 3] == 'b':
                                        if self.gameBoard[i - 4][j + 4] == 'b':
                                            return "Black"
                    if i >= 4 and j >= 4:
                        if self.gameBoard[i][j] == 'b':
                            if self.gameBoard[i + 1][j - 1] == 'b':
                                if self.gameBoard[i + 2][j - 2] == 'b':
                                    if self.gameBoard[i + 3][j - 3] == 'b':
                                        if self.gameBoard[i + 4][j - 4] == 'b':
                                            return "Black"

        return "None" 