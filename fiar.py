import pygame
import pygame.freetype
import time
from pygame.locals import Rect

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode([640,480])
pygame.display.set_caption("pygame FourInARow")

font1 = pygame.freetype.Font("fonts/natumemozi.ttf", 48)

running = True
gamenow = True
FPS = 30
WAIT = 0.15

ground = (202, 202, 202)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
CURSOR = (0, 123, 0)



CTRL_KEYS = [[pygame.K_LEFT, "LEFT", -1],
             [pygame.K_RIGHT, "RIGHT", 1],
             [pygame.K_SPACE, "SPACE", 0],
             [pygame.K_0, "WIN", 0]] # デバッグ用

win_flag = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            gamenow = False
    
    whichturn = False
    # False = red, True = blue

    # color = [[0]*9]*9 # 二次元配列
    color = [0]*81 # 一次元配列
    stonecolor = 1
    # 0 = nothing, 1 = red, 2 = blue

    cursor = 4
    #初期位置

    cursor_change = 0
    skip_frames = FPS *WAIT + 1
    update_flag = True

    stonecount = [0]*9
    gamenow = True
    win_flag = False
    print("game start")
    while gamenow == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                gamenow = False
            elif event.type == pygame.KEYDOWN:
                for key in CTRL_KEYS:
                    if event.key == key[0]:
                        if key[1] == "LEFT":
                            cursor_change = key[2]
                            update_flag = True
                        elif key[1] == "RIGHT":
                            cursor_change = key[2]
                            update_flag = True
                        elif key[1] == "SPACE":
                            sta = cursor+(8-stonecount[cursor])*9
                            if stonecount[cursor] < 9:
                                color[sta] = stonecolor #一次元配列
                                # color[8-stonecount[cursor]][cursor] = stonecolor #二次元配列
                                stonecount[cursor] += 1
                                # 勝利判定文 print()はデバッグ用
                                win_flag = True
                                if stonecount[cursor] > 3 and win_flag == True: #下
                                    for x in range(4):
                                        if color[sta+x*9] != stonecolor:
                                            win_flag = False
                                            print("false down")
                                        else:print("gameset")
                                if cursor < 6 and win_flag == True: #右
                                    for x in range (4):
                                        if color[sta+x] != stonecolor:
                                            win_flag = False
                                            print("false right")
                                        else:print("gameset")
                                if cursor > 2 and win_flag == True: # 左
                                    for x in range(4):
                                        if color[sta-x] != stonecolor:
                                            win_flag = False
                                            print("false left")
                                        else:print("gameset")
                                if stonecount[cursor] < 7 and cursor < 6 and win_flag == True: #右上
                                    for x in range(4):
                                        if color[sta-(x*9)+x] != stonecolor:
                                            win_flag = False
                                            print("false right_up")
                                        else:print("gameset")
                                if stonecount[cursor] > 3 and cursor < 6 and win_flag == True: #右下
                                    for x in range(4):
                                        if color[sta+(x*9)+x] != stonecolor:
                                            win_flag = False
                                            print("false right_down")
                                        else:print("gameset")
                                if stonecount[cursor] < 7 and cursor > 2 and win_flag == True: #左上
                                    for x in range(4):
                                        if color[sta-(x*9)-x] != stonecolor:
                                            win_flag = False
                                            print("false left_up")
                                        else:print("gameset")
                                if stonecount[cursor] > 3 and cursor > 2 and win_flag == True: #左下
                                    for x in range(4):
                                        if color[sta+(x*9)-x] != stonecolor:
                                             win_flag = False
                                             print("false left_down")
                                        else:print("gameset")
                                
                                print("stone drop")

                                if whichturn == False:
                                    whichturn = True
                                else:
                                    whichturn = False
                            update_flag = True
                        elif key[1] == "WIN":
                            print("game end debug")
                            win_flag = True
            elif event.type == pygame.KEYUP:
                for key in CTRL_KEYS:
                    if event.type == key[0]:
                        if key[1] == "LEFT":
                            cursor_change = 0
                        elif key[1] == "RIGHT":
                            cursor_change = 0

                     
    
        if update_flag and (skip_frames > FPS * WAIT):
            update_flag = False
            skip_frames = 0
            if cursor + cursor_change >= 0 and cursor + cursor_change <= 8:
                cursor += cursor_change
            cursor_change = 0

        if(whichturn == False):
            stonecolor = 1
        else:  
            stonecolor = 2
    

        screen.fill(ground) # background color

        """
        for x in range(81): #四角を描くコード 二次元配列/for文版 バグあり
            y = x//9
            if color[y][x%9] == 0:
                pygame.draw.rect(screen, WHITE, Rect(48 + x%9 * 32, 70 + y * 32, 24, 24))
            elif color[y][x%9] == 1:
                pygame.draw.rect(screen, RED, Rect(48 + x%9 * 32, 70 + y * 32, 24, 24))
            else:
                pygame.draw.rect(screen, BLUE, Rect(48 + x%9 * 32, 70 + y * 32, 24, 24))
        """


    
        for x in range(81): #四角を描くコード 一次元配列版 正常に動作
            y = x//9
            if color[x] == 0:
                pygame.draw.rect(screen, WHITE, Rect(48 + x%9 * 32, 70 + y * 32, 24, 24))
            elif color[x] == 1:
                pygame.draw.rect(screen, RED, Rect(48 + x%9 * 32, 70 + y * 32, 24, 24))
            else:
                pygame.draw.rect(screen, BLUE, Rect(48 + x%9 * 32, 70 + y * 32, 24, 24))

     

        pygame.draw.rect(screen, CURSOR, Rect(48 + cursor * 32, 24 + 0 * 32, 24, 24))
            
    
        text1, rect1 = font1.render(str(cursor), WHITE)
        rect1.center = (360, 360)
        screen.blit(text1, rect1)

        if win_flag:
            if whichturn == False:
                gamenow =  False
                time.sleep(2)
            else:
                gamenow = False
                time.sleep(2)

        """
        if event.type == pygame.KEYDOWN: #色情報を更新するコード かなり古い
            if event.key == pygame.K_SPACE:
                for down in range(8):
                    if color[cursor][down-1] != 0:
                        color[cursor][down] = 1
        """
        skip_frames += 1
        pygame.display.flip()
        clock.tick(30)

pygame.quit()