'''导入库'''
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

'''视频子目录的操作'''
def R2(web):
    while True:        
        sleep(5)
        web.switch_to_window(web.window_handles[2])
        web.refresh()
        sleep(5)
        ele = web.find_elements_by_css_selector('.ant-progress-text')        
        sleep(5)      
        for i in ele:
            if str(i.text) != '已完成':
                sleep(5)
                i.click()
                #web.refresh()
                break       
        web.close()            
        sleep(5)
        
        #视频播放界面
        web.switch_to_window(web.window_handles[2])
        web.find_element_by_css_selector(".ccH5PlayBtn").click()
        sleep(10)
        web.find_element_by_css_selector(".ccH5sp").click()
        web.find_element_by_css_selector('[data-sp = "2"]').click()
        ATIME = str(web.find_element_by_css_selector(".ccH5TimeTotal").text)
        print("all Time :")
        print(ATIME)
        while True:
            ActionChains(web).move_to_element(
                web.find_element_by_css_selector('.ccH5playerBox')
            ).perform()
            
            TIME = str(web.find_element_by_css_selector(".ccH5TimeCurrent").text)
            print(TIME)
            if TIME == ATIME:
                web.close()
                return               
            else:
                sleep(5)
                elements = web.find_elements_by_css_selector(".course_player_box")
                for e in elements:
                    
                    print(str(e.text))
                    if '让我看看你走神了没？' in str(e.text):
                        e.click()

    web.close()
    return

'''初始化'''
web = webdriver.Chrome()
web.get("https://www.ewt360.com/")
web.implicitly_wait(10)
print(web.window_handles)
web.find_element_by_css_selector("#username").send_keys("大大大大大大\n")
web.find_element_by_css_selector("#myClassEntrance").click()
web.maximize_window()



while True:
    sleep(5) 
    web.refresh()
    web.switch_to.window(web.window_handles[1])
    #选择视频选项
    web.find_element_by_css_selector(".ewt-tab-filter:nth-child(2) li:nth-last-child(1) button").click()
    sleep(5)
    ele = web.find_elements_by_css_selector('#app div  li div  button') 
    for i in ele:
        if str(i.text) == '做作业':
            
                i.click()
                break
                
    R2(web)
    
    sleep(5)
    

#视频子目录 .ant-progress-text
#播放按钮 .ccH5PlayBtn
#总时间 .ccH5TimeTotal
#当前播放时间 .ccH5TimeCurrent
#倍速调节  .ccH5sp
#2倍速 [data-sp = "2"]
#确认按键 .check_left_box
