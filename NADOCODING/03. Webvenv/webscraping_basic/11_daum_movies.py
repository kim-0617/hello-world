import requests
from bs4 import BeautifulSoup
import re

for year in range(2015,2020):
    headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"}
    url = f"https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&sq=&o=&q={year}+%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84"
    res = requests.get(url,headers=headers)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "lxml")

    images = soup.find_all("img", attrs={"class":"thumb_img"})
    
    for idx,image in enumerate(images):
        img_url = image["src"]

        image_res = requests.get(img_url)
        image_res.raise_for_status()

        with open(f"movie_{year}_{idx+1}.jpg", "wb") as f:
            f.write(image_res.content)
        if idx == 4:
            break