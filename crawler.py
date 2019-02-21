from multiprocessing import Pool
from outerinfofeed import OuterInfo
from pprint import pprint as p
import metainfofeed
import time
import json
# from metainfofeed import MetaInfo
def writeJson(data, filename='data.json'):
    with open(filename, 'w', encoding="utf-8") as make_file:
        json.dump(data, make_file, ensure_ascii=False)

def faster(hashtag,maxNumOfFeed=10,filename='data.json',numOfProcess=1):
    start_time = time.time()

    maxNumOfFeed = 30
    info = OuterInfo(hashtag,maxNumOfFeed,filename=filename)
    
    pool = Pool(processes=numOfProcess)

    # writeJson(pool.map(metainfofeed.metaInfo, info.urlAndTag()[0]))

    with open('output_'+filename, 'w', encoding="utf-8") as make_file:
        json.dump(pool.map(metainfofeed.metaInfo, info.urlAndTag()[0]), make_file, ensure_ascii=False, indent='\n')

    # p(t)
    runTime = time.time() - start_time
    p(runTime)
#멀티프로세싱 적용한 크롤링 통해 시간 단축 예정
if __name__ == "__main__":
    faster('맛집',filename='data3.json', maxNumOfFeed=30,numOfProcess=1)