# coding = utf-8
from selenium import webdriver
import time
import os
import scrypt
import getpass

#Login methods of each model
def DELL_M1000E_login(browser,username,password):
    browser.find_element_by_id("user_id").send_keys(username)
    browser.find_element_by_id("password").send_keys(password)
    browser.find_element_by_id("login_submit").click()
    return "MethodMatching!"
def Huawei_E9000_login(browser,username,password):
    browser.find_element_by_id("name").send_keys(username)
    browser.find_element_by_id("passwd").send_keys(password)
    browser.find_element_by_id("login").click()
    return "MethodMatching!"
def Huawei_6800_login(browser,username,password):
    browser.find_element_by_id("userName").send_keys(username)
    browser.find_element_by_id("passWord").send_keys(password)
    browser.find_element_by_id("loginBtn").click()
    return "MethodMatching!"
def ZTE_R8500_login(browser,username,password):
    browser.find_element_by_id("username").send_keys(username)
    browser.find_element_by_id("password").send_keys(password)
    browser.find_element_by_id("login").click()
    return "MethodMatching!"
def Inspur_NF8460M3_login(browser,username,password):
    browser.find_element_by_name("username").send_keys(username)
    browser.find_element_by_name("password").send_keys(password)
    browser.find_element_by_class_name("btn-success").click()
    return "MethodMatching!"
def Huawei_RH5212_login(browser,username,password):
    browser.find_element_by_id("UserName").send_keys(username)
    browser.find_element_by_id("Password").send_keys(password)
    browser.find_element_by_id("login").click()
    return "MethodMatching!"
def default(browser,username,password):
    print("no such model")
    return "NoModel"

switch = {'DELL_M1000E':DELL_M1000E_login,'Huawei_E9000':Huawei_E9000_login,"Huawei_6800":Huawei_6800_login,"ZTE_R8500":ZTE_R8500_login,"Inspur_NF8460M3":Inspur_NF8460M3_login,"Huawei_RH5212":Huawei_RH5212_login}
machines=[]
local_time=time.localtime()
check_date=time.strftime("%Y-%m-%d", local_time)
check_time=time.strftime("%Y-%m-%d-%H:%M:%S", local_time)
pic_path="./ScreenShot/"+check_date
log_path="./log"

print("------------------START------------------------")

#load data from file
print("------------------LOADING------------------------")
salt = getpass.getpass('password: ')
hosts_file = open("./hosts.txt","rb")
hosts_info_cipher = hosts_file.read()
hosts_file.close()
hosts_info_plain = scrypt.decrypt(hosts_info_cipher, salt)
hosts_info_list = hosts_info_plain.split("\n")
for line in hosts_info_list:
    values=line.split("\t")
    machine={"ip":values[0].strip(),"url":values[1].strip(),"username":values[2].strip(),"password":values[3].strip(),"model":values[4].strip()+"_"+values[5].strip('\n')}
    machines.append( machine)

#create screenshot and log directory
isExists=os.path.exists(pic_path)
if not isExists:
    os.makedirs(pic_path)
isExists=os.path.exists(log_path)
if not isExists:
        os.makedirs(log_path)

check_log=open(log_path+"/"+check_time+".log","w")

#Open web and capture a screenshot
print("------------------WEB PROCESSING------------------------")

#open browser
#browser = webdriver.Firefox()
browser = webdriver.Chrome()
browser.maximize_window()

for machine in machines:
    browser.get(machine["url"])
    time.sleep(10)
    method_match_status=switch.get(machine["model"], default)(browser,machine["username"],machine["password"])
    time.sleep(10)
    if browser.get_screenshot_as_file(pic_path+"/"+machine["ip"]+".png"):
        screen_shot_status="ScreenShotComplete!"
    else:
        screen_shot_status="ScreenShotFail"
    check_log.write(machine["ip"]+"\t"+method_match_status+"\t"+screen_shot_status+"\n")
browser.quit()
check_log.close()
print("-------------END-------------")
