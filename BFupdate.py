#!/usr/bin/python3
#-*- encoding:utf-8 -*-

import os
import sys
import time

import pathlib
import zipfile
import urllib.request

from bs4 import BeautifulSoup
import requests

print("BigFoot 绿色插件包自动更新器  20180819 by 欧剃")
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

TempPath = pathlib.Path("Interface")

print("本程序下载的大脚绿色插件包均来自： http://nga.178.com/read.php?tid=9545469 ")

a = input("按回车开始自动检测： ")

page_link = "http://bigfoot.178.com/wow/update.html"

page_response = requests.get(page_link, timeout=5)
page_content = BeautifulSoup(page_response.content, "html.parser")
version_list = page_content.find_all(class_='tit')
#[<span class="tit">V8.0.0.701版本说明</span>,
# <span class="tit">V8.0.0.700版本说明</span>]

current_version = str(version_list[0]).split("版本")[0].split("V")[-1]

version = str(current_version)

print("网络版本：", current_version)

local_version = ""

try:
    with open("Interface\AddOns\BigFoot\Version.cn.lua","r",encoding='utf-8') as version_lua_file:
        a = ""
        a = version_lua_file.readline()
        #local main= "8.0.0."
        #local minor = "695"
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

if local_version == version:
    a = input("目前已安装最新版本插件，是否强制更新? Y/[N]")
    if str(a).lower() != "y":
        print("不进行任何改动。")
        a = input("  ------ 按回车键退出 --------")
        quit()
    
a = input("按回车开始更新：")

print(" ")

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
    TempPath.rename("Interface.old.{}".format(int(time.time())))
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
        current = current + 1
        print("    >>> 解压缩： {} / {} ".format(current,totalNum),end="\r")
        
    print(" ")
    print("完毕。")

else:
    print("文件下载失败，请重试。")

a = input("  ------ 按回车键退出 --------")
        
