from bs4 import BeautifulSoup
from pprint import pprint as p
import driver
from multiprocessing import Pool
import time
import re
from selenium.webdriver.common.keys import Keys

def useHashTag(hashtag):
    url = 'https://www.instagram.com/explore/tags/'+hashtag
    chromeDriverPath = '/home/sco/install/chrome/chromedriver'
    browser = driver.createDriver(chromeDriverPath, url)
    time.sleep(1)
    elem = browser.find_element_by_tag_name("body")
    no_of_pagedowns = 2
 
    while no_of_pagedowns:
        elem.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.2)
        no_of_pagedowns-=1

    html = browser.page_source
    soup = BeautifulSoup(html, 'html.parser')
    
    divs=soup.find_all("div", attrs={'class':'v1Nh3 kIKUG _bz0w'})
    fullyinfofeed=[]
    
    feedLinkRe=re.compile(r"/p/.{11}")
    tagRe=re.compile(r"img alt=\".*class=\"F")
    # <img alt="Image may contain: 1 person"
    for div in divs:
        # p(type(div))
        # p(div.select('a'))
        # strdiv.append(div.select('a'))
        # strdiv.append(feedLinkRe.findall(str(div.select('a'))))
        # p(div.get('href'))
        div=str(div.select('a'))
        # tag=re.sub('img alt="','',tagRe.findall(div))
        tag=tagRe.findall(div)
        fullyinfofeed.append([feedLinkRe.findall(div),tag])
    p(fullyinfofeed)
    # p(type(strdiv))
    # p(type(strdiv[0]))
    # p(len(strdiv))
    # p(len(strdiv[0]))
    # p(strdiv)
    # for test in strdiv[0]:
    #     p(test)
    # p(strdiv[0][0])
    # t='fdhjdfg/p/Bta8BvhHq3C/dhjfg'
    # p(feedLinkRe.findall(t))
    # /p/BtVn-5Qna9a/
    
#     18. 속성이 있는지 확인
# tag.has_attr('class') 
# tag.has_attr('id')
# 있으면 True, 없으면 False


start_time = time.time()
useHashTag('빅데이터')
# pool = Pool(processes=4) # 4개의 프로세스를 사용합니다.
# pool.map(useHashTag('빅데이터')) # get_contetn 함수를 넣어줍시다.
print("--- %s seconds ---" % (time.time() - start_time))

# //*[@id="react-root"]/section/main/article/div[2]/div/div[6]/div[1]/a
#react-root > section > main > article > div:nth-child(3) > div > div:nth-child(1) > div:nth-child(2) > a
#react-root > section > main > article > div:nth-child(3) > div > div:nth-child(6) > div:nth-child(1) > a
#react-root > section > main > article > div:nth-child(3) > div > div:nth-child(7) > div:nth-child(3) > a

# //*[@id="react-root"]/section/main/article/div[2]/div/div[7]/div[3]/a
# //*[@id="react-root"]/section/main/article/div[2]/div/div[9]/div[3]/a

#react-root > section > main > article > div:nth-child(3) > div > div:nth-child(1) > div:nth-child(1) > a
#react-root > section > main > article > div:nth-child(3) > div > div:nth-child(11) > div:nth-child(3) > a