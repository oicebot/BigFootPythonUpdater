# BigFootPythonUpdater

用 Python3 写的一个更新魔兽世界大脚绿色插件包的脚本

在 Windows 10 下测试通过。

###依赖
1. pathlib
2. zipfile
3. urllib.request
4. bs4 （BeautifulSoup）
5. requests

###使用方式

##### Windows 系统 
1. 将下载的 .exe 文件复制到 WOW 根目录下，跟 _retail_ 文件夹以及 World of Warcraft Launcher.exe 同一目录。
2. 双击运行 .exe 文件。

##### 直接运行 Python 脚本
1. 安装 Python3
2. 将 .py 文件复制到 WOW 根目录下，跟 _retail_ 文件夹以及 World of Warcraft Launcher.exe 同一目录。
3. 双击运行 .py 文件。

###其他说明

安装的插件包文件来自 http://wow.bfupdate.178.com/BigFoot/Interface/3.1/Interface.{版本号}.zip

安装过程中会将已有的插件备份到 Interface.old.xxxx 文件夹中。

关于插件包的情况，详见 http://nga.178.com/read.php?tid=9545469
