import pygame
from Game_SinglePlayer import Game_SinglePlayer
from Game_Bot import Game_Bot
from Game_Tutorial import Game_Tutorial
import sys

#DONT CHANGE##########################
WHITE = (255, 255, 255)
PISTACHIO = (159, 205, 141)
INCHWORM = (178, 255, 127)
ORANGE_YELLOW = (235, 185, 51)
CAMEL = (198, 156, 109)
COYOTE_BROWN = (140, 98, 57)

pygame.init()
######################################

def main():
    selectionMade = False
    displayMenu()

    while not selectionMade:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                posx = event.pos[0]
                posy = event.pos[1]
                if (28+342) >= posx > 28 and (140+100) >= posy > 140:   #vs bot
                    pygame.display.quit()
                    selectionMade = True
                    playBotGame()
                elif (28+342) >= posx > 28 and (253+100) >= posy > 253: #vs player
                    pygame.display.quit()
                    selectionMade = True
                    playUserGame()
                elif (28+342) >= posx > 28 and (366+100) >= posy > 366: #tutorial
                    pygame.display.quit()
                    selectionMade = True
                    playTutorial()

def displayMenu():
    width = 400
    height = 500
    size = (width, height)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("GOMOKU")

    pygame.draw.rect(screen, PISTACHIO, (0, 0, width, height))

    pygame.draw.rect(screen, COYOTE_BROWN, (28, 140, 342, 100))
    opOneRect = pygame.draw.rect(screen, CAMEL, (28+3, 140+3, 342-6, 100-6))
    opOneRect.center = (240, 135+(148//2))

    pygame.draw.rect(screen, COYOTE_BROWN, (28, 253, 342, 100))
    opTwoRect = pygame.draw.rect(screen, CAMEL, (28+3, 253+3, 342-6, 100-6))
    opTwoRect.center = (260, 248+(148//2))

    pygame.draw.rect(screen, COYOTE_BROWN, (28, 366, 342, 100))
    opThreeRect = pygame.draw.rect(screen, CAMEL, (28+3, 366+3, 342-6, 100-6))
    opThreeRect.center = (270, 361+(148//2))

    font = pygame.font.Font('FFF_Tusj.ttf', 90)
    title = font.render("Gomoku", True, INCHWORM)
    font = pygame.font.Font('FFF_Tusj.ttf', 48)
    opOne = font.render("vs. CMPUT", True, ORANGE_YELLOW)
    opTwo = font.render("vs. Player", True, ORANGE_YELLOW)
    opThree = font.render("Tutorial", True, ORANGE_YELLOW)
    titleRect = title.get_rect()
    titleRect.center = (width//2, 70)

    screen.blit(title, titleRect)
    screen.blit(opOne, opOneRect)
    screen.blit(opTwo, opTwoRect)
    screen.blit(opThree, opThreeRect)
    pygame.display.update()

def displayWinner(winner):
    font = pygame.font.Font('FFF_Tusj.ttf', 28)
    screen = pygame.display.get_surface()

    pygame.draw.rect(screen, COYOTE_BROWN, (583, 90, 175, 60))
    pygame.draw.rect(screen, CAMEL, (583+3, 90+3, 175-6, 60-6))

    pygame.draw.rect(screen, COYOTE_BROWN, (583, 20, 175, 60))
    pygame.draw.rect(screen, CAMEL, (583+3, 20+3, 175-6, 60-6))


    homeText = font.render("Main Menu", True, ORANGE_YELLOW)
    quitText = font.render("Quit", True, ORANGE_YELLOW)

    font = pygame.font.Font('FFF_Tusj.ttf', 80)

    if winner == "white":
        winText = font.render("White wins!", True, INCHWORM)
    elif winner == "black":
        winText = font.render("Black wins!", True, INCHWORM)
    else:
        winText = font.render("Draw!", True, INCHWORM)

    winRect = winText.get_rect()
    homeRect = homeText.get_rect()
    quitRect = quitText.get_rect()

    winRect.center = (270, 90)
    homeRect.center = (670,50)
    quitRect.center = (670,120)

    screen.blit(winText, winRect)
    screen.blit(homeText, homeRect)
    screen.blit(quitText, quitRect)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                posx = event.pos[0]
                posy = event.pos[1]
                if (583 + 175) >= posx > 583 and (60+20) >= posy > 20:
                    main()
                elif (583 + 175) >= posx > 583 and (60+90) >= posy > 90:
                    sys.exit()

def playBotGame():
    game = Game_Bot()
    gameBoard = game.Board()
    showBoard(gameBoard)
    currentX = 0
    currentY = 0
    firstClick = True

    while True:
        for event in pygame.event.get():
            mPosX = pygame.mouse.get_pos()[0]
            mPosY = pygame.mouse.get_pos()[1]

            if 50 < mPosX <= 750 and 172 < mPosY <= 871 and \
                    ((((mPosX-50)//37)*37+67) != currentX or (((mPosY-172)//37)*37+189) != currentY):
                showBoard(gameBoard)
                pygame.draw.circle(pygame.display.get_surface(), (50, 50, 50),
                                   (((mPosX-50)//37)*37+66, ((mPosY-172)//37)*37+189), 17)
                currentX = ((mPosX-50)//37)*37+67
                currentY = ((mPosY-172)//37)*37+189
                pygame.display.update()

            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if not firstClick:
                    tileX = (mPosX-50)//37
                    tileY = (mPosY-172)//37
                    print(tileX, tileY)
                    print(event.pos[0], event.pos[1])
                    if gameBoard[tileY][tileX] == ".":
                        result = game.result([tileY+1, tileX+1])
                        if result != "None":
                            if result == "Bot":
                                print("b win")
                                showBoard(gameBoard)
                                displayWinner("white")
                            elif result == "Player":
                                print("p win")
                                showBoard(gameBoard)
                                displayWinner("black")
                            else:
                                showBoard(gameBoard)
                                displayWinner("draw")
                        else:
                            gameBoard = game.Board()
                            showBoard(gameBoard)
        firstClick = False

def playUserGame():
    game = Game_SinglePlayer()
    currentPlayer = 0
    gameBoard = game.Board()
    showBoard(gameBoard)
    currentX = 0
    currentY = 0
    firstClick = True

    while True:
        for event in pygame.event.get():
            mPosX = pygame.mouse.get_pos()[0]
            mPosY = pygame.mouse.get_pos()[1]

            if 50 < mPosX <= 750 and 172 < mPosY <= 871 and \
                    ((((mPosX - 50) // 37) * 37 + 67) != currentX or (((mPosY - 172) // 37) * 37 + 189) != currentY):
                showBoard(gameBoard)
                if currentPlayer == 0:
                    pygame.draw.circle(pygame.display.get_surface(), (50, 50, 50),
                                   (((mPosX - 50) // 37) * 37 + 66, ((mPosY - 172) // 37) * 37 + 189), 17)
                else:
                    pygame.draw.circle(pygame.display.get_surface(), (240, 240, 240),
                                       (((mPosX - 50) // 37) * 37 + 66, ((mPosY - 172) // 37) * 37 + 189), 17)
                currentX = ((mPosX - 50) // 37) * 37 + 67
                currentY = ((mPosY - 172) // 37) * 37 + 189
                pygame.display.update()

            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if not firstClick:
                    tileX = (mPosX - 50) // 37
                    tileY = (mPosY - 172) // 37
                    print(tileX, tileY)
                    print(event.pos[0], event.pos[1])
                    if gameBoard[tileY][tileX] == ".":
                        if currentPlayer == 0:
                            result = game.play("b", [tileY + 1, tileX + 1])
                            currentPlayer = 1
                        else:
                            result = game.play("w", [tileY + 1, tileX + 1])
                            currentPlayer = 0

                        if result != "None":
                            if result == "White":
                                showBoard(gameBoard)
                                displayWinner("white")
                            elif result == "Black":
                                showBoard(gameBoard)
                                displayWinner("black")
                            else:
                                showBoard(gameBoard)
                                displayWinner("draw")
                        else:
                            gameBoard = game.Board()
        firstClick = False

def displayWarning(warningPos, isTip):
    font = pygame.font.Font('FFF_Tusj.ttf', 48)
    screen = pygame.display.get_surface()

    x = str(warningPos[1] + 1)
    y = str(warningPos[0] + 1)

    if isTip:
        warnString = "You are about to win at (" + x + "," + y + ")!"
    else:
        warnString = "White is about to win at (" + x + "," + y + ")!"
    warnText = font.render(warnString, True, INCHWORM)
    warnRect = warnText.get_rect()
    warnRect.center = (370, 90)
    screen.blit(warnText, warnRect)
    pygame.display.update()

def playTutorial():
    game = Game_Tutorial()
    gameBoard = game.board()
    showBoard(gameBoard)
    showRules()
    currentX = 0
    currentY = 0
    firstClick = True
    #(warning: boolean, tip: boolean, warning/tip Location: tuple , winner: string)
    result = (False, False, (0, 0), "None")
    while True:
        for event in pygame.event.get():
            mPosX = pygame.mouse.get_pos()[0]
            mPosY = pygame.mouse.get_pos()[1]

            if 50 < mPosX <= 750 and 172 < mPosY <= 871 and \
                    ((((mPosX-50)//37)*37+67) != currentX or (((mPosY-172)//37)*37+189) != currentY):
                showBoard(gameBoard)
                if result[1]:
                    displayWarning(result[2], True)
                elif result[0]:
                    displayWarning(result[2], False)
                pygame.draw.circle(pygame.display.get_surface(), (50, 50, 50),
                                   (((mPosX-50)//37)*37+66, ((mPosY-172)//37)*37+189), 17)
                currentX = ((mPosX-50)//37)*37+67
                currentY = ((mPosY-172)//37)*37+189

                pygame.display.update()

            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if not firstClick:
                    tileX = (mPosX-50)//37
                    tileY = (mPosY-172)//37
                    print(tileX, tileY)
                    print(event.pos[0], event.pos[1])

                    if gameBoard[tileY][tileX] == ".":
                        result = game.result([tileY+1, tileX+1])
                        print("result is", result[3])
                        if result[3] != "None":
                            if result[3] == "Bot":
                                print("b win")
                                showBoard(gameBoard)
                                displayWinner("white")
                            elif result[3] == "Player":
                                print("p win")
                                showBoard(gameBoard)
                                displayWinner("black")
                            else:
                                showBoard(gameBoard)
                                displayWinner("draw")
                        else:
                            gameBoard = game.board()
                            showBoard(gameBoard)
                            if result[1]:
                                displayWarning(result[2], True)
                            elif result[0]:
                                displayWarning(result[2], False)



        firstClick = False

def showRules():
    screen = pygame.display.get_surface()
    pygame.draw.rect(screen, COYOTE_BROWN, (100, 300, 598, 300))
    pygame.draw.rect(screen, CAMEL, (100+3, 300+3, 598-6, 300-6))

    pygame.draw.rect(screen, COYOTE_BROWN, (130, 520, 175, 60))
    pygame.draw.rect(screen, CAMEL, (130+3, 520+3, 175-6, 60-6))

    font = pygame.font.Font('FFF_Tusj.ttf', 40)
    ruleText = font.render("Rules:", True, INCHWORM)

    font = pygame.font.Font('FFF_Tusj.ttf', 30)
    ruleText1 = font.render("Black plays first (you!), then white.", True, INCHWORM)
    ruleText2 = font.render("Place your stones on an empty space", True, INCHWORM)
    ruleText3 = font.render("When a player has 5 stones in a row,", True, INCHWORM)
    ruleText4 = font.render("They win!", True, INCHWORM)
    ruleText5 = font.render("Play!", True, ORANGE_YELLOW)


    ruleRect = ruleText.get_rect()
    ruleRect1 = ruleText1.get_rect()
    ruleRect2 = ruleText2.get_rect()
    ruleRect3 = ruleText3.get_rect()
    ruleRect4 = ruleText4.get_rect()
    ruleRect5 = ruleText5.get_rect()


    ruleRect.center = (210, 330)
    ruleRect1.center = (400, 370)
    ruleRect2.center = (400, 410)
    ruleRect3.center = (400, 450)
    ruleRect4.center = (400, 490)
    ruleRect5.center = (217, 550)


    screen.blit(ruleText, ruleRect)
    screen.blit(ruleText1, ruleRect1)
    screen.blit(ruleText2, ruleRect2)
    screen.blit(ruleText3, ruleRect3)
    screen.blit(ruleText4, ruleRect4)
    screen.blit(ruleText5, ruleRect5)

    pygame.display.update()

    notClicked = True
    while notClicked:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                posx = event.pos[0]
                posy = event.pos[1]
                if (130 + 175) >= posx > 130 and (60 + 520) >= posy > 520:
                    notClicked = False

            if event.type == pygame.QUIT:
                sys.exit()

def showBoard(board):
    width = 800
    height = 920
    size = (width, height)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("GOMOKU")
    pygame.draw.rect(screen, PISTACHIO, (0, 0, width, height))
    pygame.draw.rect(screen, COYOTE_BROWN, (40, 163, 718, 718))
    pygame.draw.rect(screen, (80, 80, 80), (65, 188, 668, 668))

    #Empty Board
    for i in range(18):
        for j in range(18):
            pygame.draw.rect(screen, CAMEL, ((i*37)+((width-(18*37))//2), 190+(j*37), 35, 35))

    #Place pieces
    for i in range(19):
        for j in range(19):
            if board[j][i] == "b":
                pygame.draw.circle(screen, (10, 10, 10), (((i * 37) + ((width - (18 * 37)) // 2)-1), 190 + (j * 37)-1), 17)
            elif board[j][i] == "w":
                pygame.draw.circle(screen, (220, 220, 220), (((i * 37) + ((width - (18 * 37)) // 2)-1), 190 + (j * 37)-1), 17)

    pygame.display.update()

main()