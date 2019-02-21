from multiprocessing import Pool
from outerinfofeed import OuterInfo
from pprint import pprint as p
import metainfofeed
import time
# from metainfofeed import MetaInfo
def pr(p):
    print('!!!!!!!!!!!!!!!!!!!!')
    print(p)

#멀티프로세싱 적용한 크롤링 통해 시간 단축 예정
if __name__ == "__main__":
    start_time = time.time()

    maxNumOfFeed = 30
    info = OuterInfo('호에엥',maxNumOfFeed)
    
    pool = Pool(processes=4)
    
    # result = pool.map(lambda x: MetaInfo().all() , OuterInfo('호에엥',5).urlAndTag()[0])
    # print(p.map(f, info.urlAndTag())


    t=pool.map(metainfofeed.metaInfo, info.urlAndTag()[0])
    p(t)
    runTime = time.time() - start_time