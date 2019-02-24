from outerinfofeed import OuterInfo
from pprint import pprint as p
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import json
import requests

def saveHtml(body,filename):
    f = open(filename, 'w')
    f.write(body)
    f.close

def metaInfo(_urlAndTag):
    '''''''''''''''''''''''''''''''''''''''''''''''''''
    Purpose
        feed url의 meta data를 가져온다.
    
    Input Format[
        urlAndTag,    # result[0] of outerinfofeed.py
    ]
    Return Format[
        meta = {
            'id',                   # <class 'str'>
            'numOfLikes',           # <class 'int'>
            'numOfComments',        # <class 'int'>
            'hashtags',             # <class 'list'>
            'emptyHashtags',        # <class 'bool'>
            'url',                  # <class 'numpy.str_'>
            'tag',                  # <class 'numpy.str_'>
            'uploadDatetime',       # <class 'str'>
            'commentUsernames',     # <class 'list'>
            'imageUrl',             # <class 'str'>
            'errorFlag'             # <class 'bool'>    
        }           
    ]
    '''''''''''''''''''''''''''''''''''''''''''''''''''
    url = _urlAndTag[0]
    tag = _urlAndTag[1]
    req = requests.get(url)


    # url check
    # 만들어야함. url 잘못넘어왔을때 에러날 수 있음.

    soup = BeautifulSoup(req.text,"html5lib")
    
    # saveHtml(str(soup),'html2.html')

    #img url
    imageUrl = str(soup.find("meta",  property="og:image"))[15:-23]
    # orignal imageUrl is '<meta content="https://scontent-hkg3-1.cdninstagram.com/vp/91a459e456e488a232340c58a493878c/5D0FD47F/t51.2885-15/e35/51556523_1953173108128815_4366043563577951069_n.jpg?_nc_ht=scontent-hkg3-1.cdninstagram.com" property="og:image"/>'
    # so sliced

    metaDescription = str(soup.find("meta",  property="og:description"))  

    
    
    id = re.findall(r"@[a-z_.0-9]*",metaDescription)[0][1:]
    
    # hashtag 긁어오기
    metaHashtags = soup.find_all("meta",  property="instapp:hashtags")
    hashtags = []     
    
    for metaHashtag in metaHashtags:
        hashtags.append(str(metaHashtag)[15:-31])
    # print('-----type is',type(soup.find('script', type='application/ld+json')))
    
    try:
        strDateAndComment = soup.find('script', type='application/ld+json').text
        # 댓글 유저네임 긁어오기
        commentUsernames_parser = re.findall('"alternateName":"@.{1,30}","main', strDateAndComment) #유저네임 최대 길이 30임
        commentUsernames = []
        for commentUsername in commentUsernames_parser:
            commentUsernames.append(commentUsername[18:-7])
        uploadDatetime = re.findall('\d{4}-\d{2}-\d{2}.*\d{2}:\d{2}:\d{2}', strDateAndComment)[0]

        space = re.compile('[ ]+')
        # 좋아요 개수 긁어오기
        numOfLikes = space.split(re.findall(r"[0-9]* Likes",metaDescription)[0])[0] #findall이 list 형태 반환이기에 [0] 붙임

        # 댓글 개수 긁어오기
        numOfComments = space.split(re.findall(r"[0-9]* Comments",metaDescription)[0])[0] 
        errorFlag = False # 크롤링 중 누락 정보가 없다면 Flase
    except Exception as e:
        commentUsernames = ''
        uploadDatetime = ''
        numOfLikes = 0
        numOfComments = 0  
        errorFlag = True # 크롤링 중 누락정보가 있다면 True
        # print(e,url)
    # p(strDateAndComment.decode('euc-kr'))
    # strDateAndComment에서 date, 본문, 코멘트 추출하고 코멘트 다시 한글화 해줘야함.
    
    meta = {
        'id' : id, # 작성자 ID
        'numOfLikes' : int(numOfLikes), # 좋아요 수
        'numOfComments' : int(numOfComments), #댓글 수
        'hashtags' : hashtags, #본문 내 해시태그
        'emptyHashtags' : bool(hashtags), # 본문에 해시태그가 없는 경우(댓글에 해시태그를 다는 경우가 있음) false
        'url' : url, # Url of feed
        'tag' : tag, # 피드의 첫번째 사진에 대한 설명
        'uploadDatetime' : uploadDatetime, #피드 업로드 시간
        'commentUsernames' : commentUsernames, # 댓글 단 유저 목록
        'imageUrl' : imageUrl, # 사진 url
        'errorFlag' : errorFlag # 크롤링
    }

    return json.dumps(meta, ensure_ascii=False)


'''''''''''''''''''''
가져올 항목
    필수 +ID, 일반내용, +해스태그내용, +numOfLike, linkOfPic
    ??? 덧글, 좋아요 사람들 계정, +댓글 수, 
'''''''''''''''''''''
