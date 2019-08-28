#!/usr/bin/python3
#-*- encoding:utf-8 -*-

import os
import sys
import time

import pathlib
import zipfile
import urllib.request

from bs4 import BeautifulSoup

print("BigFoot 绿色插件包自动更新器  20190828 by 欧剃")
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

print("本程序下载的大脚绿色插件包均来自： http://nga.178.com/read.php?tid=9545469 ")

page_link = "http://bigfoot.178.com/wow/update.html"

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/51.0.2704.63 Safari/537.36'}

req = urllib.request.Request(url=page_link,headers=headers)
 
res = urllib.request.urlopen(req)
 
data = res.read().decode('utf-8')

page_content = BeautifulSoup(data, "html.parser")
version_list = page_content.find_all(class_='tit')

#[<span class="tit">V8.0.0.701版本说明</span>,
# <span class="tit">V8.0.0.700版本说明</span>]

current_version = str(version_list[0]).split("版本")[0].split("V")[-1]

version = str(current_version)

print("网络版本：", current_version)

local_version = ""

#兼容不同系统的目录分隔符
#8.1开始 Interface 放在 _retail_ 内
lua_file_name = str(os.sep).join(["_retail_","Interface","AddOns","BigFoot","Version.cn.lua"])

try:
    with open(lua_file_name,"r",encoding='utf-8') as version_lua_file:
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

a = ""
if local_version == version:
    a = "目前已安装最新版本插件，是否强制更新? Y/[N]/手动输入版本号"
elif int("".join(local_version.split("."))) > int("".join(version.split("."))):
    a = "已安装版本比网络发布页的更新，是否强制更新? Y/[N]/手动输入版本号"

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

filename = str(os.sep).join(["_retail_","Interface.{}.zip".format(version)])

zipPath = pathlib.Path(filename)

if not zipPath.exists():
    url = "http://wow.bfupdate.178.com/BigFoot/Interface/3.1/Interface.{}.zip".format(version)
    print(url)
    print("正在尝试获取版本", version, "，请稍候。" )
    a = ""
    while True:
        try:
            savefile(url,filename)
        except:
            print(" ")
            print("下载插件包失败，可能是大脚官网下载点挂了，或是官网自动获取的版本号不是最新。")
            print("请手动输入想要安装的版本号，或按回车直接退出：")
            a = str(input(">>> "))
            if not a or not a[0].isdigit():
                print("不进行任何改动。")
                a = input("  ------ 按回车键退出 --------")
                quit()
            else:
                version = a
                filename = str(os.sep).join(["_retail_","Interface.{}.zip".format(version)])
                zipPath = pathlib.Path(filename)
                if not zipPath.exists():
                    url = "http://wow.bfupdate.178.com/BigFoot/Interface/3.1/Interface.{}.zip".format(version)
                    print(url)
                    print("正在尝试获取版本", version, "，请稍候。" )
                else:
                    print(filename, "已下载。")
                    break
               
        else:
            break
            
    
else:
    print(filename, "已下载。")

print(" ")

if TempPath.exists():
    print("重命名旧 Interface 文件夹... ", end="")

    old_folder_name = ["_retail_","Interface.old.{}".format(int(time.time()))]
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
        

        file.extract(name,path="_retail_")
        current = current + 1
        print("    >>> 解压缩： {} / {} ".format(current,totalNum),end="\r")
        
    print(" ")
    print("完毕。")

else:
    print("文件下载失败，请重试。")

a = input("  ------ 按回车键退出 --------")       
