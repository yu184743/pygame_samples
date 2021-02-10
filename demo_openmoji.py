# demo for openmoji,  open-source emoji
#
# https://github.com/hfg-gmuend/openmoji
# https://hfg-gmuend.github.io/openmoji/  # click to get the codepoint
#
# https://www.emojiall.com/ja/platform-openmoji
# https://emojipedia.org/openmoji/

import pygame
import pygame.freetype

# import time


DARK_GRAY = (40, 40, 40)
GRAY = (80, 80, 80)
RED = (255, 0, 0)
GREEN = (10, 250, 10)
CYAN = (120, 120, 250)
YELLOW = (250, 250, 20)
WHITE = (250, 250, 250)

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("openmoji")

clock = pygame.time.Clock()

font1 = pygame.freetype.Font("fonts/OpenMoji-Color.ttf", 96)
font2 = pygame.freetype.Font("fonts/natumemozi.ttf", 24)

# message1 = ""
# for i in range(0x1F9E0, 0x1F9FF):
#     message1 += chr(i)
# print(message1)

TOP_CODE_POINT = 0x1F3A0


def emoji_display(x, y):
    code_point = TOP_CODE_POINT + int(y / 16) * 8 + int(x / 16)
    text1, rect1 = font1.render(chr(code_point))
    rect1.center = (x, y)
    screen.blit(text1, rect1)
    # print codepoint
    text2, rect2 = font2.render(hex(code_point).upper(), RED)
    rect2.center = (WINDOW_WIDTH / 2, y + 40)
    screen.blit(text2, rect2)


def infinite_loop():
    x = WINDOW_WIDTH * 0.5
    y = WINDOW_HEIGHT * 0.5

    x_change = 0
    y_change = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -1
                if event.key == pygame.K_RIGHT:
                    x_change = 1
                if event.key == pygame.K_UP:
                    y_change = -1
                if event.key == pygame.K_DOWN:
                    y_change = 1

            if event.type == pygame.KEYUP:
                if (
                    event.key == pygame.K_LEFT
                    or event.key == pygame.K_RIGHT
                    or event.key == pygame.K_UP
                    or event.key == pygame.K_DOWN
                ):
                    x_change = 0
                    y_change = 0

        x += x_change
        y += y_change

        if x > WINDOW_WIDTH:
            x = WINDOW_WIDTH
        if y > WINDOW_HEIGHT:
            y = WINDOW_HEIGHT
        if x < 0:
            x = 0
        if y < 0:
            y = 0

        screen.fill(WHITE)
        emoji_display(x, y)

        pygame.display.update()
        clock.tick(60)


infinite_loop()
pygame.quit()
