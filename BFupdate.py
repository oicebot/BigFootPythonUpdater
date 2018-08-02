import os
import sys
import time

import pathlib
import zipfile
import urllib.request

print("BigFoot 绿色插件包自动更新器  20180802 by 欧剃")
print("--------------------------------------------")

def reporthook(count, block_size, total_size):
    global start_time
    if count == 0:
        start_time = time.time()
        return
    duration = time.time() - start_time + 0.00000000000000001
    progress_size = int(count * block_size)
    speed = int(progress_size / (1024 * duration))
    percent = int(count * block_size * 100 / total_size)
    #sys.stdout.write("\r...%d%%, %d MB, %d KB/s, 已用 %d 秒" %
    #                (percent, progress_size / (1024 * 1024), speed, duration))
    print("      ...%d%%, %d MB, %d KB/s, 已用 %d 秒                         " %
           (percent, progress_size / (1024 * 1024), speed, duration), end="\r")
    
    #sys.stdout.flush()

def savefile(url, filename):
    urllib.request.urlretrieve(url, filename, reporthook)

TempPath = pathlib.Path("Interface")

print("请输入要下载的大脚安装包版本，不知道当前版本号的请访问：")
print(" http://nga.178.com/read.php?tid=9545469&rand=479 ")

version = input("例如 8.0.0.694 ： ")

if not version:
    quit()

filename = "Interface.{}.zip".format(version)

zipPath = pathlib.Path(filename)

if not zipPath.exists():
    url = "http://wow.bfupdate.178.com/BigFoot/Interface/3.1/{}".format(filename)
    print(url)
    print("正在尝试获取", filename, "，请稍候。" )
    savefile(url,filename)
    
else:
    print(filename, "已下载。")

print(" ")

if TempPath.exists():
    print("重命名旧 Interface 文件夹... ", end="")
    TempPath.rename("Interface.old.{}".format(time.time()))
    print("成功")
else:
    print("无需重命名。")
    

if zipPath.exists():

    print("开始解压文件: " + filename)

    file = zipfile.ZipFile(filename, "r");

    totalNum = len(file.namelist())
    current = 0
    
    for name in file.namelist():

        file.extract(name)
        print("    >>> 解压缩： {} / {} ".format(current,totalNum),end="\r")
        current = current + 1
        
    print(" ")
    print("完毕。")

else:
    print("文件下载失败，请重试。")

a = input("  ------ 按回车键退出 --------")
        

