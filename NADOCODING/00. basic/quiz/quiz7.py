# for i in range(1,51):
#     with open(f"./basic/quiz/{i}주차.txt","w",encoding='utf-8') as report_file:
#         report_file.write(f" - {i} 주차 주간보고 - ")
#         report_file.write("\n부서 : ")
#         report_file.write("\n이름 : ")
#         report_file.write("\n업무 요약 : ")

with open(f"./basic/quiz/21주차.txt", "r", encoding='utf-8') as report_file:
    raws = report_file.readlines()
    for raw in raws:
        print(raw)