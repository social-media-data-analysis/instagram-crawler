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

    info = OuterInfo(hashtag,maxNumOfFeed,filename=filename)
    
    pool = Pool(processes=numOfProcess)

    # writeJson(pool.map(metainfofeed.metaInfo, info.urlAndTag()[0]))

    filename = 'output_'+filename
    with open(filename, 'w', encoding="utf-8") as make_file:
        json.dump(pool.map(metainfofeed.metaInfo, info.urlAndTag()[0]), make_file, ensure_ascii=False, indent='\n')
    
    print('---------------------------------')
    print('you can see result at <',filename,'>. go to check!')

    # p(t)
    runTime = time.time() - start_time
    print('total runtime is',runTime)

#멀티프로세싱 적용한 크롤링 통해 시간 단축 예정
if __name__ == "__main__":
    faster('한국',filename='korea11.json', maxNumOfFeed=100,numOfProcess=4)