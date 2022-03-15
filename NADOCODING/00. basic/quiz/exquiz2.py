from random import *
question_list = ["apple", "banana", "orange"]
quiz_list = []

answer = question_list[randint(0,len(question_list)-1)]
print("정답은 : ", answer)
for i in range(len(answer)):
        print("_ ", end="")
        quiz_list.append("_ ")
print("\n")

while True:
    word = input("단어 하나를 입력하세요 >>>")
    if word in answer:
        word_count = answer.count(word)
        pos = []
        for cnt in range(word_count):
            if cnt == 0:
                pos.insert(cnt,answer.find(word))
            else:
                pos.insert(cnt,answer.find(word,pos[cnt-1]+1))
        for po in pos:
            quiz_list[po] = word
        
        for q_list in quiz_list:
            print(q_list, end="")
        print("\n")
    elif len(word)>=2:
        print("please put just one word")
    else:
        print("Wrong")
    
    if "_ " not in quiz_list :
        break

print("Success") 