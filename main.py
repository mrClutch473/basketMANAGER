import random

import pygame

pygame.init()
screen = pygame.display.set_mode((900, 950)) #, flags=pygame.NOFRAME

#variables
game_status = 0
namesArr = ["Майкл Джордан", "Леброн Джеймс", "Мэджик Джонсон", "Коби Брайант", "Шакил О'Нил", "Ларри Бёрд", "Карим Абдул", "Тим Данкан", "Стивен Карри", "Лука Дончич", "Кайри Ирвинг", "Кевин Дюрант", "Джейсон Тэйтум", "Энтони Эдвардс", "Никола Йокич", "Джимми Батлер", "Кауай Леонард", "Пол Джордж", "Крис Пол"]

#MAIN MENU
menu_logo = pygame.image.load('imges/main_logo.png').convert_alpha()
start_button_img = pygame.image.load('imges/buttons/start_but.png').convert_alpha()
start_button_rect = start_button_img.get_rect(topleft=(200, 600))

pygame.display.set_caption("BaskeT_ManageR")
iconM = pygame.image.load('imges/bsket_icon.png').convert_alpha()
pygame.display.set_icon(iconM)

#FONTS
mainFont = pygame.font.Font('fonts/ShantellSans-VariableFont_BNCE,INFM,SPAC,wght.ttf', 40)
mainBaldFont = pygame.font.Font('fonts/ShantellSans-VariableFont_BNCE,INFM,SPAC,wght.ttf', 40)
mainBaldFont.set_bold(True)
cardsFont = pygame.font.Font('fonts/ShantellSans-VariableFont_BNCE,INFM,SPAC,wght.ttf', 16)
cardsFontBald = pygame.font.Font('fonts/ShantellSans-VariableFont_BNCE,INFM,SPAC,wght.ttf', 18)
cardsFontBald.set_bold(True)
cardsPriseFont = pygame.font.Font('fonts/ShantellSans-VariableFont_BNCE,INFM,SPAC,wght.ttf', 26)
valFont = pygame.font.Font('fonts/YujiMai-Regular.ttf', 40)

#DRAFT MENU
money = 1000
moneyOUT = str(str(money) + ' $')
money_text = valFont.render(moneyOUT, True, (46, 46, 48))
square_mon = pygame.Surface((170, 70))
square_mon.fill((210, 143, 82))

my_team_text = mainBaldFont.render("Your Team: ", True, (46, 46, 48))
draft_text = mainBaldFont.render("Draft: ", True, (46, 46, 48))

my_teamArr = []
draft_teamArr = []
id_gen = 0
pl_card_x = 20
pl_card_y = 475
for i in range(12):
    ic_gen = "imges/players/pl" + str(random.randint(1,20)) + ".png"
    icmin_gen = "imges/players/pl_mini" + str(random.randint(1, 20)) + ".png"
    draft_teamArr.append({
        "name":namesArr[random.randint(0, len(namesArr)-1)],
        "age":random.randint(18,40),
        "icon":pygame.image.load(ic_gen),
        "prise":random.randint(0,400),
        "icon_mini": pygame.image.load(icmin_gen),
        "id":id_gen,
        "rect":(pl_card_x,pl_card_y, 125, 200),
        "x": pl_card_x,
        "y": pl_card_y
    })
    pl_card_x += 145
    if id_gen == 5:
        pl_card_x = 20
        pl_card_y = 730
    id_gen+=1

#SOUND
tr1 = pygame.mixer.Sound('sounds/main_theme/track2(get_jiggy).mp3')
tr1.set_volume(0.1)
tr2 = pygame.mixer.Sound('sounds/main_theme/track1(where_is_my_head_at).mp3')
tr2.set_volume(0.05)


#MAIN REALIZATION
music_cheked = False
running = True
while running:

    if game_status == 0:
        if not music_cheked:
            tr1.play()
            music_cheked = True
        screen.fill((210, 143, 82))

        screen.blit(menu_logo, (150, 100))
        screen.blit(start_button_img, start_button_rect)


        if start_button_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            game_status = 1
            tr1.stop()
            music_cheked = False
    elif game_status == 1:
        if not music_cheked:
            tr2.play()
            music_cheked = True
        screen.fill((147, 101, 59))

        #screen.blit(square_mon, (730,0))
        screen.blit(money_text, (740, 0))
        screen.blit(my_team_text, (360, 150))
        screen.blit(draft_text, (410, 380))

        if draft_teamArr:
            for el in draft_teamArr:
                pygame.draw.rect(screen, (135, 135, 145), el.get('rect'))
                pygame.draw.rect(screen, (112, 112, 121), (el.get('x')+5,el.get('y')+10,115,180))
                screen.blit(el.get('icon_mini'), (el.get('x')+12,el.get('y')+10))

                screen.blit(cardsFontBald.render("Имя:", True, (0,0,0)), (el.get('x')+40,el.get('y')+80))
                screen.blit(cardsFontBald.render("Возраст:", True, (0, 0, 0)), (el.get('x') + 25, el.get('y') + 140))

                nsplit = el.get('name').split()
                n1 = cardsFont.render(nsplit[0], True, (46, 46, 48))
                n2 = cardsFont.render(nsplit[1], True, (46, 46, 48))
                screen.blit(n1, (el.get('x')+20,el.get('y')+100))
                screen.blit(n2, (el.get('x') + 20, el.get('y') + 120))

                screen.blit(cardsFont.render(str(el.get('age')), True, (46, 46, 48)), (el.get('x') + 52, el.get('y') + 165))

                screen.blit(cardsPriseFont.render((str(el.get('prise'))+'$'), True, (46, 46, 48)),(el.get('x') + 35, el.get('y') - 35))




    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
