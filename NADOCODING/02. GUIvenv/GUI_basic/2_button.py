from cgitb import text
from math import fabs
from tkinter import *

root = Tk()
root.title("Nado GUI")

btn1 = Button(root, text="버튼1")
btn1.pack()

btn2 = Button(root, padx=5, pady=10, text="버튼2")
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text="버튼3") # pad 속성을 쓰면 글자를 기준으로 여백을 확보하는 느낌
btn3.pack()

btn4 = Button(root, width=10, height=3, text="버튼4") # width height를 주면 고정된크기
btn4.pack()

btn5 = Button(root, fg="red", bg="yellow" ,text="버튼5") # fg를 글자색상 / bg는 배경칠하기
btn5.pack()


photo = PhotoImage(file='./GUIvenv/GUI_basic/img.png')
btn6 = Button(root, image=photo)
btn6.pack()

def btncmd():
    print("버튼이 클릭되었어요")

btn7 = Button(root, text="동작하는 버튼", command=btncmd)
btn7.pack()

root.mainloop()