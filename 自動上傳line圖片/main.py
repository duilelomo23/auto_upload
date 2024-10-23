from selenium import webdriver
import time
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pyautogui
import random
import cv2
import numpy as np


wind = round(random.uniform(36,36.4),1)
print(wind)


#                          cd E:\python

#滑鼠點擊
def click_image(image,pos,  action, timestamp,offset=5):
    img = cv2.imread(image)
    pyautogui.moveTo(pos[0] + offset, pos[1] + offset, timestamp)
    pyautogui.click(button=action)


#圖片尋找
def imagesearch(image, precision=0.8):
    im = pyautogui.screenshot()
    img_rgb = np.array(im)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(image, 0)
    template.shape[::-1]

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    if max_val < precision:
        return [-1,-1]
    return max_loc #返回圖片座標



# #使用方式

def bug():
    time_time = 0.3
    bb =imagesearch("666.png")                        # 右下箭頭圖示      
    click_image("666.png", bb, "left", time_time)             # 點擊圖案座標                     


    aa =imagesearch("555.png")                        # 右下line圖示
    click_image("555.png", aa, "left", 0.1)             # 點擊圖案座標
    time.sleep(0.5)                    
    pyautogui.doubleClick()
    time.sleep(0.5)    

    pp =imagesearch("111.png")                        # 群組圖案
    if pp != [-1, -1]:
        click_image("111.png", pp, "left", time_time)             # 點擊圖案座標 
        pyautogui.doubleClick()
        time.sleep(0.5)
    else:
        cc =imagesearch("333.png")                        # line好友圖案                      
        click_image("333.png", cc, "left", time_time)             # 點擊圖案座標                      


        pp =imagesearch("111.png")                        # 群組圖案   
        click_image("111.png", pp, "left", time_time)             # 點擊圖案座標 
        pyautogui.doubleClick()
        time.sleep(0.5)

    cc =imagesearch("444.png")                        #體溫圖片位置  
    click_image("444.png", cc, "left", time_time)             #點擊座標
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.5)

    qq =imagesearch("222.png")                        # 輸入訊息位置
    click_image("222.png", qq, "left", time_time)             # 點擊圖案座標


    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.press('enter')




        



def name_(name,userPwd,wind):

    res = requests.get('https://utprev.pcbut.com.tw:8443/utprev/login.jsp?fbclid=IwAR1Rv1zkjue8pbYUGtrDnnnjD_vZjjJDbyU5bJgkAxd2PCHhQnpTLrGu98Q')
    root = BeautifulSoup(res.text, 'html.parser')
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    browser.get("https://utprev.pcbut.com.tw:8443/utprev/login.jsp?fbclid=IwAR1Rv1zkjue8pbYUGtrDnnnjD_vZjjJDbyU5bJgkAxd2PCHhQnpTLrGu98Q")
    browser.maximize_window()
    time.sleep(0.5)
    browser.find_element_by_name('userID').send_keys(name)                                         #帳號
    time.sleep(0.5)
    browser.find_element_by_name('userPwd').send_keys(userPwd)                                        #密碼
    time.sleep(0.5)
    browser.find_element_by_xpath('/html/body/form/table/tbody/tr[3]/td/button').click()           #登入
    time.sleep(0.5)
    browser.find_element_by_xpath('/html/body/div[5]/div[3]/div/button').click()                   #案OK /html/body/form/table/tbody/tr[3]/td/button
    time.sleep(0.5)
    browser.find_element_by_xpath('//*[@id="measureLoc"]/option[3]').click()                       #額溫
    time.sleep(0.5)
    browser.find_element_by_name('emptemp').send_keys(str(wind))                                   #溫度
    time.sleep(0.5)
    browser.find_element_by_xpath('/html/body/form/table/tbody/tr[5]/td[2]/label[' + str(d) + ']').click()      #是2否1   到廠 
    time.sleep(0.5)
    # browser.find_element_by_xpath('/html/body/form/table/tbody/tr[13]/td[2]/input[1]').click()     #是2否1  症狀      
    time.sleep(0.5)
    browser.find_element_by_xpath('//*[@id="ALL"]').click()                                        #送出
    time.sleep(0.5)
    pyautogui.press('enter')                                                                       #案OK
    pyautogui.press('enter')                                                                       #案OK
    myScreenshot = pyautogui.screenshot(region=(750, 200, 400, 350))                               #截圖 左上座標 寬 高
    myScreenshot.save('C:\\Users\\missi\\Desktop\\444.png')                                        #存檔
    pyautogui.moveTo(1007,1056)
    time.sleep(0.5)
    pyautogui.rightClick()
    time.sleep(0.5)
    pyautogui.press('s')
    time.sleep(1)
    bug()

d = int(input('上班 2  休息 1:'))

pyautogui.moveTo(1007,1056)


count_count = 0
count_time = True
if d == 2:
    print('上班')
else:
    print('休息')

name_('22A74', 'UniTech22A74', wind)


# while count_time:
#     localtime = time.strftime("%H:%M", time.localtime())
#     print(localtime)
#     if localtime == '00:06':
#         print('超過')
#         count_time = False
#         break
        
#     if localtime[:2] == '00' and int(localtime[-2:]) >= 5:
#         name_('22A74', wind)
#         print('ok')
#         count_time = False
#     time.sleep(60)


  



