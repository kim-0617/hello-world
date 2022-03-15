import imp
import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# print(soup.title.get_text()) # 첫번째로 발견되는 타이틀의 텍스트만 가져온다
# print(soup.a) # 첫번째로 발견되는 태그를 알려준다.
# print(soup.a.attrs) # 딕셔너리 형태
# print(soup.a["href"]) # a 태그의 원하는 속성가져오기

# print(soup.find("a", attrs={"class":"Nbtn_upload"})) # class가 nbtn_upload인 a element를 찾아줘
# # "a"를 빼면 모든 element에 대해서 클래스가 Nbtn_upload인 모든 element

rank1 = soup.find("li", attrs={"class":"rank01"}) # li태그의 class속성이 rank01인 객체를 rank1에 저장
# print(rank1.a) # 숩객체처럼 soup.find로 받아온 객체를 똑같이 숩객체.{태그}로 여러 정보를 볼 수 있음
# print(rank1.a.get_text())
# rank2 = rank1.next_sibling.next_sibling # next_sibling으로 부터 한번에 못받아오는것은 개행문자 이런게 있어서 그럴수도 있다. 한번더 하면 다음 랭크정보를 받아올 수 있음
# rank3 = rank2.next_sibling.next_sibling
# print(rank3.a.get_text())
# rank2 = rank3.previous_sibling.previous_sibling
# print(rank2.a.get_text())
# print(rank1.parent) # rank1의 부모
# rank2 = rank1.find_next_sibling("li")
# print(rank2.a.get_text())
# rank3 = rank2.find_next_sibling("li")
# print(rank3.a.get_text())
# rank2 = rank3.find_previous_sibling("li")
# print(rank2.a.get_text())
# print(rank1.find_next_siblings("li")) # 모든 형제노드 정보들을 가져옴

webtoon = soup.find("a", text="독립일기-시즌2 40화 깐부")
print(webtoon)