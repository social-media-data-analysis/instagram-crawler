# instagram-crawler
Instagram crawler using Python for research data collection 

# Installation


```sh
$ git clone https://github.com/schio/instagram-crawler.git
$ pip install -r requirements.txt
```



# Usage


**How to use**

``` sh
$ python crawler.py seoul seoul100_4.json 120 4
```

**Print**

```sh
--------해시태그 검색 시작--------
스크롤 다운 횟수 : 1 피드 수 : 33
스크롤 다운 횟수 : 2 피드 수 : 45
스크롤 다운 횟수 : 3 피드 수 : 57
스크롤 다운 횟수 : 4 피드 수 : 69
스크롤 다운 횟수 : 5 피드 수 : 81
스크롤 다운 횟수 : 6 피드 수 : 81
스크롤 다운 횟수 : 7 피드 수 : 81
스크롤 다운 횟수 : 8 피드 수 : 117
스크롤 다운 횟수 : 9 피드 수 : 117
스크롤 다운 횟수 : 10 피드 수 : 129
#seoul에 대한 피드129개를 찾았습니다.
19 seconds | Num of feed : 129
---------------------------------
you can see result at < output_seoul100_4.json >. go to check!
total runtime is 51.16804623603821
```

**Two files are created.
First, output_outer <filename>**

```json
Return Format[
	fullyinfofeed[Url][Tag],    # <class 'numpy.ndarray'> 
	runTime,                    # <class 'float'> 크롤링 소요 시간
	lenFullyInfoFeed            # <class 'int'> 크롤링 한 피드 총 개수
]
```

**The second, output_ <filename>**

```json
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
```



# Help


```python crawler.py -h
$ python crawler.py -h
usage: crawler.py [-h] Hashtag Filename maxNumOfFeed numOfProcess

For Instagram Crawler

positional arguments:
  Hashtag       Hashtag you want to search
  Filename      File name to be saved
  maxNumOfFeed  How many feeds will you search for
  numOfProcess  Number of processes to use for multiprocessing

optional arguments:
  -h, --help    show this help message and exit
```