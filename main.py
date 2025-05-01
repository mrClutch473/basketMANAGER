import random
import time

import os
import pygame
from pygame import USEREVENT

os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
screen = pygame.display.set_mode((900, 950)) #, flags=pygame.NOFRAME

#variables
game_status = -1

namesArr = ["Майкл Джордан", "Леброн Джеймс", "Мэджик Джонсон", "Коби Брайант", "Шакил О'Нил", "Ларри Бёрд", "Карим Абдул", "Тим Данкан", "Стивен Карри", "Лука Дончич", "Кайри Ирвинг", "Кевин Дюрант", "Джейсон Тэйтум", "Энтони Эдвардс", "Никола Йокич", "Джимми Батлер", "Кауай Леонард", "Пол Джордж", "Крис Пол"]

end_time_l = 5

my_teamArr_pos = [0] * 6
my_teamArr = []
id_team = 0
tm_card_x = 170
tm_card_y = 175
cur_add_id = 0

money = 1000

max_team_val = 6

#LOADING_SCREEN
loading_img = pygame.image.load('imges/loading_scr/loading_icn.png').convert_alpha()
loading_img0 = pygame.image.load('imges/loading_scr/loading_icn0.png').convert_alpha()
loading_img1 = pygame.image.load('imges/loading_scr/loading_icn1.png').convert_alpha()
loading_img2 = pygame.image.load('imges/loading_scr/loading_icn2.png').convert_alpha()
loading_img3 = pygame.image.load('imges/loading_scr/loading_icn3.png').convert_alpha()
loading_arr = [loading_img0,loading_img1,loading_img2,loading_img3,loading_img]
cur_load_id = 0

#START_LOADING_SCREEN
start_loading_img = pygame.image.load('imges/start_load/start_load_img.png').convert_alpha()
start_loading_img0 = pygame.image.load('imges/start_load/start_load_img0.png').convert_alpha()
start_loading_img1 = pygame.image.load('imges/start_load/start_load_img1.png').convert_alpha()
start_loading_img2 = pygame.image.load('imges/start_load/start_load_img2.png').convert_alpha()
start_loading_img3 = pygame.image.load('imges/start_load/start_load_img3.png').convert_alpha()
start_loading_img4 = pygame.image.load('imges/start_load/start_load_img4.png').convert_alpha()
start_loading_img5 = pygame.image.load('imges/start_load/start_load_img5.png').convert_alpha()
start_loading_arr = [start_loading_img0,start_loading_img1,start_loading_img2,start_loading_img3,start_loading_img4,start_loading_img5,start_loading_img]
cur_start_load_id = 0


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
erorFont = pygame.font.Font('fonts/ShantellSans-VariableFont_BNCE,INFM,SPAC,wght.ttf', 28)

#DRAFT MENU
square_mon = pygame.Surface((170, 70))
square_mon.fill((210, 143, 82))

my_team_text = mainBaldFont.render("Your Team: ", True, (46, 46, 48))
draft_text = mainBaldFont.render("Draft: ", True, (46, 46, 48))

#ERORS
my_team_text_fault_max_1 = erorFont.render("В команде не хватает места", True, (128, 0, 0))
my_team_text_fault_max_2 = erorFont.render("Максимальный размер команды: " + str(max_team_val), True, (128, 0, 0))

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

        return False

#EFFECTS
    #BLUR
# def blur_region(region, amount):
#     SCRRR = pygame.transform.box_blur((100,100,300,300), amount)
#     screen.blit(SCRRR, (100,100,300,300))

    #BLACKED_SCREEN
blacked_screen_img = pygame.image.load('imges/effects/blacked_screen(1200_950).png').convert_alpha()
ef_blacked_screen_check = False


#SOUND
tr1 = pygame.mixer.Sound('sounds/main_theme/track2(get_jiggy).mp3')
tr2 = pygame.mixer.Sound('sounds/main_theme/track1(where_is_my_head_at).mp3')
tr3 = pygame.mixer.Sound('sounds/main_theme/track3(drain_you).mp3')
tr4 = pygame.mixer.Sound('sounds/main_theme/track4(not_worth_it).mp3')
tr5 = pygame.mixer.Sound('sounds/main_theme/track5(anora).mp3')
tr6 = pygame.mixer.Sound('sounds/main_theme/track6(obsessed_with_you).mp3')
tr7 = pygame.mixer.Sound('sounds/main_theme/track7(bugs&humans).mp3')
tr8 = pygame.mixer.Sound('sounds/main_theme/track8(everybody_talks).mp3')
tr9 = pygame.mixer.Sound('sounds/main_theme/track9(memories).mp3')


main_tracks_arr = [tr1,tr2,tr3,tr4,tr5, tr6, tr7, tr8, tr9]
cur_track = random.randint(0, len(main_tracks_arr)-1)
print("cur_track: " + str(cur_track))

vol_music = 0.1
prev_vol_music = 0.1
mute_check = False

#MAIN REALIZATION
music_cheked = False
running = True
click_check = False
delay_gm_2_check = True
check_window_gm_2 = False
check_start_load_gm_not1 = True
er_maxVal_check = False

while running:
    for jj in main_tracks_arr:
        jj.set_volume(vol_music)
    if game_status == -1:
        if check_start_load_gm_not1:
            start_time_load_st = time.time()
            check_start_load_gm_not1 = False

        screen.blit(start_loading_arr[cur_start_load_id], (10, 200))

        current_time_load_st = float(time.time() - start_time_load_st)

        if 0.2 < current_time_load_st < 0.5:
            cur_start_load_id = 1
        elif 0.5 < current_time_load_st < 0.8:
            cur_start_load_id = 2
        elif 0.8 < current_time_load_st < 1.1:
            cur_start_load_id = 3
        elif 1.1 < current_time_load_st < 1.4:
            cur_start_load_id = 4
        elif 1.4 < current_time_load_st < 1.7:
            cur_start_load_id = 5
        elif 1.7 < current_time_load_st < 5.2:
            cur_start_load_id = 6
        if 5.2 < current_time_load_st < 5.5:
            cur_start_load_id = 5
        elif 5.5 < current_time_load_st < 5.8:
            cur_start_load_id = 4
        elif 5.8 < current_time_load_st < 6.1:
            cur_start_load_id = 3
        elif 6.1 < current_time_load_st < 6.4:
            cur_start_load_id = 2
        elif 6.4 < current_time_load_st < 6.7:
            cur_start_load_id = 1
        elif 6.7 < current_time_load_st < 7.0:
            cur_start_load_id = 0
        elif current_time_load_st > 7.5:
            game_status = 1

    elif game_status == 0:
        screen.fill((247, 204, 161))

        screen.blit(menu_logo, (150, 100))
        screen.blit(loading_arr[cur_load_id], (275, 500))
        if delay_gm_2_check:
            start_time_l = time.time()
            delay_gm_2_check = False

        current_time_l = int(time.time()-start_time_l)
        if current_time_l == 1:
            cur_load_id = 1
        elif current_time_l == 2:
            cur_load_id = 2
        elif current_time_l == 3:
            cur_load_id = 3
        elif current_time_l == 4:
            cur_load_id = 4

        if current_time_l is end_time_l:
            main_tracks_arr[cur_track].stop()
            cur_track +=1
            if cur_track == len(main_tracks_arr):
                cur_track = 0
            music_cheked = False
            game_status = 2

    elif game_status == 1:
        if not music_cheked:
            main_tracks_arr[cur_track].play()
            music_cheked = True
        screen.fill((210, 143, 82))

        screen.blit(menu_logo, (150, 100))
        screen.blit(start_button_img, start_button_rect)


        if start_button_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            game_status = 0
    elif game_status == 2:
        moneyOUT = str(str(money) + ' $')
        money_text = valFont.render(moneyOUT, True, (46, 46, 48))
        if not check_window_gm_2:
            pygame.display.set_mode((1200, 950))
            check_window_gm_2 = True
        if not music_cheked:
            main_tracks_arr[cur_track].play()
            music_cheked = True
        screen.fill((147, 101, 59))

        #screen.blit(square_mon, (730,0))
        screen.blit(money_text, (1040, 0))
        screen.blit(my_team_text, (510, 120))
        screen.blit(draft_text, (560, 380))

        if er_maxVal_check:
            screen.blit(my_team_text_fault_max_1, (420, 10))
            screen.blit(my_team_text_fault_max_2, (370, 40))

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


        if ef_blacked_screen_check:
            screen.blit(blacked_screen_img, (0,0))

        if pygame.mouse.get_pressed()[0]:
            for (i,el) in enumerate(draft_teamArr):
                if el.get('rect_colider').collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                    if not click_check:
                        er_maxVal_check = False
                        if (money - el.get('prise'))>=0:
                            if add_to_my_team(el, el.get('rect'), el.get('x'), el.get('y'), el.get('rect_colider'), el.get('id')):
                                draft_teamArr.pop(i)
                                money -= el.get('prise')
                            else:
                                print("В команде нет места")
                                er_maxVal_check = True

                        else:
                            print("У вас не хватает денег!")

                        click_check = True
            for (i,el) in enumerate(my_teamArr):
                if el.get('rect_colider').collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                    if not click_check:
                        er_maxVal_check = False
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
        if event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
            main_tracks_arr[cur_track].stop()
            cur_track+=1
            if cur_track == len(main_tracks_arr):
                cur_track = 0
            main_tracks_arr[cur_track].play()
        if event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
            main_tracks_arr[cur_track].stop()
            cur_track -= 1
            if cur_track < 0:
                cur_track = len(main_tracks_arr)-1
            main_tracks_arr[cur_track].play()
        if event.type == pygame.KEYUP and event.key == pygame.K_UP:
            vol_music += 0.05
        if event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
            vol_music -= 0.05
        if event.type == pygame.KEYUP and event.key == pygame.K_m:
            if not mute_check:
                prev_vol_music = vol_music
                vol_music = 0
                mute_check = True
            else:
                vol_music = prev_vol_music
                mute_check = False
        if event.type == pygame.KEYUP and event.key == pygame.K_b:
             ef_blacked_screen_check = True
        if event.type == pygame.KEYUP and event.key == pygame.K_n:
             ef_blacked_screen_check = False