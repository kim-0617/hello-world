import requests

url = "https://nadocoding.tistory.com/"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"}

res = requests.get(url, headers = headers)
res.raise_for_status() # 문제가 있을 때 바로 종료

with open("nadocoding.html", "w", encoding="utf-8") as f:
    f.write(res.text)