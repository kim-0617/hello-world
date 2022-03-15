import pyautogui

w = pyautogui.getWindowsWithTitle("제목 없음")[0]
w.activate()

# pyautogui.write("12345")
# pyautogui.write("\nNadoCoding", interval=0.25)
# pyautogui.write("\n나도코딩", interval=0.25) # 한글은 안적힘

# # left는 왼쪽방향키 right는 오른쪽방향키 enter는 엔터
# pyautogui.write(["t", "e", "s", "t", "left", "left", "right", "l", "a", "enter"],interval=0.25)

# # 특수문자
# # shift + 4 = $
# pyautogui.keyDown("shift") # 누르기
# pyautogui.press("4")
# pyautogui.keyUp("shift") # 떼기

# # 조합키 (Hot key)
# pyautogui.keyDown("ctrl")
# pyautogui.keyDown("a")
# pyautogui.keyUp("a")
# pyautogui.keyUp("ctrl")

# 간편한 조합키
# pyautogui.hotkey("ctrl", "a")
# ctrl 누르고 > a 누르고 > a 떼고 > ctrl 떼고

# 한글입력
import pyperclip

pyperclip.copy("나도코딩") # 나도코딩글자를 클립보드에 저장
pyautogui.hotkey('ctrl', 'v') # 붙여넣기

# def my_write(text):
#     pyperclip.copy(text)
#     pyautogui.hotkey('ctrl', 'v')

# ctrl + alt + del : 자동화 프로그램 종료
