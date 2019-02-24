from multiprocessing import Pool
from outerinfofeed import OuterInfo
from pprint import pprint as p
import metainfofeed
import time
import json
import argparse

# from metainfofeed import MetaInfo
def writeJson(data, filename='data.json'):
    with open(filename, 'w', encoding="utf-8") as make_file:
        json.dump(data, make_file, ensure_ascii=False)

def faster(hashtag,maxNumOfFeed=10,filename='data.json',numOfProcess=1):
# def faster(hashtag,filename, maxNumOfFeed,numOfProcess):
    start_time = time.time()
    info = OuterInfo(hashtag,maxNumOfFeed,filename=filename)
    
    
    pool = Pool(processes=numOfProcess)
    # pool = shared.Building.get_multiprocessing_pool()

    # writeJson(pool.map(metainfofeed.metaInfo, info.urlAndTag()[0]))

    filename = 'output_'+filename
    urlAndTag = info.urlAndTag()[0]

    result = pool.map(metainfofeed.metaInfo, urlAndTag)

    with open(filename, 'w', encoding="utf-8") as make_file:
        json.dump(result, make_file, ensure_ascii=False, indent='\n')
    
    print('---------------------------------')
    print('you can see result at <',filename,'>. go to check!')

    # p(t)
    runTime = time.time() - start_time
    print('total runtime is',runTime)

def main():
    parser = argparse.ArgumentParser(description='For Instagram Crawler')

    parser.add_argument('hashtag', type=str,
			metavar='Hashtag',
			help='Hashtag you want to search')
    parser.add_argument('filename', type=str,
			metavar='Filename',
			help='File name to be saved')
    parser.add_argument('maxNumOfFeed', type=int,
			metavar='maxNumOfFeed',
			help='How many feeds will you search for')
    parser.add_argument('numOfProcess', type=int,
			metavar='numOfProcess',
			help='Number of processes to use for multiprocessing')
    
    args = parser.parse_args()
    
    # hashtag = args.hashtag
    # filename = args.filename
    # maxNumOfFeed = args.maxNumOfFeed
    # numOfProcess = args.numOfProcess

    faster(args.hashtag,filename=args.filename, maxNumOfFeed=args.maxNumOfFeed,numOfProcess=args.numOfProcess)


#멀티프로세싱 적용한 크롤링 통해 시간 단축 예정
if __name__ == "__main__":
    main()
    # faster('한국',filename='korea13.json', maxNumOfFeed=100,numOfProcess=4)