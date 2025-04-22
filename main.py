import pygame

pygame.init()

screen = pygame.display.set_mode((900, 900)) #, flags=pygame.NOFRAME
pygame.display.set_caption("BaskeT_ManageR")
iconM = pygame.image.load('imges/bsket_icon.png')
pygame.display.set_icon(iconM)

mainFont = pygame.font.Font('fonts/ShantellSans-VariableFont_BNCE,INFM,SPAC,wght.ttf', 40)
valFont = pygame.font.Font('fonts/YujiMai-Regular.ttf', 40)

money = 1000
moneyOUT = str(str(money) + ' $')
text_surface = valFont.render(moneyOUT, True, (46, 46, 48))
square_mon = pygame.Surface((170, 70))
square_mon.fill((147, 101, 59))

running = True
while running:
    screen.fill((210, 143, 82))
    screen.blit(square_mon, (730,0))
    screen.blit(text_surface, (740, 0))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
