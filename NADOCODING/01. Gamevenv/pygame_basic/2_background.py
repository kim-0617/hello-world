import pygame
from pygame.constants import SRCCOLORKEY

pygame.init() # 반드시 초기화 필요

# 화면 크기 설정
screen_width = 480 # 가로
screen_height = 640 # 세로
screen = pygame.display.set_mode((screen_width,screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game") # 게임이름

# 배경이미지 불러오기
background = pygame.image.load("./gamevenv/pygame_basic/background.png")

# 이벤트 루프
runnig = True # 게임이 진행중인가?
while runnig:
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생할 때
            runnig = False # 게임이 진행중이 아님
    #screen.fill((0,0,255)) # 이것도 배경이미지 채우기
    screen.blit(background, (0,0)) # 배경 그리기
    pygame.display.update() # 게임화면을 매프레임마다 그리기

# pygame 종료처리
pygame.quit()