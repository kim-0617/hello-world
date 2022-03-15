import pyautogui
import pyperclip

pyautogui.hotkey("win","r")
pyautogui.write("mspaint")
pyautogui.hotkey("enter")

pyautogui.sleep(1)

w = pyautogui.getWindowsWithTitle("제목 없음 - 그림판")[0]
if w.isMaximized == False:
    w.maximize()

text_icon = pyautogui.locateOnScreen("text_icon.png")
pyautogui.click(text_icon)

pyautogui.moveTo(470,485)
pyautogui.click()

comment = pyperclip.copy("참 잘했어요")
pyautogui.hotkey('ctrl','v')

pyautogui.sleep(5)
w.close()
pyautogui.sleep(1)
pyautogui.hotkey('n')