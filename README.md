# WebInspection
## 简介
有时因为企业管理规定，对硬件进行人工巡检仍然不可疏忽。本项目应用selenium模块，自动登录硬件的带外管理系统web页面，并将首页截图，节约人工登录web所需时间。
## 运行环境
Python版本为3.6.8，Selenium版本为3.141.0    
* firefox版本为78.14.0esr，geckodriver版本为0.30.0    
selenium和firefox版本要求参考https://firefox-source-docs.mozilla.org/testing/geckodriver/Support.html   
* Chrome版本为94.0.4606.81，chromedriver与chrome版本相符        
1. 安装Selenium    
`pip3 install Selenium`  
2. 升级浏览器    
Firefox    
`yum install -y firefox`    
Chrome    
`vim /etc/yum.repos.d/google-chrome.repo`
写入：
```
[google-chrome]
name=google-chrome - \$basearch  
baseurl=http://dl.google.com/linux/chrome/rpm/stable/\$basearch  
enabled=1  
gpgcheck=0
```
运行`yum install google-chrome-stable`    
3. 安装webdriver    
* geckodriver（firefox）    
下载地址 https://github.com/mozilla/geckodriver/releases/latest    
`tar -zxvf geckodriver-v0.30.0-linux64.tar.gz`    
`mv geckodriver /usr/bin`    
* chromedriver（chrome）    
下载地址 http://chromedriver.storage.googleapis.com/index.html    
解压至 /usr/bin目录下    
 `chmod +x /usr/bin/chromedriver`
4. 验证    
在图形界面下运行如下脚本：
```
from selenium import webdriver
browser = webdriver.Firefox()
browser.close()
```
如果能成功打开firefox，则环境配置完成
## 使用
1. 填写主机信息    
按照hosts.xlsx示例文件格式，填写ip，url，用户名、密码、厂家、型号。    
原始版本包含DELL_M1000E、Huawei_E9000、Huawei_6800、ZTE_R8500、Inspur_NF8460M3、Huawei_RH5212六种型号的服务器及磁盘阵列
2. 信息加密    
运行`python3 encrypt.py`，按提示输入密码（salt），则目录下会生成hosts.txt密文文件    
运行`python3 decrypt.py`，按提示输入密码（salt），可验证密文文件是否正常
3. 运行命令    
运行`python3 WebInspection.py`，按提示输入密码（salt），即可自动运行    
本目录下会自动生成ScreenShot目录保存截图，自动生成log目录保存运行log
