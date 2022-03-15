from cgitb import text
from math import fabs
from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("680x480+800+300")

label1 = Label(root, text="안녕하세요")
label1.pack()

photo = PhotoImage(file='./GUIvenv/GUI_basic/img.png')
label2 = Label(root, image=photo)
label2.pack()


def change():
    label1.config(text="또만나요")
    # 함수가 끝나면 가비지콜렉터가 필요없다고 판단하여 없애버리기 때문에
    # 사진 값을 바꾸려면 전역변수로 만들어 줘야 함
    global photo2
    photo2 = PhotoImage(file='./GUIvenv/GUI_basic/img2.png')
    label2.config(image=photo2)

btn = Button(root, text="클릭", command=change)
btn.pack()

root.mainloop()