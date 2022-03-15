# 전역변수 지역변수
# 가급적 전역변수 사용을 피하자
gun = 10  # 전역변수

def checkpoint(soldiers): # 경계근무
    global gun
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    return gun

print("전체 총 : {0}".format(gun))
gun = checkpoint_ret(gun,2) 
print("남은 총 : {0}".format(gun))