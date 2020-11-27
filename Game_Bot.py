from random import randrange
class Game_Bot:
    WHITE = "w"
    BLACK = "b"
    EMPTY = "."
    size = 19


    def __init__(self):
        '''
        Setting up the initial attributes of the Game_Bot class
        self.gameBoard is the game board that the pieces will get placed on

        '''


        self.playerColour = self.BLACK
        self.computerColour = self.WHITE
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

    def result(self, move):

        '''
        The method that handles the move that the player made and the move that the bot will make
        main sends in the move that the player made and the board is updated 
        Once that happens then the we check if the player has won, if the player has won we return "Player"
        otherwise we keep going on. Then we check if the game is tied, we check this by seeing if the board is all filled
        but their are no winners. If their is a draw we return "Draw"
        '''

        x = move[0] - 1
        y = move[1] - 1
        self.gameBoard[x][y] = "b"

        for i in range(15):
            for j in range(15):
                # Horizontal win check
                if self.gameBoard[i][j] == 'b':
                    if self.gameBoard[i][j + 1] == 'b':
                        if self.gameBoard[i][j + 2] == 'b':
                            if self.gameBoard[i][j + 3] == 'b':
                                if self.gameBoard[i][j + 4] == 'b':
                                    return "Player"

                # Vertical win check
                if self.gameBoard[i][j] == 'b':
                    if self.gameBoard[i + 1][j] == 'b':
                        if self.gameBoard[i + 2][j] == 'b':
                            if self.gameBoard[i + 3][j] == 'b':
                                if self.gameBoard[i + 4][j] == 'b':
                                    return "Player"

                # Diagonal win check
                # down and right???
                if self.gameBoard[i][j] == 'b':
                    if self.gameBoard[i + 1][j + 1] == 'b':
                        if self.gameBoard[i + 2][j + 2] == 'b':
                            if self.gameBoard[i + 3][j + 3] == 'b':
                                if self.gameBoard[i + 4][j + 4] == 'b':
                                    return "Player"

                # up and right
                if i >= 4:
                    if self.gameBoard[i][j] == 'b':
                        if self.gameBoard[i - 1][j + 1] == 'b':
                            if self.gameBoard[i - 2][j + 2] == 'b':
                                if self.gameBoard[i - 3][j + 3] == 'b':
                                    if self.gameBoard[i - 4][j + 4] == 'b':
                                        return "Player"

                # down and left check for edge cases where up and right doesnt check
                if i >= 4 and j >= 4:
                    if self.gameBoard[i][j] == 'w':
                        if self.gameBoard[i + 1][j - 1] == 'w':
                            if self.gameBoard[i + 2][j - 2] == 'w':
                                if self.gameBoard[i + 3][j - 3] == 'w':
                                    if self.gameBoard[i + 4][j - 4] == 'w':
                                        return "Player"

        filled = 0
        for i in range(len(self.gameBoard)):
            for j in range(len(self.gameBoard[i])):
                if self.gameBoard[i][j] != '.':
                    filled += 1

        if filled == 361:
            return "Draw"
        


        '''
        the bestMove list will store the points that the bot can get, and the blockPlayerBoard will store the points that the player can get. 
        '''



        bestMove = [
            ['.', '.', '.', '.', '.', '.', '.', '.', '.' , '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
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
        ]

        blockPlayerBoard = [
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



        '''
        This algorithm below goes through each possible possition of the board and talies up how many points the player can get at each position.
        It gets the maximum number of points at that location by finding the max of the 12 possible paths. The 12 paths are
        right, left, up, down, the 4 diagonal paths, and the 4 middle paths. Once it getst the max number of points it at that location it stores
        it in the self.blockPlayerBoard. If it gets 4 points it means that the player has 4 pieces that are connected on the board and then 
        we place a the bot's piece their to try to stop the player from winning. 
        '''



        for i in range(len(self.gameBoard)):
            for j in range(len(self.gameBoard[i])):
                points = [0, 0, 0, 0, 0, 0, 0, 0,0,0,0,0]

                stop = False
                horRightMove = j + 1
                while horRightMove < 19 and stop != True and points[0] < 5 and self.gameBoard[i][horRightMove] == "b":
                    points[0] += 1
                    if self.gameBoard[i][horRightMove] == "w":
                        stop = True
                    horRightMove += 1

                stop = False
                horLeftMove = j - 1
                while horLeftMove >= 0 and stop != True and points[1] < 5 and self.gameBoard[i][horLeftMove] == "b":
                    points[1] += 1
                    if self.gameBoard[i][horLeftMove] == "w":
                        stop = True
                    horLeftMove -= 1

                stop = False
                verTopMove = i - 1
                while verTopMove >= 0 and stop != True and points[2] < 5 and self.gameBoard[verTopMove][j] == "b":
                    points[2] += 1
                    if self.gameBoard[verTopMove][j] == "w":
                        stop = True
                    verTopMove -= 1

                stop = False
                verBottomMove = i + 1
                while verBottomMove < 19 and stop != True and points[3] < 5 and self.gameBoard[verBottomMove][j] == "b":
                    points[3] += 1
                    if self.gameBoard[verBottomMove][j] == "w":
                        stop = True
                    verBottomMove += 1


                stop = False
                diaTopRightX = i - 1
                diaTopRightY = j + 1
                while diaTopRightX >= 0 and diaTopRightY < 19 and stop != True and points[4] < 5 and \
                        self.gameBoard[diaTopRightX][diaTopRightY] == "b":
                    points[4] += 1
                    if self.gameBoard[diaTopRightX][diaTopRightY] == "w":
                        stop = True
                    diaTopRightX -= 1
                    diaTopRightY += 1

                stop = False
                diaTopLeftX = i - 1
                diaTopLeftY = j - 1
                while diaTopLeftX >= 0 and diaTopLeftY >= 0 and stop != True and points[5] < 5 and \
                        self.gameBoard[diaTopLeftX][diaTopLeftY] == "b":
                    points[5] += 1
                    if self.gameBoard[diaTopLeftX][diaTopLeftY] == "w":
                        stop = True
                    diaTopLeftX -= 1
                    diaTopLeftY -= 1

                stop = False
                diaBottomRightX = i + 1
                diaBottomRightY = j + 1
                while diaBottomRightX < 19 and diaBottomRightY < 19 and stop != True and points[6] < 5 and \
                        self.gameBoard[diaBottomRightX][diaBottomRightY] == "b":
                    points[6] += 1
                    if self.gameBoard[diaBottomRightX][diaBottomRightY] == "w":
                        stop = True
                    diaBottomRightX += 1
                    diaBottomRightY += 1

                stop = False
                diaBottomLeftX = i + 1
                diaBottomLeftY = j - 1
                while diaBottomLeftX < 19 and diaBottomLeftY >= 0 and stop != True and points[7] < 5 and \
                        self.gameBoard[diaBottomLeftX][diaBottomLeftY] == "b":
                    points[7] += 1
                    if self.gameBoard[diaBottomLeftX][diaBottomLeftY] == "w":
                        stop = True
                    diaBottomLeftX += 1
                    diaBottomLeftY -= 1

                stop = False
                horRightMove = j + 1
                while horRightMove < 19 and stop != True and points[8] < 5 and self.gameBoard[i][horRightMove] == "b":
                    points[8] += 1
                    if self.gameBoard[i][horRightMove] == "w":
                        stop = True
                    horRightMove += 1
                stop = False

                horLeftMove = j - 1
                while horLeftMove >= 0 and stop != True and points[8] < 5 and self.gameBoard[i][horLeftMove] == "b":
                    points[8] += 1
                    if self.gameBoard[i][horLeftMove] == "w":
                        stop = True
                    horLeftMove -= 1

                stop = False
                verTopMove = i - 1
                while verTopMove >= 0 and stop != True and points[9] < 5 and self.gameBoard[verTopMove][j] == "b":
                    points[9] += 1
                    if self.gameBoard[verTopMove][j] == "w":
                        stop = True
                    verTopMove -= 1

                stop = False
                verBottomMove = i + 1
                while verBottomMove < 19 and stop != True and points[9] < 5 and self.gameBoard[verBottomMove][j] == "b":
                    points[9] += 1
                    if self.gameBoard[verBottomMove][j] == "w":
                        stop = True
                    verBottomMove += 1

                stop = False
                diaBottomLeftX = i + 1
                diaBottomLeftY = j - 1
                while diaBottomLeftX < 19 and diaBottomLeftY >= 0 and stop != True and points[10] < 5 and \
                        self.gameBoard[diaBottomLeftX][diaBottomLeftY] == "b":
                    points[10] += 1
                    if self.gameBoard[diaBottomLeftX][diaBottomLeftY] == "w":
                        stop = True
                    diaBottomLeftX += 1
                    diaBottomLeftY -= 1

                stop = False
                diaTopRightX = i - 1
                diaTopRightY = j + 1
                while diaTopRightX >= 0 and diaTopRightY < 19 and stop != True and points[10] < 5 and \
                        self.gameBoard[diaTopRightX][diaTopRightY] == "b":
                    points[10] += 1
                    if self.gameBoard[diaTopRightX][diaTopRightY] == "w":
                        stop = True
                    diaTopRightX -= 1
                    diaTopRightY += 1

                stop = False
                diaBottomRightX = i + 1
                diaBottomRightY = j + 1
                while diaBottomRightX < 19 and diaBottomRightY < 19 and stop != True and points[11] < 5 and \
                        self.gameBoard[diaBottomRightX][diaBottomRightY] == "b":
                    points[11] += 1
                    if self.gameBoard[diaBottomRightX][diaBottomRightY] == "w":
                        stop = True
                    diaBottomRightX += 1
                    diaBottomRightY += 1

                stop = False
                diaTopLeftX = i - 1
                diaTopLeftY = j - 1
                while diaTopLeftX >= 0 and diaTopLeftY >= 0 and stop != True and points[11] < 5 and \
                        self.gameBoard[diaTopLeftX][diaTopLeftY] == "b":
                    points[11] += 1
                    if self.gameBoard[diaTopLeftX][diaTopLeftY] == "w":
                        stop = True
                    diaTopLeftX -= 1
                    diaTopLeftY -= 1

                blockPlayerBoard[i][j] = str(max(points))

        
        

        bestScore = 0
        bestPos = []
        for x in range(len(blockPlayerBoard)):
            for y in range(len(blockPlayerBoard[x])):
                if int(blockPlayerBoard[x][y]) >= bestScore and self.gameBoard[x][y] != "b" and self.gameBoard[x][
                    y] != "w":
                    bestScore = int(blockPlayerBoard[x][y])
                    bestPos = [x, y]

        if bestScore == 4:
            self.gameBoard[bestPos[0]][bestPos[1]] = "w"
            return "None"
        



        '''
        Find the best possible move and if the player has 4 connected pieces block the move.
        This algorithm below goes through each possible possition of the board and talies up how many points the bot can get at each position.
        It gets the maximum number of points at that location by finding the max of the 12 possible paths. The 12 paths are
        right, left, up, down, the 4 diagonal paths, and the 4 middle paths. Once it getst the max number of points it at that location it stores
        it in the self.bestMove. It then goes through bestMove and find the the index with the most amount of points and then it places the bot 
        piece there. 
        '''

        for i in range(len(self.gameBoard)):
            for j in range(len(self.gameBoard[i])):
                points = [0, 0, 0, 0, 0, 0, 0, 0,0,0,0,0]

                stop = False
                horRightMove = j + 1
                while horRightMove < 19 and stop != True and points[0] < 5 and self.gameBoard[i][horRightMove] == "w":
                    points[0] += 1
                    if self.gameBoard[i][horRightMove] == "b":
                        stop = True
                    horRightMove += 1

                stop = False
                horLeftMove = j - 1
                while horLeftMove >= 0 and stop != True and points[1] < 5 and self.gameBoard[i][horLeftMove] == "w":
                    points[1] += 1
                    if self.gameBoard[i][horLeftMove] == "b":
                        stop = True
                    horLeftMove -= 1

                stop = False
                verTopMove = i - 1
                while verTopMove >= 0 and stop != True and points[2] < 5 and self.gameBoard[verTopMove][j] == "w":
                    points[2] += 1
                    if self.gameBoard[verTopMove][j] == "b":
                        stop = True
                    verTopMove -= 1

                stop = False
                verBottomMove = i + 1
                while verBottomMove < 19 and stop != True and points[3] < 5 and self.gameBoard[verBottomMove][j] == "w":
                    points[3] += 1
                    if self.gameBoard[verBottomMove][j] == "b":
                        stop = True
                    verBottomMove += 1

                stop = False
                diaTopRightX = i - 1
                diaTopRightY = j + 1
                while diaTopRightX >= 0 and diaTopRightY < 19 and stop != True and points[4] < 5 and self.gameBoard[diaTopRightX][diaTopRightY] == "w":
                    points[4] += 1
                    if self.gameBoard[diaTopRightX][diaTopRightY] == "b":
                        stop = True
                    diaTopRightX -= 1
                    diaTopRightY += 1

                stop = False
                diaTopLeftX = i - 1
                diaTopLeftY = j - 1
                while diaTopLeftX >= 0 and diaTopLeftY >= 0 and stop != True and points[5] < 5 and self.gameBoard[diaTopLeftX][diaTopLeftY] == "w" :
                    points[5] += 1
                    if self.gameBoard[diaTopLeftX][diaTopLeftY] == "b":
                        stop = True
                    diaTopLeftX -= 1
                    diaTopLeftY -= 1


                stop = False
                diaBottomRightX = i + 1
                diaBottomRightY = j + 1
                while diaBottomRightX < 19 and diaBottomRightY < 19 and stop != True and points[6] < 5 and self.gameBoard[diaBottomRightX][diaBottomRightY] == "w":
                    points[6] += 1
                    if self.gameBoard[diaBottomRightX][diaBottomRightY] == "b":
                        stop = True
                    diaBottomRightX += 1
                    diaBottomRightY += 1

                stop = False
                diaBottomLeftX = i + 1
                diaBottomLeftY = j - 1
                while diaBottomLeftX < 19 and diaBottomLeftY >= 0 and stop != True and points[7] < 5 and self.gameBoard[diaBottomLeftX][diaBottomLeftY] == "w" :
                    points[7] += 1
                    if self.gameBoard[diaBottomLeftX][diaBottomLeftY] == "b":
                        stop = True
                    diaBottomLeftX += 1
                    diaBottomLeftY -= 1
                
                stop = False
                horRightMove = j + 1
                while horRightMove < 19 and stop != True and points[8] < 5 and self.gameBoard[i][horRightMove] == "w":
                    points[8] += 1
                    if self.gameBoard[i][horRightMove] == "b":
                        stop = True
                    horRightMove += 1

                stop = False
                horLeftMove = j - 1
                while horLeftMove >= 0 and stop != True and points[8] < 5 and self.gameBoard[i][horLeftMove] == "w":
                    points[8] += 1
                    if self.gameBoard[i][horLeftMove] == "b":
                        stop = True
                    horLeftMove -= 1
                

                verTopMove = i - 1
                stop = False
                while verTopMove >= 0 and stop != True and points[9] < 5 and self.gameBoard[verTopMove][j] == "w":
                    points[9] += 1
                    if self.gameBoard[verTopMove][j] == "b":
                        stop = True
                    verTopMove -= 1

                stop = False
                verBottomMove = i + 1
                while verBottomMove < 19 and stop != True and points[9] < 5 and self.gameBoard[verBottomMove][j] == "w":
                    points[9] += 1
                    if self.gameBoard[verBottomMove][j] == "b":
                        stop = True
                    verBottomMove += 1


                stop = False
                diaBottomLeftX = i + 1
                diaBottomLeftY = j - 1
                while diaBottomLeftX < 19 and diaBottomLeftY >= 0 and stop != True and points[10] < 5 and \
                        self.gameBoard[diaBottomLeftX][diaBottomLeftY] == "w":
                    points[10] += 1
                    if self.gameBoard[diaBottomLeftX][diaBottomLeftY] == "b":
                        stop = True
                    diaBottomLeftX += 1
                    diaBottomLeftY -= 1

                stop = False
                diaTopRightX = i - 1
                diaTopRightY = j + 1
                while diaTopRightX >= 0 and diaTopRightY < 19 and stop != True and points[10] < 5 and \
                        self.gameBoard[diaTopRightX][diaTopRightY] == "w":
                    points[10] += 1
                    if self.gameBoard[diaTopRightX][diaTopRightY] == "b":
                        stop = True
                    diaTopRightX -= 1
                    diaTopRightY += 1

                stop = False
                diaBottomRightX = i + 1
                diaBottomRightY = j + 1
                while diaBottomRightX < 19 and diaBottomRightY < 19 and stop != True and points[11] < 5 and \
                        self.gameBoard[diaBottomRightX][diaBottomRightY] == "w":
                    points[11] += 1
                    if self.gameBoard[diaBottomRightX][diaBottomRightY] == "b":
                        stop = True
                    diaBottomRightX += 1
                    diaBottomRightY += 1

                stop = False
                diaTopLeftX = i - 1
                diaTopLeftY = j - 1
                while diaTopLeftX >= 0 and diaTopLeftY >= 0 and stop != True and points[11] < 5 and \
                        self.gameBoard[diaTopLeftX][diaTopLeftY] == "w":
                    points[11] += 1
                    if self.gameBoard[diaTopLeftX][diaTopLeftY] == "b":
                        stop = True
                    diaTopLeftX -= 1
                    diaTopLeftY -= 1

                bestMove[i][j] = str(max(points))


        bestScore = 0
        bestPos = []
        for x in range(len(bestMove)):
            for y in range(len(bestMove[x])):
                if int(bestMove[x][y]) >= bestScore and self.gameBoard[x][y]!= "b" and self.gameBoard[x][y]!= "w":
                    bestScore = int(bestMove[x][y])
                    bestPos = [x,y]



        '''
        This part randomizes the bots first move.
        Checks if currently the bot has not made a move, if so randomizes the first move that it makes

        '''


        filled = 0
        for i in range(len(self.gameBoard)):
            for j in range(len(self.gameBoard[i])):
                if self.gameBoard[i][j] == '.':
                    filled += 1

        if filled == 360:
            x = randrange(19)
            y = randrange(19)
            while (x == (move[0] - 1) or y == (move[1] - 1)):
                x = randrange(19)
                y = randrange(19)
            self.gameBoard[x][y] = "w"
        else:
            self.gameBoard[bestPos[0]][bestPos[1]] = "w"
        
        

        '''
        If the bot has 4 pieces that are already connected, connect the 5th piece and return "Bot"
        otherwise return "None" to indicated that no one has won yet

        '''

        if bestScore == 4:
            returnList = []
            returnList.append("Bot")
            returnList.append(self.gameBoard)
            return ("Bot")
        else:
            return ("None")



        '''
        Checks for a draw by checking the whole board and seeing if their is any empty position left, if no empty positions
        are left it returns "Draw"

        '''

        filled = 0
        for i in range(len(self.gameBoard)):
            for j in range(len(self.gameBoard[i])):
                if self.gameBoard[i][j] != '.':
                    filled += 1

        if filled == 361:
            return "Draw"


