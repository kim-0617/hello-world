### fm코리아 이미지
import requests
from bs4 import BeautifulSoup
import datetime
import time
from random import *
#################################################################################################################

for page in range(1,10):
    rd_num = randint(1,4)
    time.sleep(rd_num)
    url = 'https://www.fmkorea.com/index.php?mid=afreecatv&category=2980561886&listStyle=list&page=' + str(page)
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    sel = '#bd_2978469841_0 > div > table > tbody > tr > td.title.hotdeal_var8'
    titles = soup.select(sel)

    for t in titles:
        print("------계시물 선택-------")
        sub_url = "https://www.fmkorea.com" + t.find('a')['href']
        rd_num = randint(1,4)
        time.sleep(rd_num)
        res = requests.get(sub_url)
        soup = BeautifulSoup(res.text, "html.parser")

        file_name = t.find('a').text.strip()   
        # 파일이름에 포함시키면 안되는 문자들 처리
        rule_lst = ['/' ,'\\', '?', '%', '*', ':', '|', '"', '<', '>', '.']        
        for rule in rule_lst:
            if rule in file_name:
                file_name = file_name.replace(rule,'')

        img = soup.find('div', attrs={'class':'rd_body'}).find_all('img')
        video = soup.find('div', attrs={'class':'rd_body'}).find_all('video')

        if img:
            for i in img:
                img_url = "https:" + i['src']
                rd_num = randint(1,4)
                time.sleep(rd_num)
                res = requests.get(img_url)
                print("이미지 저장 : ",img_url)
                now = datetime.datetime.now()
                now = time.strftime("%Y%M%d_%H%M%S")
                with open("./img/" + file_name + str(now) + ".png", "wb") as f:
                    f.write(res.content)
                time.sleep(1)

        if video:
            for v in video:
                try:
                    video_url = v.find('source').get('data-src')
                    video_url = "https:" + str(video_url)
                    print("비디오 저장 : ", video_url)
                    rd_num = randint(1,4)
                    time.sleep(rd_num)
                    res = requests.get(video_url)

                    now = datetime.datetime.now()
                    now = time.strftime("%Y%M%d_%H%M%S")
                    with open("./img/" + file_name + str(now) + ".mp4","wb") as f:
                        f.write(res.content)
                    time.sleep(1)
                except:
                    pass