#!python3
# -*- coding:utf-8 -*-

__author__="Panda Fang"
__copyright__ = "Copyright 2017, Panda Fang"
__license__ = "MIT"
__version__ = "1.0"

import shutil, os, send2trash, re, logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

fh = logging.FileHandler('mylog.log','a','utf-8')

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

fh.setFormatter(formatter)
logger.addHandler(fh)

# 这里写要被删除的文件夹或者文件的正则表达式
regex = re.compile(".mht$|.nfo$|abc.+(jpg|png)$")



def deltrash(path):
    for foldername, subfolders, filenames in os.walk(path):
        logger.debug('current folder is ' + foldername)

        for subfodler in subfolders:
            logger.debug('SUBFOLDER OF ' + foldername + ' : ' + subfodler)
            if regex.search(subfodler) != None:
                the_folder_path = os.path.join(foldername, subfodler)
                print(the_folder_path)
                send2trash.send2trash(the_folder_path)

        for filename in filenames:
            logger.debug('FILE INSIDE ' + foldername + ' : ' + filename)
            if regex.search(filename) != None:
                
                the_file_path = os.path.join(foldername, filename)
                print(the_file_path)
                send2trash.send2trash(the_file_path)

def main():
 
    # 改成自己实际的文件夹路径
    folders = [r'C:\folder1', r'D:\fodler2', r'E:\folder3']
    for folder in folders:
        deltrash(folder)


if __name__ == '__main__':
    main()

