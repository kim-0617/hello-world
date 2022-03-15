# 집합
# 중복 안됨, 순서 없음

my_set = {1,2,3,3,3}
print(my_set) # 1,2,3 출력

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

# 교집합 
print(java & python) # 유재석 출력
print(java.intersection(python)) # 유재석 출력

# 합집합
print(java | python) # 김태호, 양세형, 박명수, 유재석 출력
print(java.union(python))

# 차집합
print(java - python)
print(java.difference(python))

# python에 데이터 추가하기
python.add("김태호")
print(python)

# java에 데이터 삭제하기
python.remove("김태호")
print(python)