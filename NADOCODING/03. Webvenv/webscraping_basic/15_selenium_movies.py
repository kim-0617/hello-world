from traceback import print_tb
from attr import attr
import requests
from bs4 import BeautifulSoup

url="https://play.google.com/store/movies/details/%EB%B2%A0%EB%86%88_2_%EB%A0%9B_%EB%8D%B0%EC%96%B4_%EB%B9%84_%EC%B9%B4%EB%8B%88%EC%A7%80_Venom_Let_There_Be_Carnage?id=980e3tkCMZE.P"
headers={ 
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
    "Accept-Language":"ko-KR,ko" 
}
res=requests.get(url,headers=headers)
res.raise_for_status()
soup=BeautifulSoup(res.text,"lxml")

titles = soup.find("h1", attrs = {"class":"Fd93Bb F5UCq p5VxAd"})
titles = titles.find("span").get_text()

print(titles)

