import time
import datetime
from xmlrpc.client import DateTime

# print(time.time()) # 1970년 이후로 누적된 초를 float 단위로 반환
# print(time.gmtime()) # UTC 기준 시퀸스 객체 반환
# print(time.localtime()) # 지방표준시 기준 시퀸스 객체 반환

# day = datetime.date.today()
# print(day) # 오늘
# print(day.month) # 몇월인가
# print(day.day) # 몇일인가
# print(day.max) # 마지막날?
# print(datetime.datetime(2009,3,15,20,0,30)) # 시간 표현

# now = datetime.datetime.now()
# print(now) # 지금
# print(now.date()) # 날짜
# print(now.time()) # 시간

dt = datetime.datetime.now()
td = datetime.timedelta(days= -3)
print(dt + td) # 3일전 시간