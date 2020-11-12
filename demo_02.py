# demo for 7-segment simulation

import pygame
from pygame.locals import Rect

from seven_seg_pg import Seven_seg


DARK_GRAY = (40, 40, 40)
GRAY = (80, 80, 80)
RED = (255, 0, 0)
GREEN = (10, 250, 10)
YELLOW = (250, 250, 20)
WHITE = (250, 250, 250)

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode([320, 320])
pygame.display.set_caption("pygame 7-segment display simulation")
screen.fill(DARK_GRAY)

display1 = Seven_seg(screen)
display1.init_col(BLOCK_SIZE=6, BLOCK_INTV=8, COLOR_ON=GREEN, COLOR_OFF=GRAY)
display1.init_line(X_ORG=2, Y_ORG=8, X_INTV=6)

display2 = Seven_seg(screen)
display2.init_col(BLOCK_SIZE=3, BLOCK_INTV=4, COLOR_ON=RED, COLOR_OFF=GRAY)
display2.init_line(X_ORG=14, Y_ORG=30, X_INTV=6)

display3 = Seven_seg(screen)
display3.init_col(BLOCK_SIZE=3, BLOCK_INTV=4, COLOR_ON=YELLOW, COLOR_OFF=GRAY)
display3.init_line(X_ORG=8, Y_ORG=40, X_INTV=6)

display4 = Seven_seg(screen)
display4.init_col(BLOCK_SIZE=6, BLOCK_INTV=8, COLOR_ON=WHITE, COLOR_OFF=GRAY)
display4.init_line(X_ORG=2, Y_ORG=30, X_INTV=8)


running = True
# infinite loop top ----
while running:
    for count in range(16 ** 4):  # 0から65535まで
        # press ctrl-c or close the window to stop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if not running:
            break
        # 「for count」のループから抜ける。whileループも抜ける。

        display1.update(col=0, num=count // (16 ** 3)) # 4096の位
        display1.update(col=1, num=count // (16 ** 2)) # 256の位
        display1.update(col=2, num=count // 16)  # 16の位
        display1.update(col=3, num=count % 16)   # 1の位

        display2.update(col=0, num=count // (16 ** 3))  # 4096の位
        display2.update(col=1, num=count // (16 ** 2))  # 256の位

        display3.update(col=0, num=(count // (16 ** 2)) // 100, base=10)
        display3.update(col=1, num=(count // (16 ** 2)) // 10, base=10)
        display3.update(col=2, num=(count // (16 ** 2)), base=10)

        display4.update(col=0, num=0, base=10)
        display4.update(col=1, num=1, base=10)
        display4.update(col=2, num=2, base=10)
        display4.update(col=3, num=12)
        display4.update(col=4, num=15, base=16)

        pygame.display.flip()  # update
        clock.tick(120)  # FPS, Frame Per Second
# infinit loop bottom ----

pygame.quit()