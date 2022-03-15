import pyautogui
# pyautogui.FAILSAFE = False # 멈추고 싶지 않으면 이 값을 설정하면 된다
# pyautogui.PAUSE = 1 # 함수마다 1초씩 대기하게 한다.
# pyautogui.mouseInfo() # 마우스 정보

# 자동화 프로그램을 멈추고 싶으면 마우스포인터를 네곳 귀퉁이에 옮긴다
for i in range(5):
    pyautogui.move(100,100)
    pyautogui.sleep(1)

