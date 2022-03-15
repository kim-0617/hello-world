import pygame
from pygame.constants import SRCCOLORKEY
from random import *
##################################################################
# 기본 초기화 (반드시 해야 하는 것들)
pygame.init() # 반드시 초기화 필요

# 화면 크기 설정
screen_width = 480 # 가로
screen_height = 640 # 세로
screen = pygame.display.set_mode((screen_width,screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game") # 게임이름

# FPS
clock = pygame.time.Clock()
##################################################################

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 폰트 등)
background = pygame.image.load("./gamevenv/pygame_basic/background.png")

character = pygame.image.load("./Gamevenv/pygame_basic/character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height

# 이동할 좌표
to_x = 0
to_y = 0

# 이동 속도
charater_speed = 0.6

enemy_images = [
    pygame.image.load("./Gamevenv/pygame_basic/enemy.png"),
    pygame.image.load("./Gamevenv/pygame_basic/enemy.png"),
    pygame.image.load("./Gamevenv/pygame_basic/enemy.png"),
    pygame.image.load("./Gamevenv/pygame_basic/enemy.png"),
    pygame.image.load("./Gamevenv/pygame_basic/enemy.png"),
    pygame.image.load("./Gamevenv/pygame_basic/enemy.png"),
    pygame.image.load("./Gamevenv/pygame_basic/enemy.png")
]
enemys = [] # 12, 7개
center = 0

for i in range(7):
    enemys.append({
    "pos_x" : center,
    "pos_y" : 0, 
    "img_idx" :0,
    "to_y" : 6, 
    "init_spd_y": 6
    })
    center += 82
enemys_copy = enemys.copy()

weapon = pygame.image.load("./Gamevenv/pygame_basic/weapon.png")
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]

weapons = []
weapon_speed = 10

# 사라질 무기, 공 정보 저장 변수
weapon_to_remove = -1
enemy_to_remove = -1

runnig = True 
while runnig:
    dt = clock.tick(30)
    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            runnig = False

    if event.type == pygame.KEYDOWN: # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT: # 키가 왼쪽으로
                to_x -= charater_speed
            elif event.key == pygame.K_RIGHT:
                to_x += charater_speed
            elif event.key == pygame.K_UP:
                weapon_x_pos = character_x_pos + (character_width/2) - (weapon_width/2)
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos, weapon_x_pos])
                

    if event.type == pygame.KEYUP: # 키를 떼면 멈춤
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            to_x = 0
    
    # 3. 게임 캐릭터 위치 정의
    character_x_pos += to_x * dt # 프레임 값에 따른 이동속도 보정을 위해서 

    # 가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

        # 무기 위치 조정
    weapons = [[w[0],w[1] - weapon_speed] for w in weapons] # 무기 위치를 위로 올린다

    # 천장에 닿은 무기 없애기
    weapons = [[w[0], w[1]] for w in weapons if w[1] > 0]

    for enemy_idx, enemy_val in enumerate(enemys):
        enemy_pos_x = enemy_val["pos_x"]
        enemy_pos_y = enemy_val["pos_y"]
        enemy_img_idx = enemy_val["img_idx"]

        enemy_size = enemy_images[enemy_img_idx].get_rect().size
        enemy_width = enemy_size[0]
        enemy_height = enemy_size[1]
        enemy_val["pos_y"] += enemy_val["to_y"]
        if enemy_pos_y > screen_height - enemy_height:
            enemy_val["pos_y"] = 0

    # 4. 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    # 충돌체크
    for enemy_idx, enemy_val in enumerate(enemys):
        enemy_pos_x = enemy_val["pos_x"]
        enemy_pos_y = enemy_val["pos_y"]
        enemy_img_idx = enemy_val["img_idx"]
        enemy_rect = enemy_images[enemy_img_idx].get_rect()
        enemy_rect.left = enemy_pos_x
        enemy_rect.top = enemy_pos_y

        if character_rect.colliderect(enemy_rect):
            # runnig = False
            break

        for weapon_idx, weapon_val in enumerate(weapons):
            weapon_x_pos = weapon_val[0]
            weapon_y_pos = weapon_val[1]

            # 무기 rect 정보 업데이트
            weapon_rect = weapon.get_rect()
            weapon_rect.left = weapon_x_pos
            weapon_rect.top = weapon_y_pos

            # 충돌 체크
            if weapon_rect.colliderect(enemy_rect):
                weapon_to_remove = weapon_idx
                enemy_to_remove = enemy_idx
                enemy_val["pos_y"] = 0
                break

    if enemy_to_remove > -1:
        a = enemys[enemy_to_remove]
        del enemys[enemy_to_remove]
        enemy_to_remove = -1
    if weapon_to_remove > -1:
        del weapons[weapon_to_remove]
        weapon_to_remove = -1

    # 5. 화면에 그리기
    screen.blit(background, (0,0)) # 배경 그리기
    screen.blit(character, (character_x_pos,character_y_pos))
    for idx, val in enumerate(enemys):
        enemy_pos_x = val["pos_x"]
        enemy_pos_y = val["pos_y"]
        enemy_img_idx = val["img_idx"]
        if len(enemys) < 7 and enemy_pos_y > screen_height - enemy_height:
            screen.blit(enemy_images[enemy_img_idx], (enemy_pos_x, enemy_pos_y))
            enemys.clear()
            enemys = enemys_copy.copy()

        else:
            screen.blit(enemy_images[enemy_img_idx], (enemy_pos_x,enemy_pos_y))


    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))

    pygame.display.update() # 게임화면을 매프레임마다 그리기


# pygame 종료처리
pygame.quit()