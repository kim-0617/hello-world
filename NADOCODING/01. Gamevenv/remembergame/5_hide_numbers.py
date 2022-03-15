from ast import PyCF_ALLOW_TOP_LEVEL_AWAIT
from modulefinder import packagePathMap
from tkinter import CENTER, Button
import pygame
from random import randint, random

# 레벨에 맞게 설정
def setup(level):
    global display_time
    # 얼마동안 숫자를 보여줄지
    display_time = 5 - (level // 3)
    display_time = max(display_time, 1)

    # 얼마나 많은 숫자를 보여줄 것인가?
    number_count = (level // 3) + 5
    number_count = min(number_count, 20)

    # 실제 화면에 grid 형태로 숫자를 랜덤으로 배치
    shuffle_grid(number_count)

# 숫자 섞기(가장 중요)
def shuffle_grid(number_count):
    rows = 5
    columns = 9

    cell_size = 130 # 각 Grid cell 별 가로,세로 크기
    button_size = 110 # 버튼 크기
    screen_left_margin = 55 # 스크린 왼쪽 여백
    screen_top_margin = 20 # 스크린 위쪽 여백

    grid = [[0 for col in range(columns)] for row in range(rows)]

    number = 1
    while number <= number_count:
        row_idx = randint(0,rows-1)
        col_idx = randint(0,columns-1)

        if grid[row_idx][col_idx] == 0:
            grid[row_idx][col_idx] = number
            number += 1

            # 현재 grid cell 위치 기준으로 x,y 위치를 구함
            center_x = screen_left_margin + (col_idx * cell_size) + (cell_size / 2)
            center_y = screen_top_margin + (row_idx * cell_size) + (cell_size / 2)

            # 숫자 버튼 만들기
            button = pygame.Rect(0, 0, button_size, button_size)
            button.center = (center_x, center_y)

            number_buttons.append(button)

    print(grid)

def display_start_screen():
    pygame.draw.circle(screen, WHITE, start_button.center, 60, 5)
    # 흰색 동그라미, 중심좌표는 startbutton, 반지름 60, 선두께는 5

# 게임 화면 보여주기
def display_game_screen():
    global hidden
    if not hidden:
        elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 # ms -> sec
        if elapsed_time > display_time:
            hidden = True

    for idx, rect in enumerate(number_buttons, start = 1):
        if hidden: # 숨김처리
            pygame.draw.rect(screen, WHITE, rect)
        else:
            # 실제 숫자 텍스트 그리기
            cell_text = game_font.render(str(idx), True, WHITE)
            text_rect = cell_text.get_rect(center=rect.center)
            screen.blit(cell_text, text_rect)


# pos에 해당하는 버튼 확인
def check_button(pos):
    global start
    global start_ticks
    # 게임이 시작했으면?
    if start:
        check_number_buttons(pos)
    elif start_button.collidepoint(pos):
        start = True
        start_ticks = pygame.time.get_ticks() # 타이머 시작(현재 시간을 저장)

# 사용자가 클릭한 버튼이 버튼리스트인지, 첫번째 버튼인지
def check_number_buttons(pos):
    global hidden
    for button in number_buttons:
        if button.collidepoint(pos):
            if button == number_buttons[0]:
                print("correct")
                del number_buttons[0]
                if not hidden:
                    hidden = True
            else:
                print("Wrong")
            break

pygame.init() # 반드시 초기화 필요

# 화면 크기 설정
screen_width = 1280 # 가로
screen_height = 720 # 세로
screen = pygame.display.set_mode((screen_width,screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Memory Game") # 게임이름

# 폰트 설정
game_font = pygame.font.Font(None, 120)

# 시작 버튼
start_button = pygame.Rect(0, 0, 120, 120)
start_button.center = (120, screen_height - 120)

# 색깔
BLACK = (0,0,0) # RGB
WHITE = (255,255,255)
GRAY = (50,50,50)

# 플레이어들이 눌러야 하는 버튼의 위치정보 관리
number_buttons = []

# 숫자를 보여주는 시간
display_time = None
# 시간계산
start_ticks = None

# 게임 시작 여부 판단
start = False
# 숫자 숨김 여부 (사용자가 1을 클릭했거나, 보여주는 시간을 초과했을 때)
hidden = False

# 게임 시작 직전에 게임 설정 함수 실행
setup(1)

# 게임 루프
runnig = True # 게임이 진행중인가?
while runnig:
    click_pos = None

    # 이벤트 루프
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생할 때
            runnig = False # 게임이 진행중이 아님
        elif event.type == pygame.MOUSEBUTTONUP:
            click_pos = pygame.mouse.get_pos()

    # 화면 전체를 까맣게 칠함
    screen.fill(BLACK)

    if start: 
        # 게임 화면 표시
        display_game_screen()
    else:
        # 시작 화면 표시
        display_start_screen()

    # 사용자가 어딘가 클릭을 하면
    if click_pos:
        check_button(click_pos)

    # 화면 업데이트
    pygame.display.update()

# pygame 종료처리
pygame.quit()