from bs4 import BeautifulSoup
from pprint import pprint as p
import driver

def useHashTag(hashtag):
    url = 'https://www.instagram.com/explore/tags/'+hashtag
    chrome = driver.createDriver('/home/sco/install/chrome/chromedriver', url)
    print(chrome)

useHashTag('ny')