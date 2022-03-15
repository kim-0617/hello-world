from cProfile import label
from cgi import test
from math import fabs
from subprocess import list2cmdline
from tkinter import *
from typing import List
import tkinter.ttk as ttk

root = Tk()
root.title("Nado GUI")
root.geometry("640x480+300+100") # 가로 x 세로 + x좌표 + y좌표

values = [str(i)+"일" for i in range(1,32)]
combobox = ttk.Combobox(root, height=5, values=values) # height는 최대 보여주는 목록이 5개이다.
combobox.set("카드 결제일")
combobox.pack()

readonly_combobox = ttk.Combobox(root, height=10, values=values, state="readonly")
readonly_combobox.current(0) # 0번째 인덱스 값 선택
readonly_combobox.pack()

def btncmd():
    print(combobox.get())
    print(readonly_combobox.get())

btn = Button(root, text="선택", command=btncmd)
btn.pack()

root.mainloop()