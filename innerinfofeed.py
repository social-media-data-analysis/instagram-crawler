from outerinfofeed import OuterInfo
from pprint import pprint as p
from urllib.request import urlopen
from bs4 import BeautifulSoup

class InnerInfo():
    def __init__(self,link):
        self.link = link
    
    def all(self):
        print("d")
def saveHtml(strHtml,filename):
    Html_file= open(filename,"w")
    Html_file.write(strHtml)
    Html_file.close()

if __name__ == "__main__":

    # url = urlandtag[0][0]
    url = 'https://www.instagram.com/p/Bm3hHBTl_3P/'
    url1 = 'https://www.instagram.com/p/BtfWKHfhvjp/'
    html = urlopen(url1)
    source = html.read()
    html.close()
    soup = BeautifulSoup(source,"html5lib")
    meta = soup.find("meta",  property="og:description")
    title = soup.find("title")
    hashtag = soup.find_all('meta', property="instapp:hashtags")
    # img = 
    
    print('meta -',meta)
    print()
    print('tilte -',title)
    print()
    print('hashtag -',hashtag)
    print()
    # soup = BeautifulSoup(urlopen(urlandtag[0][0], "html.parser"))
    # # datetime = soup.select('div > div > a > time')
    # numOfLike = soup.find_all('span')
    # # p(soup)
    # # p(datetime)
    # saveHtml(str(soup),'html4.html')
    
    # for i in numOfLike:
    #     p(i)
    #     print()
    #react-root > section > main > div > div > article > div.eo2As > div.k_Q0X.NnvRN > a > time
'''''''''''''''''''''
가져올 항목
    필수 ID, data, 일반내용, 해스태그내용, numOfLike, linkOfPic
    ??? 덧글, 좋아요 사람들 계정, 댓글 수
'''''''''''''''''''''

