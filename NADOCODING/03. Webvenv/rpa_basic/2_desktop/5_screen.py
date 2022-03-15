import pyautogui

# 스크린샷 찍기
# img = pyautogui.screenshot()
# img.save("ss.png")

# pyautogui.mouseInfo()
# 1011,12 192,192,192 #C0C0C0

pixel = pyautogui.pixel(1011,12)
print(pixel)

print(pyautogui.pixelMatchesColor(1011,12,(191,191,191)))