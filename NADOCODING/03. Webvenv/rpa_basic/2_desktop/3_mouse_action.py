from pydoc import cli
import pyautogui

pyautogui.sleep(2)
print(pyautogui.position()) # 1016,16

# pyautogui.click(1016,16, duration=1)
# pyautogui.mouseDown()
# pyautogui.mouseUp()  # 위 동작과 같음

# pyautogui.click(clicks=1000) # 현재마우스 위치에서 천번 클릭

# 드래그 & 드랍
# pyautogui.moveTo(100,200)
# pyautogui.mouseDown()
# pyautogui.moveTo(300,400)
# pyautogui.mouseUp()

# 우클릭
# pyautogui.rightClick()
# 휠클릭
# pyautogui.middleClick()

# pyautogui.moveTo(816,346)
# pyautogui.dragTo(1000,600,duration=1)

pyautogui.scroll(1000) # 위 방향으로 1000만큼 스크롤 - 일경우 아래로