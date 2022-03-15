# 파일 기본
import os
from traceback import print_tb
from unittest import result

# print(os.getcwd()) # current working directory
# os.chdir("./Webvenv/rpa_basic") # 적어둔 공간으로 작업공간 이동
# print(os.getcwd())
# os.chdir("../..")
# print(os.getcwd())

# os.chdir("c:/")
# print(os.getcwd())

# 파일 경로
# print(os.path.join(os.getcwd(), "my_file.txt")) # 절대 경로 생성 

# 파일 경로에서 폴더 정보 가져오기
# print(os.path.dirname(r'C:\NADOCODING')) # NADOCODING의 부모폴더

# # 파일 정보 가져오기
# import time
# import datetime


# # 파일의 생성 날짜
# ctime = os.path.getctime("file_menu.png")
# print(ctime)
# print(datetime.datetime.fromtimestamp(ctime).strftime('%Y%m%d %H:%M:%S'))

# # 파일의 수정 날짜
# mtime = os.path.getmtime("file_menu.png")
# print(mtime)
# print(datetime.datetime.fromtimestamp(mtime).strftime('%Y%m%d %H:%M:%S'))

# # 파일의 마지막 접근날짜
# atime = os.path.getatime("file_menu.png")
# print(datetime.datetime.fromtimestamp(atime).strftime('%Y%m%d %H:%M:%S'))

# # 파일 크기 / 바이트 단위
# print(os.path.getsize("file_menu.png"))

# # 파일 목록 가져오기
# print(os.listdir("./Webvenv/rpa_basic"))

# 하위 폴더 모두 포함해서 가져오기
# result = os.walk("./Webvenv/rpa_basic")

# for root, dirs, files in result:
#     print(root, dirs, files)

# # 폴더 내에서 특정 파일들을 찾으려면?
# name = "11_file_system.py"
# result = []

# for root, dirs, files in os.walk(os.getcwd()):
#     if name in files:
#         result.append(os.path.join(root,name))
# print(result)

# # 폴더 내에서 특정 패턴을 가진 파일들 찾으려면?
# import fnmatch
# pattern = "file*.png"
# result = []

# for root, dirs, files in os.walk("."):
#     for name in files:
#         if fnmatch.fnmatch(name,pattern):
#             result.append(os.path.join(root,name))
# print(result)

# # 주어진 경로가 파일인지? 폴더인지?
# print(os.path.isdir("./Webvenv/rpa_basic"))
# print(os.path.isfile("./Webvenv/rpa_basic/2_desktop/11_file_system.py"))

# # 주어진 경로가 존재하는지?
# if os.path.exists("./Webvenv/rpa_basic"):
#     print("파일 또는 폴더가 존재합니다.")
# else:
#     print("존재하지 않습니다.")

# # 파일 만들기
# open("new_file.txt","a").close() # 빈 파일 생성

# # 파일명 변경하기
# os.rename("new_file.txt", "new_file_rename.txt")

# # 파일 삭제하기
# os.remove("new_file_rename.txt")

# # 폴더만들기 / 있으면 못만듦
# os.mkdir("./Webvenv/rpa_basic/new_folder")

# # 여러개 한꺼번에 만들기 / newfolder,a,b,c
# os.makedirs("./Webvenv/rpa_basic/new_folder/a/b/c")

# # 폴더명 바꾸기
# os.rename("원래이름", "바꿀이름")

# # 폴더지우기 
# os.rmdir("지울폴더이름")  # 빈껍데기 폴더만 삭제가능
import shutil # shell utilities
# shutil.rmtree("지울폴더이름") # 묻지도 따지지도 않고 삭제

# 파일 복사하기
# copy, copyfile : 메타정보를 복사하지 않는다
# copy2 : 메타정보를 복사한다.
# os.makedirs("test_folder")
# shutil.copy("file_menu.png","test_folder") # 원본경로 대상경로
# shutil.copy("file_menu.png","test_folder/copied_run_btn.png") # 원본경로 대상경로(변경된 파일명)
# shutil.copyfile("file_menu.png","test_folder/copied_run_btn2.png" ) # copyfile은 파일경로까지 다 적어줘야함
# shutil.copy2("file_menu.png","test_folder/copied_run_btn3.png")

# 폴더 복사
# shutil.copytree("test_folder","test2_folder") # 원폰폴더경로 대상폴더경로
# shutil.copytree("test_folder","test3_folder") # 원폰폴더경로 대상폴더경로

# 폴더 이동
# shutil.move("test_folder","test3_folder") # 옮겨질녀석 옮길위치
# shutil.move("test2_folder","test3_folder")
# shutil.move("test_folder","test_folder_rename") # 마치 폴더명을 변경한 것처럼
