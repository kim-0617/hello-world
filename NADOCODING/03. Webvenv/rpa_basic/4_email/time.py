import time
import datetime

# print(time.strftime('%d-%a-%Y'))
# print(time.strftime('%Y-%m-%d'))
# print(time.strftime('%Y-%m-%d/ %a'))

dt = datetime.datetime.strptime("2022-01-28", '%Y-%m-%d')
# print(type(dt))
# print(dt.strftime('%d-%a-Y'))
# print(dt)
print(datetime.datetime.strptime("2021-10-18 21:31:48",'%Y-%m-%d %H:%M:%S'))
