# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
class Game_Bot:
    WHITE = "w"
    BLACK = "b"
    EMPTY = "."
    size = 19

    def __init__(self):
        self.playerColour = self.BLACK
        self.computerColour = self.WHITE
        self.computerScore = 0
        self.playerScore = 0
        self.captured = []
        self.bestscore = 0
        self.newGame()

    def newGame(self):
        print("entered newgame")
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
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ]

        print("before result")
        self.result([5,5])
        print("after result")


    def result(self, move):
        x = move[0]
        y = move[1]
        self.gameBoard[x][y] = "b"

        bestMove = [
            ['.', '.', '.', '.', '.', '.', '.', '.', '.' , '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', 'w', 'w', 'w', 'w', '.', '.', '.', '.', '.', '.', '.'],
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

        for i in range(len(self.gameBoard)):
            for j in range(len(self.gameBoard[i])):

                print(i,j)
                points = [0, 0, 0, 0, 0, 0, 0, 0]

                print(i,j, "first")

                stop = False
                horRightMove = j + 1
                while horRightMove < 19 and stop != True and points[0] < 5:
                    if self.gameBoard[i][horRightMove] == "w":
                        points[0] += 1
                    if self.gameBoard[i][horRightMove] == "b":
                        stop = True
                    horRightMove += 1


                print(i,j, "second")

                stop = False
                horLeftMove = j - 1
                while horLeftMove >= 0 and stop != True and points[1] < 5:
                    if self.gameBoard[i][horLeftMove] == "w":
                        points[1] += 1
                    if self.gameBoard[i][horLeftMove] == "b":
                        stop = True
                    horLeftMove -= 1



                print(i,j, "third")

                stop = False
                verTopMove = i - 1
                while verTopMove >= 0 and stop != True and points[2] < 5:
                    if self.gameBoard[verTopMove][j] == "w":
                        points[2] += 1
                    if self.gameBoard[verTopMove][j] == "b":
                        stop = True
                    verTopMove -= 1


                print(i,j, "fourth")

                stop = False
                verBottomMove = i + 1
                while verBottomMove < 19 and stop != True and points[3] < 5:
                    if self.gameBoard[verBottomMove][j] == "w":
                        points[3] += 1
                    if self.gameBoard[verBottomMove][j] == "b":
                        stop = True
                    verBottomMove += 1


                print(i,j, "fifth")

                stop = False
                diaTopRightX = i - 1
                diaTopRightY = j + 1
                while diaTopRightX >= 0 and diaTopRightY < 19 and stop != True and points[4] < 5:
                    if self.gameBoard[diaTopRightX][diaTopRightY] == "w":
                        points[4] += 1
                    if self.gameBoard[diaTopRightX][diaTopRightY] == "b":
                        stop = True
                    diaTopRightX -= 1
                    diaTopRightY += 1


                print(i,j, "sixth")

                stop = False
                diaTopLeftX = i - 1
                diaTopLeftY = j - 1
                while diaTopLeftX >= 0 and diaTopLeftY >= 0 and stop != True and points[5] < 5:
                    if self.gameBoard[diaTopLeftX][diaTopLeftY] == "w":
                        points[5] += 1
                    if self.gameBoard[diaTopLeftX][diaTopLeftY] == "b":
                        stop = True
                    diaTopLeftX -= 1
                    diaTopLeftY -= 1


                print(i,j, "seventh")
                stop = False
                diaBottomRightX = i + 1
                diaBottomRightY = j + 1
                while diaBottomRightX < 19 and diaBottomRightY < 19 and stop != True and points[6] < 5:
                    if self.gameBoard[diaBottomRightX][diaBottomRightY] == "w":
                        points[6] += 1
                    if self.gameBoard[diaBottomRightX][diaBottomRightY] == "b":
                        stop = True
                    diaBottomRightX += 1
                    diaBottomRightY += 1

                print(i,j, "eight")

                stop = False
                diaBottomLeftX = i + 1
                diaBottomLeftY = j - 1
                while diaBottomLeftX < 19 and diaBottomLeftY >= 0 and stop != True and points[7] < 5:
                    if self.gameBoard[diaBottomLeftX][diaBottomLeftY] == "w":
                        points[7] += 1
                    if self.gameBoard[diaBottomLeftX][diaBottomLeftY] == "b":
                        stop = True
                    diaBottomLeftX += 1
                    diaBottomLeftY -= 1

                bestMove[i][j] = str(max(points))



        bestScore = 0
        bestPos = []
        for x in range(len(bestMove)):
            for y in range(len(bestMove[x])):
                if int(bestMove[x][y]) >= bestScore:
                    bestScore = int(bestMove[x][y])
                    bestPos = [x,y]



        self.gameBoard[bestPos[0]][bestPos[1]] = "w"

        if bestScore == 4:
            print("Bot")
            #print ["Bot", self.gameBoard]
        #else:
            #print ["None", self.gameBoard]

