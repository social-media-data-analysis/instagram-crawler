from multiprocessing import Pool
from outerinfofeed import OuterInfo
from innerinfofeed import MetaInfo
import time


#멀티프로세싱 적용한 크롤링 통해 시간 단축 예정
if __name__ == "__main__":
    self.start_time = time.time()

    pool = Pool(processes=4)
    pool.map()


    runTime = time.time() - self.start_time