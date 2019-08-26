#!/usr/bin/python3
#-*- encoding:utf-8 -*-

import os
import sys
import time

import pathlib
import zipfile
import urllib.request

from bs4 import BeautifulSoup
#import requests

print("怀旧服 BigFoot 绿色插件包自动更新器  20190826 by 欧剃")
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
    print("      ...%d%%, %d MB, %d KB/s, 已用 %d 秒                         " %
           (percent, progress_size / (1024 * 1024), speed, duration), end="\r")
    

def savefile(url, filename):
    urllib.request.urlretrieve(url, filename, reporthook)

TempPath = pathlib.Path(str(os.sep).join(["_retail_","Interface"]))

# ------------------------------------------------------------
#a = input("按回车开始自动检测： ")

#page_link = "http://nga.178.com/read.php?tid=18302645&_ff=240"

#headers = {
#    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
#    "Connection": "keep-alive",
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
#    "Accept-Language": "zh-CN,zh;q=0.8"
#    }
  
#page_request = urllib.request.Request(url=page_link, headers=headers)

#page_response = urllib.request.urlopen(page_request).read()

#page_content = BeautifulSoup(page_response.content, "html.parser")
#version_list = page_content.find_all(class_='urltip')
#<span class="urltip">http://wow.bfupdate.178.com/BigFoot/Interface/classic/Interface.1.13.2.1.zip </span>

#current_version = str(version_list[0]).split("Interface.")[0].split(".zip")[-1]

#version = str(current_version)

#print("网络版本：", current_version)

# ----------------- 由于爬不到NGA帖子内容，可耻地注释了 -----------------

local_version = ""

#兼容不同系统的目录分隔符
#怀旧服 Interface 放在 _classic_ 内
lua_file_name = str(os.sep).join(["_classic_","Interface","AddOns","BigFoot","Version.cn.lua"])

try:
    with open(lua_file_name,"r",encoding='utf-8') as version_lua_file:
        a = ""
        a = version_lua_file.readline()
        #local main= "1.0.0."
        #local minor = "1"
        big_vers = version_lua_file.readline().split('"')[1]
        small_vers = version_lua_file.readline().split('"')[1]
except:
    local_version = "0.0.0.000"
    print("本地版本： 未安装或已损坏")
else:
    local_version = "".join([big_vers,small_vers])
    print("本地版本：", local_version)
finally:
    #version_lua_file.close()
    print("-------------")

print("本程序下载的大脚绿色插件包均来自： http://nga.178.com/read.php?tid=18302645 ")

print("因 NGACN 网站禁止脚本自动读取帖子内容，请手工打开↑上面这个网址，\n然后输入你想安装的插件包版本号:")

version=input()

a = ""
if local_version == version or "".join(local_version.split(".")) >= "".join(version.split(".")):
    a = "目前已安装最新版本插件，是否强制更新? Y/[N]/手动输入版本号"
elif int("".join(local_version.split("."))) > int("".join(version.split("."))):
    a = "已安装版本比你输入的版本更新，是否强制更新? Y/[N]/手动输入版本号"

if a:
    print(a)
    a = str(input(">>> "))
    if a.lower() != "y":
        if not a or not a[0].isdigit():
            print("不进行任何改动。")
            a = input("  ------ 按回车键退出 --------")
            quit()
        else:
            version = a
            a = input("准备手动更新 {} 版本，按回车确认开始：".format(version))

print("正在开始更新…… ")
print(" ")

filename = str(os.sep).join(["_classic_","Interface.{}.zip".format(version)])


zipPath = pathlib.Path(filename)

if not zipPath.exists():
    url = "http://wow.bfupdate.178.com/BigFoot/Interface/classic/Interface.{}.zip".format(version)

    print("正在尝试获取怀旧服插件版本", version, "，请稍候。" )

    print(url)
    try:
        savefile(url,filename)
    except:
        print("文件下载失败，请重试。")
        a = input("  ------ 按回车键退出 --------")       
        exit()
    
else:
    print(filename, "已下载。")

print(" ")

if TempPath.exists():
    print("重命名旧 Interface 文件夹... ", end="")

    old_folder_name = ["_classic_","Interface.old.{}".format(int(time.time()))]
    TempPath.rename(str(os.sep).join(old_folder_name))
    print("成功")
else:
    print("无需重命名。")
    

if zipPath.exists():

    print("开始解压文件: " + filename)

    file = zipfile.ZipFile(filename, "r");

    totalNum = len(file.namelist())
    current = 0
    
    for name in file.namelist():
        

        file.extract(name,path="_classic_")
        current = current + 1
        print("    >>> 解压缩： {} / {} ".format(current,totalNum),end="\r")
        
    print(" ")
    print("完毕。")

else:
    print("文件下载失败，请重试。")

a = input("  ------ 按回车键退出 --------")       
