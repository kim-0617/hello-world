### 갤러리 사진스크래핑 - 저장
import requests
from bs4 import BeautifulSoup
import time

path = 'C:/Users/PC/Desktop/here'

for page in range(1,3):
    url = f'https://www.inven.co.kr/board/webzine/2097?iskin=lol&p={page}' # 전체목록
    res = requests.get(url)

    soup = BeautifulSoup(res.text, 'html5lib')
    sel = '#new-board > form > div > table > tbody > tr > td.tit > div > div > a' # 특정 게시물 선택
    titles = soup.select(sel)

    for tag in titles:
        sub_url = tag['href']
        res = requests.get(sub_url) # 특정 게시물로 이동
        soup = BeautifulSoup(res.text, 'html5lib')
        
        # 파일 이름 가공 (글의 제목으로)
        file_name = tag.text.strip()
        file_name = file_name.replace('\t','').split('\n')[1]
        file_name = file_name.replace('\t','').strip()

        # 파일이름에 포함시키면 안되는 문자들 처리
        rule_lst = ['/' ,'\\', '?', '%', '*', ':', '|', '"', '<', '>', '.']
        
        for rule in rule_lst:
            if rule in file_name:
                file_name = file_name.replace(rule,'')

        # 이미지 선택
        sel = '#BBSImageHolderTop > img'
        links = soup.select(sel)

        # 이미지 태그의 src 속성 선택
        for idx,link in enumerate(links):
            img_url = link['src']

            res = requests.get(img_url)
            if img_url[-4] == '.':
                extension = img_url[-3:]
            else:
                extension = img_url.split('.')[-1]

            with open(path + '/' + file_name + "." + extension, "wb") as f:
                    f.write(res.content)

        time.sleep(1)