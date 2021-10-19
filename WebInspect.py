# coding = utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.expected_conditions import presence_of_all_elements_located
import time
import os
import scrypt
import getpass

#Login methods of each model
#incomplete
def HP_C7000_login(browser,username,password,wait):
    #browser.find_element_by_id("usernameInput").send_keys(username)
    #browser.find_element_by_id("passwordInput").send_keys(password)
    #browser.find_element_by_id("ID_LOGON").click()
    return "MethodMatching!"
def DELL_M1000E_login(browser,username,password,wait):
    if wait.until(presence_of_element_located((By.ID,"details-button"))) and wait.until(presence_of_element_located((By.ID,"proceed-link"))):
        browser.find_element(By.ID,"details-button").click()
        browser.find_element(By.ID,"proceed-link").click()
    else:
        print("Fail to dispaly Privacy error")
    if wait.until(presence_of_element_located((By.ID,"user_id"))) and wait.until(presence_of_element_located((By.ID,"password"))) and wait.until(presence_of_element_located((By.ID,"login_submit"))):
        browser.find_element(By.ID,"user_id").send_keys(username)
        browser.find_element(By.ID,"password").send_keys(password)
        browser.find_element(By.ID,"login_submit").click()
    else:
        print("Fail to display username and password")
    time.sleep(10)
    return "MethodMatching!"
def Huawei_E9000_login(browser,username,password,wait):
    if wait.until(presence_of_element_located((By.ID,"details-button"))) and wait.until(presence_of_element_located((By.ID,"proceed-link"))):
        browser.find_element(By.ID,"details-button").click()
        browser.find_element(By.ID,"proceed-link").click()
    else:
        print("Fail to dispaly Privacy error")
    if wait.until(presence_of_element_located((By.ID,"name"))) and wait.until(presence_of_element_located((By.ID,"passwd"))) and wait.until(presence_of_element_located((By.ID,"login"))):
        browser.find_element(By.ID,"name").send_keys(username)
        browser.find_element(By.ID,"passwd").send_keys(password)
        browser.find_element(By.ID,"login").click()
    else:
        print("Fail to display username and password")
    time.sleep(10)
    return "MethodMatching!"
#incomplete
def Cisco_12345_login(browser,username,password,wait):
    return "MethodMatching!"
#incomplete
def Hitachi_G400_login(browser,username,password,wait):
    browser.find_element_by_class_name("gwt-TextBox").send_keys(username)
    browser.find_element_by_class_name("gwt-PasswordTextBox").send_keys(password)
    #-----------------------can't find element-----------------
    #browser.find_element_by_class_name("gwt-PushButton-Logingwt-PushButton-Login-up").click()
    return "MethodMatching!"
#incomplete
def Huawei_6800_login(browser,username,password,wait):
    print("Hw6800:"+username+"-"+password)
    browser.find_element_by_id("userName").send_keys(username)
    browser.find_element_by_id("passWord").send_keys(password)
    browser.find_element_by_id("loginBtn").click()
    return "MethodMatching!"
def ZTE_R8500_login(browser,username,password,wait):
    if wait.until(presence_of_element_located((By.ID,"details-button"))) and wait.until(presence_of_element_located((By.ID,"proceed-link"))):
        browser.find_element(By.ID,"details-button").click()
        browser.find_element(By.ID,"proceed-link").click()
    else:
        print("Fail to dispaly Privacy error")
    if wait.until(presence_of_element_located((By.ID,"username"))) and wait.until(presence_of_element_located((By.ID,"password"))) and wait.until(presence_of_element_located((By.ID,"login"))):
        browser.find_element(By.ID,"username").send_keys(username)
        browser.find_element(By.ID,"password").send_keys(password)
        browser.find_element(By.ID,"login").click()
    else:
        print("Fail to display username and password")
    time.sleep(10)
    return "MethodMatching!"
#incomplete
def Sugon_I620_login(browser,username,password,wait):
    #browser.find_element_by_id("").send_keys(username)
    #browser.find_element_by_id("").send_keys(password)
    #browser.find_element_by_id("").click()
    return "MethodMatching!"
def Inspur_NF8460M3_login(browser,username,password,wait):
    if wait.until(presence_of_element_located((By.ID,"details-button"))) and wait.until(presence_of_element_located((By.ID,"proceed-link"))):
        browser.find_element(By.ID,"details-button").click()
        browser.find_element(By.ID,"proceed-link").click()
    else:
        print("Fail to dispaly Privacy error")
    if wait.until(presence_of_element_located((By.NAME,"username"))) and wait.until(presence_of_element_located((By.NAME,"password"))) and wait.until(presence_of_element_located((By.CLASS_NAME,"btn-success"))):
        browser.find_element(By.NAME,"username").send_keys(username)
        browser.find_element(By.NAME,"password").send_keys(password)
        browser.find_element(By.CLASS_NAME,"btn-success").click()
    else:
        print("Fail to display username and password")
    time.sleep(10)
    return "MethodMatching!"
#incomplete
def HP_DL380_login(browser,username,password,wait):
    #browser.find_element_by_id("").send_keys(username)
    #browser.find_element_by_id("").send_keys(password)
    #browser.find_element_by_id("").click()
    return "MethodMatching!"
def Huawei_RH5212_login(browser,username,password,wait):
    if wait.until(presence_of_element_located((By.ID,"details-button"))) and wait.until(presence_of_element_located((By.ID,"proceed-link"))):
        browser.find_element(By.ID,"details-button").click()
        browser.find_element(By.ID,"proceed-link").click()
    else:
        print("Fail to dispaly Privacy error")
    if wait.until(presence_of_element_located((By.ID,"UserName"))) and wait.until(presence_of_element_located((By.ID,"Password"))) and wait.until(presence_of_element_located((By.ID,"login"))):
        browser.find_element(By.ID,"UserName").send_keys(username)
        browser.find_element(By.ID,"Password").send_keys(password)
        browser.find_element(By.ID,"login").click()
    else:
        print("Fail to display username and password")
    return "MethodMatching!"
def default(browser,username,password,wait):
    print("no such model")
    return "NoModel"

switch = {'HP_C7000':HP_C7000_login,'DELL_M1000E':DELL_M1000E_login,'Huawei_E9000':Huawei_E9000_login,'Cisco_12345':Cisco_12345_login,'Hitachi_G400':Hitachi_G400_login,"Huawei_6800":Huawei_6800_login,"ZTE_R8500":ZTE_R8500_login,"Sugon_I620":Sugon_I620_login,"Inspur_NF8460M3":Inspur_NF8460M3_login,"HP_DL380":HP_DL380_login,"Huawei_RH5212":Huawei_RH5212_login}
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
wait = WebDriverWait(browser, 10)

for machine in machines:
    browser.get(machine["url"])
    method_match_status=switch.get(machine["model"], default)(browser,machine["username"],machine["password"],wait)
    if browser.get_screenshot_as_file(pic_path+"/"+machine["ip"]+".png"):
        screen_shot_status="ScreenShotComplete!"
    else:
        screen_shot_status="ScreenShotFail"
    check_log.write(machine["ip"]+"\t"+method_match_status+"\t"+screen_shot_status+"\n")
browser.quit()
check_log.close()
print("-------------END-------------")
