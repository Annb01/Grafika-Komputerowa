from math import sin, cos, pi
import pygame
import sys

pygame.init()

win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Wielokąt")

ZOLTY = (255, 255, 0)
NIEBIESKI = (0, 0, 255)


wielokat = [
    (300 + 150 * cos(2 * pi * i / 8), 
     300 + 150 * sin(2 * pi * i / 8))
    for i in range(8)
]

while True:
    win.fill(ZOLTY)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                pygame.draw.polygon(win, NIEBIESKI, wielokat)
                pygame.display.flip()

            if event.key == pygame.K_2:
                win.fill(ZOLTY)
                odwracane = pygame.Surface((600, 600), pygame.SRCALPHA)
                powiększony_walec = [
                    (300 + 1.8 * 150 * cos(2 * pi * i / 8), 
                     300 + 1.8 * 150 * sin(2 * pi * i / 8))
                    for i in range(8)
                ]
                pygame.draw.polygon(odwracane, NIEBIESKI, powiększony_walec)
                odwracane = pygame.transform.rotate(odwracane, 50)
                rect = odwracane.get_rect(center=(300, 300))
                win.blit(odwracane, rect.topleft)
                pygame.display.flip()

            if event.key == pygame.K_3:
                win.fill(ZOLTY)
                odwracane = pygame.Surface((600, 600), pygame.SRCALPHA)
                powiększony_walec = [
                    (300 +  150 * cos(2 * pi * i / 8), 
                     300 + 1.5 * 150 * sin(2 * pi * i / 8))
                    for i in range(8)
                ]
                pygame.draw.polygon(odwracane, NIEBIESKI, powiększony_walec)
                odwracane = pygame.transform.rotate(odwracane, 180)
                odwracane = pygame.transform.flip(odwracane,True,False)
                rect = odwracane.get_rect(center=(300, 300))
                win.blit(odwracane, rect.topleft)
                pygame.display.flip()

            if event.key == pygame.K_4:
                win.fill(ZOLTY)
                odwracane = pygame.Surface((600, 600), pygame.SRCALPHA)
                
                powiększony_walec = [
                    (300 + 150 * cos(2 * pi * i / 8), 
                    300 + 150 * sin(2 * pi * i / 8))
                    for i in range(8)
                ]
                przesuniete_punkty = [
                    (point[0] +20  if i < 4 else point[0] - 20, point[1])
                    for i, point in enumerate(powiększony_walec)
                ]
                pygame.draw.polygon(odwracane, NIEBIESKI, przesuniete_punkty)
                odwracane = pygame.transform.rotate(odwracane, -22)
                rect = odwracane.get_rect(center=(300, 300))
                win.blit(odwracane, rect.topleft)
                pygame.display.flip()


            if event.key == pygame.K_5:
                win.fill(ZOLTY)
                odwracane = pygame.Surface((600, 600), pygame.SRCALPHA)
                powiększony_walec = [
                    (300 + 1.5 * 150 * cos(2 * pi * i / 8), 
                     300 + 150 * sin(2 * pi * i / 8))
                    for i in range(8)
                ]
                przesuniecie_w_gore = 150
                przesunieta_figura = [
                    (point[0], point[1] - przesuniecie_w_gore)
                    for point in powiększony_walec
                ]
                
                pygame.draw.polygon(odwracane, NIEBIESKI, przesunieta_figura)
                rect = odwracane.get_rect(center=(300, 300))
                win.blit(odwracane, rect.topleft)
                pygame.display.flip()

            if event.key == pygame.K_6:
                win.fill(ZOLTY)
                odwracane = pygame.Surface((600, 600), pygame.SRCALPHA)
                
                powiększony_walec = [
                    (300 + 1.5 * 150 * cos(2 * pi * i / 8), 
                    300 + 1.5 * 150 * sin(2 * pi * i / 8))
                    for i in range(8)
                ]
                przesuniete_punkty = [
                    (point[0] +20  if i < 4 else point[0] - 20, point[1])
                    for i, point in enumerate(powiększony_walec)
                ]
                pygame.draw.polygon(odwracane, NIEBIESKI, przesuniete_punkty)
                odwracane = pygame.transform.rotate(odwracane, -100)
                rect = odwracane.get_rect(center=(300, 300))
                win.blit(odwracane, rect.topleft)
                pygame.display.flip()

            if event.key == pygame.K_7:
                win.fill(ZOLTY)
                odwracane = pygame.Surface((600, 600), pygame.SRCALPHA)
                powiększony_walec = [
                    (300 +  150 * cos(2 * pi * i / 8), 
                     300 + 1.5 * 150 * sin(2 * pi * i / 8))
                    for i in range(8)
                ]
                pygame.draw.polygon(odwracane, NIEBIESKI, powiększony_walec)
                odwracane = pygame.transform.rotate(odwracane, 180)
                rect = odwracane.get_rect(center=(300, 300))
                win.blit(odwracane, rect.topleft)
                pygame.display.flip()

            if event.key == pygame.K_8:
                win.fill(ZOLTY)
                odwracane = pygame.Surface((600, 600), pygame.SRCALPHA)
                powiększony_walec = [
                    (300 +  150 * cos(2 * pi * i / 8), 
                     300 + 1.5 * 150 * sin(2 * pi * i / 8))
                    for i in range(8)
                ]
                pygame.draw.polygon(odwracane, NIEBIESKI, powiększony_walec)
                odwracane = pygame.transform.rotate(odwracane, 40)

                rect = odwracane.get_rect(center=(200, 400))
                win.blit(odwracane, rect.topleft)
                pygame.display.flip()
            
            if event.key == pygame.K_9:
                win.fill(ZOLTY)
                odwracane = pygame.Surface((600, 600), pygame.SRCALPHA)
                
                powiększony_walec = [
                    (300 + 1.5 * 150 * cos(2 * pi * i / 8), 
                    300 + 1.5 * 150 * sin(2 * pi * i / 8))
                    for i in range(8)
                ]
                przesuniete_punkty = [
                    (point[0] +20  if i < 4 else point[0] - 20, point[1])
                    for i, point in enumerate(powiększony_walec)
                ]
                pygame.draw.polygon(odwracane, NIEBIESKI, przesuniete_punkty)
                odwracane = pygame.transform.rotate(odwracane, -216)
                rect = odwracane.get_rect(center=(400, 300))
                win.blit(odwracane, rect.topleft)
                pygame.display.flip()






               


            

                

