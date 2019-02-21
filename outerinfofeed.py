from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from pprint import pprint as p
import driver
import time
import numpy as np
import re
import json


def unique_rows(a):
    a = np.ascontiguousarray(a)
    unique_a = np.unique(a.view([('', a.dtype)]*a.shape[1]))
    return unique_a.view(a.dtype).reshape((unique_a.shape[0], a.shape[1]))

class OuterInfo():
    def __init__(self, hashtag, maxFeed, filename='data.json'):
        print("--------해시태그 검색 시작--------")
        self.start_time = time.time()
        self.hashtag = hashtag
        self.maxFeed = maxFeed
        self.filename = filename

    def urlAndTag(self):
        '''''''''''''''''''''''''''''''''''''''''''''''''''
        Purpose
            해스태그에 해당하는 피드의 링크와 태그를 가져온다.
        
        Tag ex>
            Image may contain: screen, coffee cup and drink,
            Image may contain: 2 people, indoor,
            Image may contain: food
            No photo description available

        Input Format[
            hashatg,    # <class 'str'> 어떤 키워드로 검색할지
            maxFeed     # <class 'int'> 피드 최대 몇개 긁어올지
        ]

        Return Format[
            fullyinfofeed[Url][Tag],    # <class 'numpy.ndarray'> 
            runTime,                    # <class 'float'> 크롤링 소요 시간
            lenFullyInfoFeed            # <class 'int'> 크롤링 한 피드 총 개수
        ]
        '''''''''''''''''''''''''''''''''''''''''''''''''''
        
        # 인스타그램 공식 홈페이지
        instagramHompage = 'https://www.instagram.com'
        
        # 긁어올 주소
        url = 'https://www.instagram.com/explore/tags/'+self.hashtag

        #인스타그램 정보 담을 리스트 선언
        fullyinfofeed=[]

        # 크롬 드라이버 생성
        browser = driver.createDriver(url)
        time.sleep(1) # URL 접속 후 모든 정보 불러오기 위한 1초 대기시간 부여

        # 접속 URL의 body 부분 볼 것이다
        elem = browser.find_element_by_tag_name("body")

        
        # 피드 몇개 가져왔는지 계속 체크 하고 여기에 계속 append
        # 뒤에서 [-4]과 [-1] 비교해서 같으면 더 이상 찾을 것이 없다는 것으로 판단하고 결과반환
        numOfFeed=[-3,-2,-1] 

        # feed 가져온 개수
        beforeOfFeed=0
        numOfPageDown=1
        # URL 접속 후 PAGE DOWN 키 눌러(스크롤 내려서) 피드를 추가 로드
        while numOfFeed[-1] <= self.maxFeed:
            elem.send_keys(Keys.PAGE_DOWN) # PAGE DOWN Key 누름
            elem.send_keys(Keys.PAGE_DOWN)
            elem.send_keys(Keys.PAGE_DOWN)
            time.sleep(0.6) # 누른 후 정보 불러오기 위한 대기시간 부여
            
            

            # 지금까지 로드된 html 파싱
            html = browser.page_source
            soup = BeautifulSoup(html, 'html.parser')
            
            # 파싱한 html에서 피드 관련 정보가 담긴 v1Nh3 kIKUG _bz0w div만 볼 것
            divs=soup.find_all("div", attrs={'class':'v1Nh3 kIKUG _bz0w'}) 
                
            # html에서 정보추출을 위한 정규표현식 선언 
            feedLinkRe=re.compile(r"/p/.{11}") # URL of feed
            tagRe=re.compile(r"img alt=\".*class=\"F") # Tag of feed

            for div in divs:
                div=str(div.select('a')) # instagram feed link
                tag=str(tagRe.findall(div))[11:-12]
                fullyinfofeed.append(\
                    [instagramHompage+feedLinkRe.findall(div)[0],\
                    tag\
                    ])

            # fullyinfofeed = unique_rows(fullyinfofeed)
            lenFullyInfoFeed = len(unique_rows(fullyinfofeed))
            numOfFeed.append(lenFullyInfoFeed)
            print("스크롤 다운 횟수 :",numOfPageDown, "피드 수 :",numOfFeed[-1])

            # 피드를 추가적으로 불러오지 못했다면 다 불러온 것으로 판단
            if numOfFeed[-4] == numOfFeed[-1]:
                print("#"+self.hashtag+"에 대한 모든 피드 "+str(lenFullyInfoFeed)+"개를 찾았습니다.")
                return unique_rows(fullyinfofeed)
            else:
                numOfPageDown = numOfPageDown + 1

        runTime = time.time() - self.start_time
        print("#"+self.hashtag+"에 대한 피드"+str(lenFullyInfoFeed)+"개를 찾았습니다.")
        print("%d seconds" % runTime,"| Num of feed :",lenFullyInfoFeed)

        unique_rows(fullyinfofeed)[:self.maxFeed],runTime,lenFullyInfoFeed

        result = [unique_rows(fullyinfofeed)[:self.maxFeed],runTime,lenFullyInfoFeed]

        # 긁어온 링크와 사진 설명문 저장
        # resultJson = {
        #     'maxFeed' : unique_rows(fullyinfofeed)[:self.maxFeed].tolist(),
        #     'runTime' : runTime,
        #     'lenFullyInfoFeed' : lenFullyInfoFeed
        # }
        # with open('output_outer'+self.filename, 'w', encoding="utf-8") as make_file:
        #     json.dump(resultJson, make_file, ensure_ascii=False, indent='\t')

        return result

if __name__ == "__main__":
    maxNumOfFeed = 999
    info = OuterInfo('호에에에엥',maxNumOfFeed)
    p(info.urlAndTag())