from bs4 import BeautifulSoup
from pprint import pprint as p
import driver
from multiprocessing import Pool
import time
import numpy as np
import re
from selenium.webdriver.common.keys import Keys

def unique_rows(a):
    a = np.ascontiguousarray(a)
    unique_a = np.unique(a.view([('', a.dtype)]*a.shape[1]))
    return unique_a.view(a.dtype).reshape((unique_a.shape[0], a.shape[1]))

def outerInfo(hashtag, maxFeed):
    # 인스타그램 공식 홈페이지
    instagramHompage = 'https://www.instagram.com'
    
    # 긁어올 주소
    url = 'https://www.instagram.com/explore/tags/'+hashtag

    #인스타그램 정보 담을 리스트 선언
    fullyinfofeed=[]

    # 크롬 드라이버 생성
    chromeDriverPath = '/home/sco/install/chrome/chromedriver'
    browser = driver.createDriver(chromeDriverPath, url)
    time.sleep(1) # URL 접속 후 모든 정보 불러오기 위한 1초 대기시간 부여

    # 접속 URL의 body 부분 볼 것이다
    elem = browser.find_element_by_tag_name("body")

    # feed 가져온 개수    
    numOfFeed=0
    beforeOfFeed=0
    numOfPageDown=0
    # URL 접속 후 PAGE DOWN 키 눌러(스크롤 내려서) 피드를 추가 로드
    while numOfFeed <= maxFeed:
        elem.send_keys(Keys.PAGE_DOWN) # PAGE DOWN Key 누름
        elem.send_keys(Keys.PAGE_DOWN)
        elem.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.6) # 누른 후 정보 불러오기 위한 대기시간 부여
        numOfPageDown = numOfPageDown + 1
        

        # 지금까지 로드된 html 파싱
        html = browser.page_source
        soup = BeautifulSoup(html, 'html.parser')
        
        # 파싱한 html에서 피드 관련 정보가 담긴 v1Nh3 kIKUG _bz0w div만 볼 것
        divs=soup.find_all("div", attrs={'class':'v1Nh3 kIKUG _bz0w'}) 
               
        # html에서 정보추출을 위한 정규표현식 선언 
        feedLinkRe=re.compile(r"/p/.{11}")
        tagRe=re.compile(r"img alt=\".*class=\"F")

        for div in divs:
            div=str(div.select('a')) # instagram feed link
            tag=str(tagRe.findall(div))[11:-12]
            fullyinfofeed.append(\
                [instagramHompage+feedLinkRe.findall(div)[0],\
                tag\
                ])

        # fullyinfofeed = unique_rows(fullyinfofeed)
        numOfFeed = len(unique_rows(fullyinfofeed))
        print("스크롤 다운 횟수 :",numOfPageDown, "피드 수 :",numOfFeed)
        # if beforeOfFeed == numOfFeed:
        #     print("#"+hashtag+"에 대한 모든 피드 "+str(numOfFeed)+"개를 찾았습니다.")
        #     return fullyinfofeed
        # else:
        #     beforeOfFeed = numOfFeed
    print("#"+hashtag+"에 대한 피드 "+str(numOfFeed)+"개를 찾았습니다.")
    return unique_rows(fullyinfofeed)

start_time = time.time()
test=outerInfo('호에에에엥',288)


for i in range(len(test)):
    print(i,test[i])

print("%d seconds" % (time.time() - start_time),"| Num of feed :",len(test))