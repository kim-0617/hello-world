from socket import timeout
import pyautogui
import time
import sys

# file_menu = pyautogui.locateOnScreen("file_menu.png")
# print(file_menu)

# pyautogui.click(file_menu)

def my_click(img_file, timeout=10):
    target = find_target(img_file,timeout)
    if target:
        pyautogui.click(target)
    else:
        print(f"[Timeout {timeout}s Target not fount {img_file}]")
        sys.exit()

def find_target(img_file, timeout=10):
    start = time.time()
    target = None
    while target is None:
        target = pyautogui.locateOnScreen(img_file)
        end = time.time()
        if end - start > timeout:
            break
    return target

my_click("file_menu.png",5)