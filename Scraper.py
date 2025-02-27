import os
from icrawler.builtin import BingImageCrawler,GoogleImageCrawler,BaiduImageCrawler
import glob
import socket
from tqdm import tqdm

starFilePath = "StarName.txt"

idStarFilePath = "id_name_url.txt"


def GetIpAddress():
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    return IPAddr


def ListFiles(path):
    rlt = glob.glob(path + "/*")
    rlt.sort()
    return rlt


def GetFileContent(fileName):
    with open(fileName, 'r') as f:
        return f.readlines()


def Download(storePath):
    if not os.path.exists(storePath):
        os.makedirs(storePath)

    ipAddr = GetIpAddress()
    ipTag = int(ipAddr.split(".")[-1])-128
    print(ipTag)
    lines = GetFileContent(idStarFilePath)
    #print(len(lines))
    for i, line in tqdm(enumerate(lines)):
        try:
            if i%8 != ipTag:
                continue

            cells = line.strip().split("\t")
            starId = cells[0]
            name = cells[1]
            file_path = os.path.join(storePath, f"{starId}_{name}")
            if not os.path.exists(file_path):
                os.makedirs(file_path)
                
            bing_storage = {'root_dir': file_path}
            bing_crawler = BaiduImageCrawler(parser_threads=4, downloader_threads=8, storage=bing_storage)
            bing_crawler.crawl(keyword=name, max_num=100)

        except Exception as a: 
            print("error exist",a)
            continue
        

basePath = "/devdata/spider"
#basePath = "data/spider"
Download(basePath)
# items = ListFiles(basePath)
# print(len(items))
