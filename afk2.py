import mouse
import pygame
import sys
import requests
import time

username = input("Enter your intra username: ")

pygame.init()
info = pygame.display.Info()
pygame.mouse.set_visible(False)
width, height = info.current_w, info.current_h
display = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

def check_status():
    url = f"https://raw.githubusercontent.com/hindsighttt/BlackScreen/refs/heads/main/users/{username}"
    response = requests.get(url)
    content = response.text
    if "exit" in content:
        return True
    else:
        return False

def main(move_size):
    for _ in range(100):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pygame.quit()
                    sys.exit()

        if move_size > 0:
            mouse.move(width, height)
            mouse.move(width, height - move_size)
            mouse.move(width - move_size, height - move_size)
            mouse.move(width - move_size, height)
        time.sleep(0.01)

def run():
    move_size = 5
    last_check = time.time()
    status = False

    while True:
        if time.time() - last_check >= 60:
            status = check_status()
            last_check = time.time()
        if status:
            move_size = 0
        else:
            move_size = 5
        main(move_size)

run()

