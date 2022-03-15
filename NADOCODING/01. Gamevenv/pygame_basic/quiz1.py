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

enemy = pygame.image.load("./Gamevenv/pygame_basic/enemy.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = randint(0,screen_width - enemy_width)
enemy_y_pos = 0

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
    if event.type == pygame.KEYUP: # 키를 떼면 멈춤
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            to_x = 0
    
    # 3. 게임 캐릭터 위치 정의
    character_x_pos += to_x * dt # 프레임 값에 따른 이동속도 보정을 위해서 
    character_y_pos += to_y * dt

    # 가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 4. 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # 충돌체크
    if character_rect.colliderect(enemy_rect):
        print("충돌했어요")
        runnig = False
    else:
        enemy_y_pos += 10
    
    if enemy_y_pos == screen_height:
        enemy_y_pos = 0 
        enemy_x_pos = randint(0,screen_width - enemy_width)

    # 5. 화면에 그리기
    screen.blit(background, (0,0)) # 배경 그리기
    screen.blit(character, (character_x_pos,character_y_pos)) # 캐리거 그리기
    screen.blit(enemy, (enemy_x_pos,enemy_y_pos)) # 적 그리기

    pygame.display.update() # 게임화면을 매프레임마다 그리기


# pygame 종료처리
pygame.quit()