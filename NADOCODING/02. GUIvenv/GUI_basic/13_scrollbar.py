from cmath import exp
from msilib.schema import ListBox
from os import set_inheritable
from select import select
from subprocess import list2cmdline
import tkinter.messagebox as msgbox
from tkinter import *
from typing import List

root = Tk()
root.title("Nado GUI")
root.geometry("640x480+800+300") # 가로 x 세로 + x좌표 + y좌표

frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y") # fill은 y 방향으로 쭉 늘어남

# set이 없으면 스크롤을 내려도 다시 올라옴
listbox = Listbox(frame, selectmode="extended", height=10, yscrollcommand=scrollbar.set)
for i in range(1,32):
    listbox.insert(END,str(i)+"일")
listbox.pack(side="left")

scrollbar.config(command=listbox.yview)

root.mainloop()