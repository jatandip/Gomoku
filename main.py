import pygame
from Game_Bot import Game_Bot
import math

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
            if event.type == pygame.MOUSEBUTTONDOWN:
                posx = event.pos[0]
                posy = event.pos[1]
                if (28+342) >= posx > 28 and (140+100) >= posy > 140:   #vs bot
                    #print("click1")
                    pygame.display.quit()
                    selectionMade = True
                    playBotGame()
                elif (28+342) >= posx > 28 and (253+100) >= posy > 253: #vs player
                    print("click2")
                    pygame.display.quit()
                    selectionMade = True
                    #playUserGame()
                elif (28+342) >= posx > 28 and (366+100) >= posy > 366: #tutorial
                    print("click3")
                    pygame.display.quit()
                    selectionMade = True
                    #playTutorial()


def displayMenu():
    width = 400
    height = 500
    size = (width, height)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("GOMOKU")

    pygame.draw.rect(screen, PISTACHIO, (0, 0, width, height))

    pygame.draw.rect(screen, COYOTE_BROWN, (28, 140, 342, 100))
    opOneRect = pygame.draw.rect(screen, CAMEL, (28+3, 140+3, 342-6, 100-6))
    opOneRect.center = (250, 140+(148//2))

    pygame.draw.rect(screen, COYOTE_BROWN, (28, 253, 342, 100))
    opTwoRect = pygame.draw.rect(screen, CAMEL, (28+3, 253+3, 342-6, 100-6))
    opTwoRect.center = (270, 253+(148//2))

    pygame.draw.rect(screen, COYOTE_BROWN, (28, 366, 342, 100))
    opThreeRect = pygame.draw.rect(screen, CAMEL, (28+3, 366+3, 342-6, 100-6))
    opThreeRect.center = (280, 366+(148//2))

    font = pygame.font.Font('Bitink.ttf', 100)
    title = font.render("Gomoku", True, INCHWORM)
    font = pygame.font.Font('Bitink.ttf', 48)
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

def playBotGame():
    game = Game_Bot()
    gameBoard = game.Board()
    showBoard(gameBoard)
    leftPad = 50
    topPad = 172
    currentX = 0
    currentY = 0

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

            if event.type == pygame.MOUSEBUTTONDOWN:
                print((mPosX-50)//37, (mPosY-172)//37)
                print(event.pos[0], event.pos[1])
                result = game.result([((mPosX-50)//37)+1, (mPosY-172)//37+1])


def playUserGame():
    pass

def playTutorial():
    pass

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
            #print("looking at: ", board[j][i])
            if board[j][i] == "b":
                pygame.draw.circle(screen, (10, 10, 10), (((i * 37) + ((width - (18 * 37)) // 2)-1), 190 + (j * 37)-1), 17)
            elif board[j][i] == "w":
                pygame.draw.circle(screen, (220, 220, 220), (((i * 37) + ((width - (18 * 37)) // 2)-1), 190 + (j * 37)-1), 17)

    pygame.display.update()

main()