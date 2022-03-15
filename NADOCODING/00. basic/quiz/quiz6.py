
def std_weight(height,gender):
    if gender == "남자":
        weight = round(height*height*22,2)
    elif gender == "여자":
        weight = round(height*height*21,2)
    else:
        print("성별을 잘못입력했네요.")
    return f"키 {height} {gender}의 표준 체중은 {weight}kg 입니다."

print(std_weight(1.75,"남자"))
print(std_weight(1.65,"여자"))
