# score_file = open("./basic/score.txt","w", encoding="UTF8")
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()

# score_file = open("./basic/score.txt","a", encoding="UTF8")
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close()

# score_file = open("./basic/score.txt","r", encoding="UTF8")
# print(score_file.read())
# score_file.close()

# score_file = open("./basic/score.txt","r", encoding="UTF8")
# print(score_file.readline(),end="") # 한줄읽고 커서는 다음줄로 이동
# print(score_file.readline(),end="") # 한줄읽고 커서는 다음줄로 이동
# print(score_file.readline(),end="") # 한줄읽고 커서는 다음줄로 이동
# print(score_file.readline(),end="") # 한줄읽고 커서는 다음줄로 이동
# score_file.close()

score_file = open("./basic/score.txt","r", encoding="UTF8")
raws = score_file.readlines()
for raw in raws:
    print(raw,end="")
score_file.close()