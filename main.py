import pygame
from pygame.locals import *


def draw_block():
    surface.fill((91, 180, 181))
    surface.blit(block, (block_x, block_y))
    pygame.display.flip()


if __name__ == "__main__":
    pygame.init()

    moveRate = 10
    windowWidth = 1000
    windowHeight = 600
    surface = pygame.display.set_mode((windowWidth, windowHeight))
    surface.fill((91, 180, 181))

    block = pygame.image.load("resources/block.jpg").convert()
    block_x = 100
    block_y = 100
    surface.blit(block, (block_x, block_y))

    pygame.display.flip()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:

                if event.key == K_ESCAPE:
                    running = False
                if event.key == K_UP:
                    block_y -= moveRate
                    draw_block()
                if event.key == K_DOWN:
                    block_y += moveRate
                    draw_block()
                if event.key == K_LEFT:
                    block_x -= moveRate
                    draw_block()
                if event.key == K_RIGHT:
                    block_x += moveRate
                    draw_block()
            elif event.type == QUIT:
                running = False
