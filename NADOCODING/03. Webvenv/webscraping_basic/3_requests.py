import requests

res = requests.get("http://google.com")
res.raise_for_status() # 문제가 있을 때 바로 종료

if res.status_code == requests.codes.ok:
    print("정상입니다.")
else:
    print("문제가 생겼습니다. [에러코드 ", res.status_code, " ]")

print(len(res.text))

with open("mygoogle.html", "w", encoding="utf-8") as f:
    f.write(res.text)