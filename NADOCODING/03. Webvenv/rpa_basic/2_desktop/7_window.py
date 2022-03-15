from winreg import REG_OPTION_BACKUP_RESTORE
import pyautogui

# fw = pyautogui.getActiveWindow() # 현재 활성화된 창
# print(fw.title)
# print(fw.size)
# print(fw.left, fw.top, fw.right, fw.bottom)

# pyautogui.click(fw.left+20, fw.top+20)

# for w in pyautogui.getAllWindows():
#     print(w) # 모든 윈도우 가져오기

w = pyautogui.getWindowsWithTitle("제목 없음")[0]
print(w)

if w.isActive == False:
    w.activate() # 맨 앞으로 가져옴

if w.isMaximized == False:
    w.maximize() # 최대화 시킴

w.restore() # 원상복구

w.close() # 닫기