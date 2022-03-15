import pygame
from pygame.constants import SRCCOLORKEY

pygame.init() # 반드시 초기화 필요

# 화면 크기 설정
screen_width = 480 # 가로
screen_height = 640 # 세로
screen = pygame.display.set_mode((screen_width,screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game") # 게임이름

# FPS
clock = pygame.time.Clock()

# 배경이미지 불러오기
background = pygame.image.load("./gamevenv/pygame_basic/background.png")

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load("./gamevenv/pygame_basic/charater.png")
character_size = character.get_rect().size # 이미지의 크기를 구해옴
character_width = character_size[0] # 캐릭터의 가로크기
character_height = character_size[1] # 캐릭터의 세로크기
character_x_pos = (screen_width / 2) - (character_width / 2) # 화면 가로의 절반 크기에 해당하는 고셍 위치
character_y_pos = screen_height - character_height # 화면 세로 크기 가장 아래에 위치

# 이동할 좌표
to_x = 0
to_y = 0

# 이동 속도
charater_speed = 0.6

# 적 enemy 캐릭터
enemy = pygame.image.load("./gamevenv/pygame_basic/enemy.png")
enemy_size = enemy.get_rect().size # 이미지의 크기를 구해옴
enemy_width = enemy_size[0] # 캐릭터의 가로크기
enemy_height = enemy_size[1] # 캐릭터의 세로크기
enemy_x_pos = (screen_width / 2) - (enemy_width / 2) # 화면 가로의 절반 크기에 해당하는 고셍 위치
enemy_y_pos = (screen_height / 2) - (enemy_height / 2) # 화면 세로 크기

# 이벤트 루프
runnig = True # 게임이 진행중인가?
while runnig:
    dt = clock.tick(60) # 게임화면의 초당 프레임 수를 설정

    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생할 때
            runnig = False # 게임이 진행중이 아님
        
        if event.type == pygame.KEYDOWN: # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT: # 키가 왼쪽으로
                to_x -= charater_speed
            elif event.key == pygame.K_RIGHT:
                to_x += charater_speed
            elif event.key == pygame.K_UP:
                to_y -= charater_speed
            elif event.key == pygame.K_DOWN:
                to_y += charater_speed
        if event.type == pygame.KEYUP: # 키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
    character_x_pos += to_x * dt # 프레임 값에 따른 이동속도 보정을 위해서 
    character_y_pos += to_y * dt

    # 가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    
    # 세로 경계값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    # 충돌 처리
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

    screen.blit(background, (0,0)) # 배경 그리기
    screen.blit(character, (character_x_pos,character_y_pos)) # 캐리거 그리기
    screen.blit(enemy, (enemy_x_pos,enemy_y_pos)) # 적 그리기
    pygame.display.update() # 게임화면을 매프레임마다 그리기

# pygame 종료처리
pygame.quit()