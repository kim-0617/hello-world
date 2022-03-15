from email import header
import requests
from bs4 import BeautifulSoup
import re

headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"}

for i in range(1,6):
    print("페이지 : ",i)
    url = f"https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={i}&rocketAll=false&searchIndexingToken=&backgroundColor="
    res = requests.get(url,headers=headers)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "lxml")

    items = soup.find_all("li", attrs={"class",re.compile("^search-product")})
    for item in items:
        name = item.find("div", attrs={"class" : "name"}).get_text()
        # 애플 제품 제외
        if "Apple" in name:
            continue
        price = item.find("strong", attrs={"class" : "price-value"}).get_text()
        rate = item.find("em", attrs={"class" : "rating"})
        link = item.find("a", attrs={"class" : "search-product-link"})
        link = "https://www.coupang.com" + link["href"]
        if rate:
            rate = rate.get_text()
        else:
            rate = "평점없음"
            continue
        rate_cnt = item.find("span", attrs={"class" : "rating-total-count"})
        
        if rate_cnt:
            rate_cnt = rate_cnt.get_text()
            rate_cnt = int(rate_cnt[1:-1])
        else:
            rate_cnt = "평점 수 없음"
            
        if float(rate) >= 4.5 and rate_cnt > 100:
            print(f"제품명 : {name}")
            print(f"가격 : {price}")
            print(f"평점 : {rate} / 리뷰 수 : {rate_cnt}")
            print(f"링크 : {link}")
            print("-"*100)