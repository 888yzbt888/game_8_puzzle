import sys
import pygame
import random
import time
import numpy as np
import algorithm_8_puzzle
REPLAY_SPEED=0.4
XOFFSET = 30
YOFFSET = 15
WINDOW_HEIGHT=440
WINDOW_WIDTH=400
FINAL_STATE=[[1,2,3],[4,5,6],[7,8,0]]
def initgame():
    img = []
    for i in range(0, 9):
        img.append(pygame.image.load(str(i) + ".bmp"))
    game=Game()
    state=game.getState()
    return game,state,img
#move to algorithm
def find_0_posi(block):
    return [int(np.where(block == 0)[0]), int(np.where(block == 0)[1])]#[row,col]
#move to algorithm
def if_solvable(block):
    block=block.reshape(9)
    posi=int(np.where(block==0)[0])
    total_rev=0
    for i in range(1,9):
        for k in range(i):
            if block[k]>block[i]:
                total_rev=total_rev+1
    if (total_rev+posi)%2==0:
        return True
    else:
        return False
class Game:
    def __init__(self):
        self.block=np.array(random.sample(range(9),9))
        self.block=self.block.reshape((3,3))
        print("yes" if if_solvable(self.block) else "no")##
    def move(self,action):
        #print(action)
        if self.checkvalid(action)==False:
            return self.block,"invalid"
        else:
            posi = find_0_posi(self.block)
            if action=="down":
                tem=self.block[posi[0]-1,posi[1]]
                self.block[posi[0]-1,posi[1]]=self.block[posi[0],posi[1]]
                self.block[posi[0],posi[1]]=tem
            if action=="up":
                tem = self.block[posi[0]+1, posi[1]]
                self.block[posi[0]+1, posi[1]] = self.block[posi[0], posi[1]]
                self.block[posi[0], posi[1]] = tem
            if action=="left":
                tem = self.block[posi[0], posi[1]+1]
                self.block[posi[0], posi[1]+1] = self.block[posi[0], posi[1]]
                self.block[posi[0], posi[1]] = tem
            if action=="right":
                tem = self.block[posi[0], posi[1] - 1]
                self.block[posi[0], posi[1] - 1] = self.block[posi[0], posi[1]]
                self.block[posi[0], posi[1]] = tem
        return self.block,"done"

    def checkvalid(self,action):
        if action=="down" or action=="up" or action=="left" or action=="right":
            posi = find_0_posi(self.block)
            if posi[0]==0 and action=="down":
                return False
            if posi[0]==2 and action=="up":
                return False
            if posi[1]==0 and action=="right":
                return False
            if posi[1]==2 and action=="left":
                return False
            return True
        else:
            return False

    def getState(self):
        return self.block

def display_img(state,screen,img):
    pygame.display.update()
    screen.blit(img[state[0, 0]], (0 + XOFFSET, 0 + YOFFSET))
    screen.blit(img[state[0, 1]], (120 + XOFFSET, 0 + YOFFSET))
    screen.blit(img[state[0, 2]], (240 + XOFFSET, 0 + YOFFSET))
    screen.blit(img[state[1, 0]], (0 + XOFFSET, 140 + YOFFSET))
    screen.blit(img[state[1, 1]], (120 + XOFFSET, 140 + YOFFSET))
    screen.blit(img[state[1, 2]], (240 + XOFFSET, 140 + YOFFSET))
    screen.blit(img[state[2, 0]], (0 + XOFFSET, 280 + YOFFSET))
    screen.blit(img[state[2, 1]], (120 + XOFFSET, 280 + YOFFSET))
    screen.blit(img[state[2, 2]], (240 + XOFFSET, 280 + YOFFSET))
def user(screen):
    game, state, img = initgame()
    sol=if_solvable(state)
    esc=False
    while True:
        if sol==False and esc==True:
            break
        if (state==FINAL_STATE).all():
            break
        action=""
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                k=event.key
                if k==pygame.K_LEFT:
                    action="left"
                elif k==pygame.K_RIGHT:
                    action="right"
                elif k==pygame.K_UP:
                    action="up"
                elif k==pygame.K_DOWN:
                    action="down"
                elif k==pygame.K_ESCAPE:
                    esc=True
        state,msg=game.move(action)
        #print(msg,action)
        display_img(state,screen,img)
    if esc==False:
        while True:
            end = False
            display_img(state, screen, img)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    end = True
            if end == True:
                break
    else:
        pass
def auto(screen):
    game, state, img = initgame()
    if if_solvable(state):
        while True:
            print(state)#
            procedure = algorithm_8_puzzle.solve(state)
            print(procedure)#
            l=len(procedure)
            if l>0:
                if procedure[0]=="finish":
                    break
            for action in procedure:
                state, msg = game.move(action)
                #print(msg, action)
                display_img(state,screen,img)
                time.sleep(REPLAY_SPEED)
    else:
        print("unsolvable")
    while True:
        end = False
        display_img(state, screen, img)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                end = True
        if end == True:
            break
def menu():
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
    pygame.display.set_caption("Game")
    pygame.init()
    menu_option_img=[]
    menu_option_img.append(pygame.image.load("Manual.bmp"))
    menu_option_img.append(pygame.image.load("Auto.bmp"))
    menu_option_img.append(pygame.image.load("Exit.bmp"))
    while True:
        pygame.display.update()
        screen.fill([0,0,0])
        screen.blit(menu_option_img[0],(10,80))
        screen.blit(menu_option_img[1],(210,80))
        screen.blit(menu_option_img[2],(110,300))
        option=""
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                k=event.key
                if k==pygame.K_LEFT:
                    option="manual"
                elif k==pygame.K_RIGHT:
                    option="auto"
                elif k==pygame.K_DOWN:
                    option="exit"
        if option=="manual":
            screen.fill([0,0,0])
            user(screen)
        elif option=="auto":
            screen.fill([0, 0, 0])
            auto(screen)
        elif option=="exit":
            print("exit")
            pygame.quit()
            sys.exit()

def main():
    menu()
if __name__ == '__main__' :
    main()
