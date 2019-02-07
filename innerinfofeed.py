from outerinfofeed import OuterInfo
from pprint import pprint as p
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

class MetaInfo():
    def __init__(self,url):
        print()
        print('--------피드 상세 정보 로드--------')
        html = urlopen(url)
        source = html.read()
        html.close()
        self.soup = BeautifulSoup(source,"html5lib")

        # saveHtml(str(self.soup),'html5.html')

    def all(self):
        metaDescription = str(self.soup.find("meta",  property="og:description"))
        
        space = re.compile('[ ]+')

        # 좋아요 개수 긁어오기
        numOfLikes = space.split(re.findall(r"[0-9]* Likes",metaDescription)[0])[0] #findall이 list 형태 반환이기에 [0] 붙임

        # 댓글 개수 긁어오기
        numOfComments = space.split(re.findall(r"[0-9]* Comments",metaDescription)[0])[0] 
        id = re.findall(r"@[a-z_.0-9]*",metaDescription)[0][1:]
        
        # hashtag 긁어오기
        metaHashtags = self.soup.find_all("meta",  property="instapp:hashtags")
        hashtags = []     
        
        for metaHashtag in metaHashtags:
            hashtags.append(str(metaHashtag)[15:-31])

        # hashtag를 글 본문이 아닌 댓글에 단 경우
        if len(hashtags) == 0:
            hashtagsInCommentFlag = 1
        else:
            hashtagsInCommentFlag = 0
        
        return [id, numOfLikes, numOfComments, hashtags, hashtagsInCommentFlag]

def saveHtml(strHtml,filename):
    Html_file= open(filename,"w")
    Html_file.write(strHtml)
    Html_file.close()

if __name__ == "__main__":

    maxNumOfFeed=5
    info = OuterInfo('호에엥',maxNumOfFeed)
    urlAndTag = info.urlAndTag()
    url = urlAndTag[0][4][0]
    # metaInfo = MetaInfo(url)
    
    # all = metaInfo.all()
    all = MetaInfo(url).all()

    print('url :', url)
    print('tag :',urlAndTag[0][4][1])
    print('id :',all[0])
    print('numOfLikes :',all[1])
    print('numOfComments :',all[2])
    print('hashtags :',all[3])
    print('hashtagsInCommentFlag :',all[4])


'''''''''''''''''''''
가져올 항목
    필수 +ID, 일반내용, +해스태그내용, +numOfLike, linkOfPic
    ??? 덧글, 좋아요 사람들 계정, +댓글 수, 
'''''''''''''''''''''

