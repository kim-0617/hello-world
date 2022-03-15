from cgi import print_directory
import re
from traceback import print_tb

p = re.compile("ca.e")

def print_match(m):
    if m:
        print(m.group()) # 일치하는 문자열 반환
        print(m.string) # 입력받은 문자열
        print(m.start()) # 일치하는 문자열의 시작 index
        print(m.end()) # 일치하는 문자열의 끝 index
        print(m.span()) # 일치하는 문자열의 시작 / 끝 index
    else:
        print("매칭되지 않음")

m = p.match("carelesscareless") # 주어진 문자열의 처음부터 일치하는지 확인
print_match(m)

# m = p.search("good care") # 주어진 문자열 중에 일치하는게 있는지 확인
# print_match(m)

# lst = p.findall("careless") # 일치하는 모든 것을 리스트 형태로 반환
# print(lst)