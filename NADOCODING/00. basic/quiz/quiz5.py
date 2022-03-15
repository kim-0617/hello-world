from random import *

passenger = [i for i in range(1,51)]
passenger_time = []
cnt = 0
for i in range(0,len(passenger)):
    seek_time = randint(5,50)
    passenger_time.append(seek_time)

for i in range(0,len(passenger)):
    if 5<= passenger_time[i] <= 15:
        mark = "O"
        cnt += 1
    else:
        mark = ""
    print(f"[{mark}] {passenger[i]}번째 손님 (소요시간 : {passenger_time[i]}분 )")

print(f"총 탑승 승객 : {cnt}분")