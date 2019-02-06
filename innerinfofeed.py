from outerinfofeed import OuterInfo
from pprint import pprint as p
from urllib.request import urlopen
from bs4 import BeautifulSoup

class InnerInfo():
    def __init__(self,link):
        self.link = link
    
    def all(self):
        print("d")
def saveHtml(html):
    Html_file= open("html.html","w")
    Html_file.write(html)
    Html_file.close()

if __name__ == "__main__":

    # maxNumOfFeed = 30
    # info = OuterInfo('호에에엥',maxNumOfFeed)
    # urlandtag = info.urlAndTag()

    # p(len(urlandtag))
    # p(urlandtag[1])
    # p(urlandtag[2])
    
    # url = urlandtag[0][0]
    url = 'https://www.instagram.com/p/Bm3hHBTl_3P/'
    html = urlopen(url)
    source = html.read()
    html.close()
    soup = BeautifulSoup(source,"html5lib")
    # soup = BeautifulSoup(urlopen(urlandtag[0][0], "html.parser"))
    datetime = soup.select('div > div > a > time')
    # p(soup)
    # p(datetime)
    saveHtml(str(soup))
    #react-root > section > main > div > div > article > div.eo2As > div.k_Q0X.NnvRN > a > time
'''''''''''''''''''''
가져올 항목
    필수 ID, data, body, numOfLike, linkOfPic
    ??? 덧글
'''''''''''''''''''''
# url = "https://www.rottentomatoes.com/"
# html = urlopen(url)
# source = html.read() # 바이트코드 type으로 소스를 읽는다.
# html.close() # urlopen을 진행한 후에는 close를 한다.

# soup = BeautifulSoup(source, "html5lib")

