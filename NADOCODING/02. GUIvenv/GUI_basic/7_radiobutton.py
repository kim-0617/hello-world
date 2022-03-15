from cProfile import label
from cgi import test
from math import fabs
from subprocess import list2cmdline
from tkinter import *
from typing import List

root = Tk()
root.title("Nado GUI")
root.geometry("640x480+300+100") # 가로 x 세로 + x좌표 + y좌표

Label(root, text="메뉴를 선택하세요").pack()

burger_var = IntVar() # int형으로 값을 저장
btn_burget1 = Radiobutton(root, text="햄버거", value=1, variable=burger_var)
btn_burget2 = Radiobutton(root, text="치즈버거", value=2, variable=burger_var)
btn_burget2.select()
btn_burget3 = Radiobutton(root, text="치킨버거", value=3, variable=burger_var)

btn_burget1.pack()
btn_burget2.pack()
btn_burget3.pack()

Label(root, text="음료를 선택하세요").pack()

drink_var = StringVar()
btn_drink1 = Radiobutton(root, text="콜라", value="콜라", variable=drink_var)
btn_drink1.select()
btn_drink2 = Radiobutton(root, text="사이다", value="사이다", variable=drink_var)
btn_drink3 = Radiobutton(root, text="환타", value="환타", variable=drink_var)

btn_drink1.pack()
btn_drink2.pack()
btn_drink3.pack()

def btncmd():
    print(burger_var.get())
    print(drink_var.get())

btn = Button(root, text="주문", command=btncmd)
btn.pack()

root.mainloop()