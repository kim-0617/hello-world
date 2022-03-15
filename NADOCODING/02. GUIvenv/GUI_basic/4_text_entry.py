from math import fabs
from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480+800+300") # 가로 x 세로 + x좌표 + y좌표

# 텍스트는 여러줄을 입력받을 때
txt = Text(root, width=30, height=5)
txt.pack()
txt.insert(END, "글자를 입력하세요")

# 엔트리는 한줄에 걸쳐 입력받을 때
e = Entry(root, width=30)
e.pack()
e.insert(0, "한줄만 입력해요")

def btncmd():
    # 내용 출력
    print(txt.get("1.0",END)) # 1.0의 의미 : 1은 첫번째 줄에서, 0은 0번째 칼럼부터 ~~ 끝까지 가져와라 (END)
    print(e.get())

    # 내용 삭제
    txt.delete("1.0", END)
    e.delete(0,END)

btn = Button(root, text="click", command=btncmd)
btn.pack()

root.mainloop()