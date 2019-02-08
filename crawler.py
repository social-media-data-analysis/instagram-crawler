from multiprocessing import Pool
from outerinfofeed import OuterInfo
from metainfofeed import MetaInfo
import time

def pr(p):
    print('!!!!!!!!!!!!!!!!!!!!')
    print(p)

#멀티프로세싱 적용한 크롤링 통해 시간 단축 예정
if __name__ == "__main__":
    start_time = time.time()

    pool = Pool(processes=4)
    
    result = pool.map(lambda x: MetaInfo.all() , OuterInfo('호에엥',5).urlAndTag()[0])

    runTime = time.time() - start_time