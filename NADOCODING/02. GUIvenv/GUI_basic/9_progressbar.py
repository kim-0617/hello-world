from cProfile import label
from cgi import test
import imp
from math import fabs
from statistics import mode
from subprocess import list2cmdline
from tkinter import *
from typing import List
import tkinter.ttk as ttk
import time

root = Tk()
root.title("Nado GUI")
root.geometry("640x480+300+100") # 가로 x 세로 + x좌표 + y좌표

# # progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate")
# progressbar = ttk.Progressbar(root, maximum=100, mode="determinate")
# progressbar.start(10) # 10ms 마다 움직임
# progressbar.pack()

# def btncmd():
#     progressbar.stop() # 작동중지

# btn = Button(root, text="중지", command=btncmd)
# btn.pack()

p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()

def btncmd2():
    for i in range(1,101):
        time.sleep(0.01)
        p_var2.set(i) # bar의 값을 설정
        progressbar2.update() # 값이 차는게 보임
        print(p_var2.get())

btn = Button(root, text="시작", command=btncmd2)
btn.pack()

root.mainloop()