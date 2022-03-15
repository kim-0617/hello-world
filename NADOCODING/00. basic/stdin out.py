scores = {"국어" : 50, "수학" : 60, "영어" : 70}

# 정렬 / 8칸확보하고 왼쪽정렬, 4칸확보하고 오른쪽정렬
for subject, score in scores.items():
    print(subject.ljust(8), str(score).rjust(4),sep = ":")

# zfill : 3칸의 숫자 중 나머지는 0으로 채움
for num in range(21):
    print("대기번호 : " + str(num).zfill(3))
