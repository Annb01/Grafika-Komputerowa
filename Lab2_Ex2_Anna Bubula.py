import pygame

pygame.init()
win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Z")

CZERWONY = (255, 0, 0)
BIALY = (255, 255, 255)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.fill(BIALY)

    szerokosc_kwadratu = 20
    wysokosc_kwadratu = 20

    kwadrat_surface = pygame.Surface((szerokosc_kwadratu, wysokosc_kwadratu), pygame.SRCALPHA)
    kwadrat_surface.fill(CZERWONY)

    skala_szerokosci = 25
    szerokosc_po_skalowaniu = int(szerokosc_kwadratu * skala_szerokosci)
    skalowany_kwadrat_surface = pygame.transform.scale(kwadrat_surface, (szerokosc_po_skalowaniu, wysokosc_kwadratu))

    win.blit(skalowany_kwadrat_surface, (50, 40))

    szerokosc_kwadratu2 = 20
    wysokosc_kwadratu2 = 20

    kwadrat_surface2 = pygame.Surface((szerokosc_kwadratu2, wysokosc_kwadratu2), pygame.SRCALPHA)
    kwadrat_surface2.fill(CZERWONY)

    skala_szerokosci2 = 35
    szerokosc_po_skalowaniu2 = float(szerokosc_kwadratu2 * skala_szerokosci2)
    skalowany_kwadrat_surface2 = pygame.transform.scale(kwadrat_surface2, (szerokosc_po_skalowaniu2, wysokosc_kwadratu2))

    obrocony_kwadrat_surface2 = pygame.transform.rotate(skalowany_kwadrat_surface2, 45)
    win.blit(obrocony_kwadrat_surface2, (48, 40))

    szerokosc_kwadratu3 = 20
    wysokosc_kwadratu3 = 20

    kwadrat_surface3 = pygame.Surface((szerokosc_kwadratu3, wysokosc_kwadratu3), pygame.SRCALPHA)
    kwadrat_surface3.fill(CZERWONY)

    skala_szerokosci3 = 25
    szerokosc_po_skalowaniu3 = int(szerokosc_kwadratu3 * skala_szerokosci3)
    skalowany_kwadrat_surface3 = pygame.transform.scale(kwadrat_surface3, (szerokosc_po_skalowaniu3, wysokosc_kwadratu3))

    win.blit(skalowany_kwadrat_surface3, (55, 535))
    pygame.display.update()


