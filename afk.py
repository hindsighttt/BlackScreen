import mouse
import pygame
import sys

pygame.init()
info = pygame.display.Info()
pygame.mouse.set_visible(False)
width, height = info.current_w, info.current_h
display = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

def main(move_size):
    while True:
        print("can't catch me")
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pygame.quit()
                    sys.exit()
        mouse.move(width, height)
        mouse.move(width, height - move_size)
        mouse.move(width - move_size , height - move_size)
        mouse.move(width - move_size , height)

main(5)
