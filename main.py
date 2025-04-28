import random
import time

import pygame
from pygame import USEREVENT

pygame.init()
screen = pygame.display.set_mode((900, 950)) #, flags=pygame.NOFRAME

#variables
game_status = 1

namesArr = ["Майкл Джордан", "Леброн Джеймс", "Мэджик Джонсон", "Коби Брайант", "Шакил О'Нил", "Ларри Бёрд", "Карим Абдул", "Тим Данкан", "Стивен Карри", "Лука Дончич", "Кайри Ирвинг", "Кевин Дюрант", "Джейсон Тэйтум", "Энтони Эдвардс", "Никола Йокич", "Джимми Батлер", "Кауай Леонард", "Пол Джордж", "Крис Пол"]

end_time_l = 5

my_teamArr_pos = [0] * 6
my_teamArr = []
id_team = 0
tm_card_x = 170
tm_card_y = 175
cur_add_id = 0

#LOADING_SCREEN
loading_img = pygame.image.load('imges/loading_icn.png').convert_alpha()

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


square_mon = pygame.Surface((170, 70))
square_mon.fill((210, 143, 82))

my_team_text = mainBaldFont.render("Your Team: ", True, (46, 46, 48))
draft_text = mainBaldFont.render("Draft: ", True, (46, 46, 48))

    #DRAFT_POSIGILITY
draft_teamArr = []
id_gen = 0
pl_card_x = 20
pl_card_y = 475
for i in range(16):
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
        "y": pl_card_y,
        "rect_colider": pygame.Rect(pl_card_x,pl_card_y, 125, 200)
    })
    pl_card_x += 145
    if id_gen == 7:
        pl_card_x = 20
        pl_card_y = 730
    id_gen+=1


def back_to_draft(dr_card, cr_rec, cr_x, cr_y, cr_rec_col, cr_id):
    global id_team, tm_card_x, tm_card_y
    draft_teamArr.append({
        "name": dr_card.get('name'),
        "age": dr_card.get('age'),
        "icon": dr_card.get('icon'),
        "prise": dr_card.get('prise'),
        "icon_mini": dr_card.get('icon_mini'),
        "id": cr_id,
        "rect": cr_rec,
        "x": cr_x,
        "y": cr_y,
        "rect_colider": cr_rec_col,
    })
    id_team -= 1
    print(my_teamArr_pos)

    #TEAM_POSIBILITY
def add_to_my_team(dr_card, pr_rec, pr_x, pr_y, pr_rec_col, pr_id):
    global id_team, tm_card_x, tm_card_y, cur_add_id
    if id_team<6:
        for j in range(6):
            if my_teamArr_pos[j] == 0:
                print("add_arr indx: " + str(j))
                my_teamArr_pos[j] = 1
                if j == 0:
                    tm_card_x = 170
                    cur_add_id = 0
                elif j == 1:
                    tm_card_x = 315
                    cur_add_id = 1
                elif j == 2:
                    tm_card_x = 460
                    cur_add_id = 2
                elif j == 3:
                    tm_card_x = 605
                    cur_add_id = 3
                elif j == 4:
                    tm_card_x = 750
                    cur_add_id = 4
                elif j == 5:
                    tm_card_x = 895
                    cur_add_id = 5
                break
        print(my_teamArr_pos)
        my_teamArr.append({
            "name": dr_card.get('name'),
            "age": dr_card.get('age'),
            "icon": dr_card.get('icon'),
            "prise": dr_card.get('prise'),
            "icon_mini": dr_card.get('icon_mini'),
            "id": cur_add_id,
            "rect": (tm_card_x, tm_card_y, 125, 200),
            "x": tm_card_x,
            "y": tm_card_y,
            "rect_colider": pygame.Rect(tm_card_x, tm_card_y, 125, 200),
            "prev_rect": pr_rec,
            "prev_x": pr_x,
            "prev_y": pr_y,
            "prev_rect_colider": pr_rec_col,
            "prev_id": pr_id
        })
        id_team+=1
        return True
    else:
        print("В команде нет места")
        return False


#SOUND
tr1 = pygame.mixer.Sound('sounds/main_theme/track2(get_jiggy).mp3')
tr1.set_volume(0.1)
tr2 = pygame.mixer.Sound('sounds/main_theme/track1(where_is_my_head_at).mp3')
tr2.set_volume(0.05)


#MAIN REALIZATION
music_cheked = False
running = True
click_check = False
delay_gm_2_check = True



while running:
    if game_status == 0:
        screen.fill((247, 204, 161))

        screen.blit(menu_logo, (150, 100))
        screen.blit(loading_img, (275, 500))
        if delay_gm_2_check:
            start_time_l = time.time()
            delay_gm_2_check = False

        current_time_l = int(time.time()-start_time_l)
        if current_time_l is end_time_l:
            tr1.stop()
            music_cheked = False
            game_status = 2

    elif game_status == 1:
        if not music_cheked:
            tr1.play()
            music_cheked = True
        screen.fill((210, 143, 82))

        screen.blit(menu_logo, (150, 100))
        screen.blit(start_button_img, start_button_rect)


        if start_button_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            game_status = 0
    elif game_status == 2:
        moneyOUT = str(str(money) + ' $')
        money_text = valFont.render(moneyOUT, True, (46, 46, 48))
        if not music_cheked:
            pygame.display.set_mode((1200, 950))
            tr2.play()
            music_cheked = True
        screen.fill((147, 101, 59))

        #screen.blit(square_mon, (730,0))
        screen.blit(money_text, (1040, 0))
        screen.blit(my_team_text, (510, 120))
        screen.blit(draft_text, (560, 380))

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

        if my_teamArr:
            for el in my_teamArr:
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




        if pygame.mouse.get_pressed()[0]:
            for (i,el) in enumerate(draft_teamArr):
                if el.get('rect_colider').collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                    if not click_check:
                        if (money - el.get('prise'))>=0:
                            if add_to_my_team(el, el.get('rect'), el.get('x'), el.get('y'), el.get('rect_colider'), el.get('id')):
                                draft_teamArr.pop(i)
                                money -= el.get('prise')
                        else:
                            print("У вас не хватает денег!")
                        click_check = True
            for (i,el) in enumerate(my_teamArr):
                if el.get('rect_colider').collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                    if not click_check:
                        print("del_arr indx: " + str(el.get('id')))
                        my_teamArr_pos[el.get('id')] = 0
                        back_to_draft(el, el.get('prev_rect'), el.get('prev_x'), el.get('prev_y'), el.get('prev_rect_colider'), el.get('prev_id'))
                        my_teamArr.pop(i)
                        money += el.get('prise')
                        click_check = True
        else:
            click_check = False



    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()