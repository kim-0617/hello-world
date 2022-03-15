import requests
from bs4 import BeautifulSoup
import re
import os

def create_soup(url):
    headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"}  
    res = requests.get(url,headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text,"lxml")
    return soup

def scrape_weather():
    print("[오늘의 날씨]")
    url = "https://search.naver.com/search.naver?where=nexearch&sm=top_sly.hst&fbm=1&acr=1&ie=utf8&query=%EC%A0%95%EC%99%95%EB%8F%99+%EB%82%A0%EC%94%A8"
    soup = create_soup(url)

    # 흐림, 어제보다 00도 높아요
    weather1 = soup.find("span", attrs={"class":"weather before_slash"}).get_text()
    weather2 = soup.find("p", attrs={"class":"summary"}).get_text()
    y_pos = weather2.find("요")
    weather2 = weather2[:y_pos+1]
    weather = weather1 + ", " + weather2

    # 현재 00도 (최저 00도 / 최고 00도)
    now_temp = soup.find("div",attrs = {"class","temperature_text"}).get_text()
    max_temp = soup.find("span", attrs={"class":"highest"}).get_text()
    low_temp = soup.find("span", attrs={"class":"lowest"}).get_text()
    temp = (now_temp + "(" + low_temp + " / " + max_temp + ")").strip()
    
    # 오전 강수확률 00% . 오후 강수확률 00%
    rain_fall = soup.find_all("span",attrs = {"class","rainfall"})
    morn_rain_fall = rain_fall[0].get_text()
    after_rain_fall = rain_fall[1].get_text()
    rain = "오전 강수확률 " + morn_rain_fall + " / 오후 강수확률 " + after_rain_fall

    # 미세먼지 00 좋음
    # 초미세먼지 00 좋음
    dust = soup.find_all("span",attrs = {"class","txt"})
    mise = dust[0].get_text()
    cho_mise = dust[1].get_text()
    dust_stat = "미세먼지 " + mise + "\n초미세먼지 " + cho_mise

    # 출력
    print(weather)
    print(temp)
    print(rain)
    print(dust_stat)
    print()

def scrape_headlines():
    print("[헤드라인 뉴스]")
    
    url = "https://news.daum.net/"
    soup = create_soup(url)
    headlines = soup.find("ul", attrs={"class":"list_newsissue"}).find_all("li",limit=5)
    for idx,headline in enumerate(headlines):
        title = headline.find("a", attrs={"class":"link_txt"}).get_text().strip()
        link = headline.find("a")["href"]

        # 출력
        print(f"{idx+1}. {title}")
        print(f"링크 : {link}")
        print()

def scrape_it_news():
    print("[IT 뉴스]")
    
    url = "https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=105&sid2=230"
    soup = create_soup(url)
    it_headlines = soup.find("ul",attrs={"class":"type06_headline"}).find_all("li", limit=3)

    for idx, i in enumerate(it_headlines):
        a_idx = 0
        img = i.find("img")
        if img:
            a_idx = 1
        a_tag = i.find_all("a")[a_idx]

        title = a_tag.get_text().strip()
        link = a_tag["href"]

        # 출력
        print(f"{idx+1}. {title}")
        print(f"링크 : {link}")
        print()

def scrape_english():
    print("[오늘의 영어 회화]")

    url = "https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=haceng_submain_lnb_eng_I_others_english&logger_kw=haceng_submain_lnb_eng_I_others_english#;"
    soup = create_soup(url)

    sentenses = soup.find_all("div", attrs={"id":re.compile("^conv_kor_t")})
    print("\n(영어 지문)\n")
    for s in sentenses[len(sentenses)//2:]:
        print(s.get_text().strip())

    print("\n(한글 지문)\n")
    for s in sentenses[:len(sentenses)//2]:
        print(s.get_text().strip())

if __name__ == "__main__":
    scrape_weather() # 오늘의 날씨정보 가져오기
    scrape_headlines() # 헤드라인 뉴스 가져오기
    scrape_it_news() # it 헤드라인 뉴스 가져오기
    scrape_english() # 오늘의 영어회화 가져오기
    os.system("pause")