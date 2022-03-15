import pickle
# profile_file = open("./basic/profile.pickle", "wb") # 피클을 쓰기위해선 바이너리 파일로 열어야함
# profile = {"이름" : "박명수", "나이" : "30", "취미" : ["축구","골프","코딩"]}
# print(profile)
# pickle.dump(profile,profile_file)
# profile_file.close()

profile_file = open("./0. basic/profile.pickle", "rb") # 피클을 쓰기위해선 바이너리 파일로 열어야함
profile = pickle.load(profile_file)
print(profile)
profile_file.close()