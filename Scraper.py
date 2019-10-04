import os
from icrawler.builtin import BingImageCrawler
import glob
import socket

starFilePath = "StarName.txt"


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
    ipAddr = GetIpAddress()
    ipTag = int(ipAddr.split(".")[-1])-128
    print(ipTag)
    lines = GetFileContent(starFilePath)
    #print(len(lines))
    for i, line in enumerate(lines):
        if i%8 != ipTag:
            continue

        name = line.strip()
        file_path = os.path.join(storePath, name)
        if not os.path.exists(file_path):
            os.makedirs(file_path)

        bing_storage = {'root_dir': file_path}
        bing_crawler = BingImageCrawler(parser_threads=4, downloader_threads=8, storage=bing_storage)
        bing_crawler.crawl(keyword=name, max_num=100)

basePath = "data"
Download(basePath)
# items = ListFiles(basePath)
# print(len(items))
