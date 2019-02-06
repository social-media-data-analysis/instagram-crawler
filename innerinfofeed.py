from outerinfofeed import OuterInfo
import driver

class InnerInfo():
    def __init__(self,link,browser):
        self.link = link
        self.browser = browser
    
    def all(self):
        print("d")

if __name__ == "__main__":

    # 인스타그램 공식 홈페이지
    instagramHompage = 'https://www.instagram.com'
        
    # 긁어올 주소
    url = 'https://www.instagram.com/explore/tags/'+self.hashtag

    #인스타그램 정보 담을 리스트 선언
    fullyinfofeed=[]

    # 크롬 드라이버 생성
    chromeDriverPath = '/home/sco/install/chrome/chromedriver'
    browser = driver.createDriver(chromeDriverPath, url)


    maxNumOfFeed = 30
    info = OuterInfo('호에에에엥',maxNumOfFeed)
    p(info.urlAndTag())
'''''''''''''''''''''
가져올 항목
    필수 ID, body, numOfLike
    ??? 덧글
'''''''''''''''''''''
