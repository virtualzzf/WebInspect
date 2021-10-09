# WebInspection
## 简介
有时因为企业管理规定，对硬件进行人工巡检仍然不可疏忽。本项目应用selenium模块，自动登录硬件的带外管理系统web页面，并将首页截图，节约人工登录web所需时间。
## 运行环境
Python版本为3.6.8，Selenium版本为3.141.0，firefox版本为78.14.0esr，geckodriver版本为0.30.0    
selenium和firefox版本要求参考https://firefox-source-docs.mozilla.org/testing/geckodriver/Support.html   
1. 安装Selenium    
`pip3 install Selenium`  
2. 升级firefox    
`yum install -y firefox`
3. 配置geckodriver    
下载地址 https://github.com/mozilla/geckodriver/releases/latest    
`tar -zxvf geckodriver-v0.30.0-linux64.tar.gz`    
`mv geckodriver /usr/bin`
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
按照hosts.xlsx示例文件格式，填写ip，url，用户名、密码、厂家、型号格式填写。    
原始版本适用于DELL_M1000E、Huawei_E9000、Huawei_6800、ZTE_R8500、Inspur_NF8460M3、Huawei_RH5212六种型号的服务器及磁盘阵列
2. 信息加密    
运行`python3 encrypt.py`，按提示输入密码（salt），则目录下会生成hosts.txt密文文件    
运行`python3 decrypt.py`，按提示输入密码（salt），可验证密文文件是否正常
3. 运行命令    
运行`python3 WebInspection.py`，按提示输入密码（salt），即可自动运行
本目录下会自动生成ScreenShot目录保存截图，自动生成log目录保存运行log
