from outerinfofeed import OuterInfo
from pprint import pprint as p
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import json
import chardet



class MetaInfo():
    def __init__(self,_urlAndTag):

        print()
        print('--------피드 상세 정보 로드--------')
        
        self.url = _urlAndTag[0]
        self.tag = _urlAndTag[1]
        html = urlopen(self.url)
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

        strDateAndComment = self.soup.find('script', type='application/ld+json').text
        print('?????????????????????????')
        
        # 업로드 시간 긁어오기
        uploadDatetime = re.findall('\d{4}-\d{2}-\d{2}.*\d{2}:\d{2}:\d{2}', strDateAndComment)[0]
        
        # 댓글 유저네임 긁어오기
        commentUsernames_parser = re.findall('"alternateName":"@.{1,30}","main', strDateAndComment) #유저네임 최대 길이 30임
        commentUsernames = []
        for commentUsername in commentUsernames_parser:
            commentUsernames.append(commentUsername[18:-7])
        
        # p(strDateAndComment.decode('euc-kr'))
        # strDateAndComment에서 date, 본문, 코멘트 추출하고 코멘트 다시 한글화 해줘야함.
        print('?????????????????????????')
        
        self.meta = {
            'id' : id, # 작성자 ID
            'numOfLikes' : numOfLikes, # 좋아요 수
            'numOfComments' : numOfComments, #댓글 수
            'hashtags' : hashtags, #본문 내 해시태그
            'emptyHashtags' : bool(hashtags), # 본문에 해시태그가 없는 경우(댓글에 해시태그를 다는 경우가 있음)
            'url' : self.url, # Url of feed
            'tag' : self.tag, # 피드의 첫번째 사진에 대한 설명
            'uploadDatetime' : uploadDatetime, #피드 업로드 시간
            'commentUsernames' : commentUsernames
        }
        
        return json.dumps(self.meta, ensure_ascii=False)

if __name__ == "__main__":

    maxNumOfFeed=3
    info = OuterInfo('호에엥',maxNumOfFeed)
    urlAndTags = info.urlAndTag()
    urlAndTag = urlAndTags[0][0]

    # p(urlAndTag[0])
    meta = MetaInfo(urlAndTag).all()
    p(meta)
    


'''''''''''''''''''''
가져올 항목
    필수 +ID, 일반내용, +해스태그내용, +numOfLike, linkOfPic
    ??? 덧글, 좋아요 사람들 계정, +댓글 수, 
'''''''''''''''''''''
