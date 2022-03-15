import pygame

def display_start_screen():
    pygame.draw.circle(screen, WHITE, start_button.center, 60, 5)
    # 흰색 동그라미, 중심좌표는 startbutton, 반지름 60, 선두께는 5

def display_game_screen():
    print("Game start")

# pos에 해당하는 버튼 확인
def check_button(pos):
    global start
    if start_button.collidepoint(pos):
        start = True

pygame.init() # 반드시 초기화 필요

# 화면 크기 설정
screen_width = 1280 # 가로
screen_height = 720 # 세로
screen = pygame.display.set_mode((screen_width,screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Memory Game") # 게임이름

# 시작 버튼
start_button = pygame.Rect(0, 0, 120, 120)
start_button.center = (120, screen_height - 120)

# 색깔
BLACK = (0,0,0) # RGB
WHITE = (255,255,255)

# 게임 시작 여부 판단
start = False

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