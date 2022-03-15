# # glob : 경로내의 폴더 / 파일 목록 조회
# import glob
# print(glob.glob("./basic/*.py"))

# # os : 운영체제에서 제공하는 기본 기능
# import os
# print(os.getcwd())
# folder = "./basic/sample_dir"
# if os.path.exists(folder):
#     print("이미 존재하는 폴더입니다.")
# else:
#     os.makedirs(folder) # 폴더생성
#     print(folder,"폴더를 생성하였습니다.")

# # time : 시간관련 함수
# import time
# print(time.localtime())
# print(time.strftime("%Y-%m-%d %H:%m:%S"))
import datetime
print("오늘날짜는" ,datetime.date.today())
today = datetime.date.today()
td = datetime.timedelta(days=100)
print("우리가 만난지 100일은", today+td)