# BigFootPythonUpdater

用 Python3 写的一个更新魔兽世界大脚绿色插件包的脚本

在 Windows 10 下测试通过。

## 依赖
1. pathlib
2. zipfile
3. urllib.request
4. bs4 （BeautifulSoup）
5. ~~requests~~

## 使用方式

#### 下载地址

https://github.com/oicebot/BigFootPythonUpdater/releases 

#### Windows10 系统 
1. 将下载的 .exe 文件复制到 WOW 根目录下，跟 `_retail_` / `_classic_` 文件夹以及 World of Warcraft Launcher.exe 同一目录。
2. 双击运行 .exe 文件。

#### 直接运行 Python 脚本
1. 安装系统对应的 Python3 本体及依赖
2. 将 .py 文件复制到 WOW 根目录下，跟 `_retail_` / `_classic_` 文件夹以及 World of Warcraft Launcher.exe 同一目录。
3. 双击运行 .py 文件

详细安装使用教程请看本仓库的 [wiki](https://github.com/oicebot/BigFootPythonUpdater/wiki)

#### 怀旧服版更新器的特别说明

因 NGACN 网站禁止脚本自动读取帖子内容，怀旧服安装器（BFupdate_classic）用户需要手工输入你想安装的插件包版本号。

## 其他说明

安装的插件包文件来自 http://wow.bfupdate.178.com/BigFoot/Interface/3.1/Interface.{版本号}.zip

安装过程中会将已有的插件备份到 Interface.old.xxxx 文件夹中。

关于插件包的情况，详见 http://nga.178.com/read.php?tid=9545469
