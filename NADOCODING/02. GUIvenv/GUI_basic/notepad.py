import os
from tkinter import *

root = Tk()
root.title("제목 없음 - Windows 메모장")
root.geometry("640x480+800+300") # 가로 x 세로 + x좌표 + y좌표

def save_file():
    print('save')
    with open("./GUIvenv/GUI_basic/mynote.txt","w",encoding='utf-8') as f:
            f.write(txt.get("1.0",END))

def open_file():
    print('open')
    if os.path.isfile("./GUIvenv/GUI_basic/mynote.txt"):
        with open("./GUIvenv/GUI_basic/mynote.txt","r",encoding='utf-8') as f:
            txt.delete("1.0",END)
            txt.insert(END,f.read())

menu = Menu(root)

# File 메뉴
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="열기", command=open_file)
menu_file.add_separator() # 구분자
menu_file.add_command(label="저장", command=save_file)
menu_file.add_separator() # 구분자
menu_file.add_command(label="끝내기", command=root.quit)
menu.add_cascade(label="파일", menu=menu_file) # File 메뉴 항목 추가하기

# 그 외 메뉴
menu.add_cascade(label="편집")
menu.add_cascade(label="서식")
menu.add_cascade(label="보기")
menu.add_cascade(label="도움말")

# 스크롤 바
scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y") # fill은 y 방향으로 쭉 늘어남

# 본문
txt = Text(root, yscrollcommand=scrollbar.set)
txt.pack(side="left", fill="both", expand=True)

scrollbar.config(command=txt.yview)

root.config(menu=menu)
root.mainloop()