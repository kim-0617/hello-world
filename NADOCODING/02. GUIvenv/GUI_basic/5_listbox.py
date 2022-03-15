from math import fabs
from subprocess import list2cmdline
from tkinter import *
from typing import List

root = Tk()
root.title("Nado GUI")
root.geometry("640x480+300+100") # 가로 x 세로 + x좌표 + y좌표

# 여러가지 리스트를 목록으로 관리하는 위젯
listbox = Listbox(root, selectmode="extended", height=0) # height는 보여줄 리스트의 개수 3이면 3개만 보여준다
listbox.insert(0,"사과")
listbox.insert(1,"딸기")
listbox.insert(2,"바나나")
listbox.insert(END,"수박")
listbox.insert(END,"포도")
listbox.pack()

def btncmd():
    # listbox.delete(END) # 맨 뒤에 항목 삭제

    # print("리스트에는", listbox.size(), "개가 있어요") # 개수확인

    # print("첫 번째부터 세 번째까지의 항목: ", listbox.get(0,2)) # 0,1,2 항목 출력
    
    print("선택된 항목: ", listbox.curselection()) # 선택된 항목 확인(index 반환)


btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()