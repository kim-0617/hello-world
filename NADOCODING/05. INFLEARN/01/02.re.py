import re

# ^ : 문자열의 시작을 의미
# $ : 문자열의 종료를 의미
# | : OR 연산
# * : 문자가 0회 이상 반복됨을 의미

# re.match : 문자열의 시작부터 패턴이 존재하는지 검사
# re.search : 문자열의 전체에서 패턴이 존재하는지 검사
# re.split : 패턴을 구분자로 string을 분리하여 리스트 반환

# print(bool(re.match('ap','This is an apple'))) # False
# print(bool(re.search('ap','This is an apple'))) # True
# print(re.split('[:. ]+', 'apple Orange:banana tomato', 2)) # ['apple', 'Orange', 'banana tomato']

# c = re.compile(r"app\w*") # app을 포함하는거 > bapp 이런거는 app만 나옴, 왜..?
# print(c.findall("application orange apple banana")) # ['application', 'apple']
# print(c.findall("There are so many apples in the basket")) # ['apples']