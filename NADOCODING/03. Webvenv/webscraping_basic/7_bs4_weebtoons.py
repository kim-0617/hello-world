import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday" # 네이버 웹툰 url
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

# 네이버 웹툰 전체목록 가져오기
cartoons = soup.find_all("a", attrs={"class":"title"}) # a태그의 클래스가 title인 모든객체
for cartoon in cartoons:
    print(cartoon.get_text())

