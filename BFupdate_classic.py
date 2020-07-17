#!/usr/bin/python3
#-*- encoding:utf-8 -*-

import os
import sys
import time

import pathlib
import zipfile
import urllib.request

#from bs4 import BeautifulSoup

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.phantomjs.webdriver import WebDriver

print("怀旧服 BigFoot 绿色插件包自动更新器  20200418 by 欧剃")
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

TempPath = pathlib.Path(str(os.sep).join(["_classic_","Interface"]))

a = input("按回车开始自动检测： ")

print("\n开始读取NGA页面，可能需要一点时间……")

exename = 'phantomjs.exe' if os.name == 'nt' else 'phantomjs'

driver = WebDriver(executable_path=str(os.sep).join(['selenium','bin',exename]), port=5001)

page_link = "http://nga.178.com/read.php?tid=18302645&_ff=240"

driver.get(page_link)

try:
    WebDriverWait(driver,15).until(
        EC.presence_of_element_located((By.CLASS_NAME, "quote"))
    )
    print("已读取：", driver.title,"\n")
except Exception as e:
    print(e)

quote_list = driver.find_elements_by_class_name("quote")

version_list = quote_list[2].text.split()[0]
#2020/04/03(1.13.3.47)

#print(version_list)

current_version = str(version_list).split("(")[-1].split(")")[0]

version = str(current_version)

print("网络版本：", current_version)

driver.quit()

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

filename = os.sep.join(["_classic_","Interface.{}.zip".format(version)])


zipPath = pathlib.Path(filename)

if not zipPath.exists():
    url = "http://wow.bfupdate.178.com/BigFoot/Interface/classic/Interface.{}.zip".format(version)

    print("正在尝试获取怀旧服插件版本", version, "，请稍候。" )

    try:
        savefile(url,filename)
    except:
        print(" ")
        print("下载插件包失败，可能是大脚官网下载点挂了，或是官网自动获取的版本号不是最新。")
        print("鉴于当前怀旧服插件情况，建议重试，或检查你输入的版本号。")
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

    file = zipfile.ZipFile(filename, "r")

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
