import os
from traceback import print_tb

# 파일 목록 가지고 오기
dir_path = 'D:\download\바탕화면\끝내주는 바탕화면\Ayami'
file_list = os.listdir(dir_path)

# print(file_list)

# 파일 이름 변경
# 새이름 + 규칙 + 번호 + 확장자
str_name = 'pie' # 새이름
str_prefix = '-' # 규칙
num = 0 # 번호

for old_name in file_list:
    index = old_name.find('.')
    file_name = old_name[:index]
    file_extension = old_name[index:]
    # print(f'filename : {file_name}')
    # print(f'fileextension : {file_extension}')
    # print('-'*50)

    num += 1
    new_name = str_name + str_prefix + str(num)+ file_extension
    # print(new_name)

    os.rename(dir_path + '/' + old_name, dir_path + '/' +new_name)