# :project: zstu-covid19-report
# :author: L-ING
# :copyright: (C) 2022 L-ING <hlf01@icloud.com>
# :license: MIT, see LICENSE for more details.

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep, strftime, localtime, time
import os
import json
from notification import notify

class ZSTU:
    def __init__(self, headless=True):
        self.id = os.environ['ZSTU_ID']
        self.passwd = os.environ['ZSTU_PASSWD']

        with open('option.json') as file:
            option = json.load(file)
            self.location = option['Location']
            self.arrive_status = option['Arrive-Status']
            self.dna = str(option['DNA-Result'])
            self.antigen = str(option['Antigen-Result'])
            self.learning_status = str(option['Learning-status'])
        
        self.arrive_status_dict = {
            '1': '在（入）校，下沙及临平校区',
            '2': '在（入）校，下沙校区',
            '3': '在（入）校，临平校区',
            '4': '不在（入）校'
        }
        
        self.detect_dict = {
            '1': '未检测',
            '2': '阴性',
            '3': '阳性',
            '4': '已检测，结果未出',
        }

        self.learning_status_dict = {
            '1': '在校学习（含科研）',
            '2': '在本市实习实践（大杭州范围）',
            '3': '市外实习实践',
            '4': '联合培养单位学习（含科研）',
        }

        opt = Options()
        opt.add_argument('--headless')
        opt.add_argument('--disable-gpu')
        opt.add_argument('--no-sandbox')
        #禁止图片和css加载
        prefs = {"profile.managed_default_content_settings.images": 2,'permissions.default.stylesheet':2}
        opt.add_experimental_option("prefs", prefs)
        
        if headless:
            self.browser = webdriver.Chrome(options=opt) #不显示浏览器
        else:
            self.browser = webdriver.Chrome() #显示浏览器
        #self.browser.minimize_window()  # 最大化窗口
        self.wait = WebDriverWait(self.browser, 20) # 等待加载20s
        self.browser.get('http://fangyi.zstu.edu.cn:6006/iForm/1817056F47E744D3B8488B')

    def login(self):
        print('正在登录')
        self.enter_by_xpath(self.id, '/html/body/app-root/app-right-root/rg-page-container/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[1]/app-login-normal/div/form/div[1]/nz-input-group/input')
        self.enter_by_xpath(self.passwd, '/html/body/app-root/app-right-root/rg-page-container/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[1]/app-login-normal/div/form/div[2]/nz-input-group/input')
        self.click_by_xpath('/html/body/app-root/app-right-root/rg-page-container/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[1]/app-login-normal/div/form/div[6]/div/button')
        
    def run(self):
        print('\n'+strftime('%Y-%m-%d %H:%M:%S',localtime(time())))

        try:
            self.login()
        except:
            print('登录失败')
            raise RuntimeError('登录失败')

        print('等待alert出现')
        try:
            self.alert_handle()
        except:
            print('没有出现alert')

        print('开始打卡')

        try:
            self.browser.execute_script('document.getElementsByClassName("van-field__control")[6].readOnly = false') # 取消地理位置的只读状态，使其可以修改
            self.clear_by_xpath('//*[@id="iform"]/div[1]/div[3]/form/div[6]/div/div/div[2]/div/div/div/div[1]/input') # 清除地理位置框
            self.enter_by_xpath(self.location, '//*[@id="iform"]/div[1]/div[3]/form/div[6]/div/div/div[2]/div/div/div/div[1]/input') # 输入地理位置
            print('输入地理位置：%s'%self.location)
        except:
            print('地理位置输入失败')
            raise RuntimeError('地理位置输入失败')

        try:
            self.click_by_xpath('//*[@class="van-row iform-item iform-radiobox iform-item-ARRIVESTATUS"]/div/div/div[2]/div/div/div/div[1]/div/div[%s]/span'%self.arrive_status) # 默认核酸结果阴性
            print('选择入校状态：%s'%self.arrive_status_dict[self.arrive_status])
        except:
            print('入校状态选择失败')
            raise RuntimeError('入校状态选择失败')

        try:
            self.click_by_xpath('//*[@class="van-row iform-item iform-radiobox iform-item-SFYHSYXBG"]/div/div/div[2]/div/div/div/div[1]/div/div[%s]/span'%self.dna) # 默认核酸结果阴性
            print('选择核酸结果：%s'%self.detect_dict[self.dna])
        except:
            print('核酸结果选择失败')
            raise RuntimeError('核酸结果选择失败')

        try:
            self.click_by_xpath('//*[@class="van-row iform-item iform-radiobox iform-item-KYJCJG"]/div/div/div[2]/div/div/div/div[1]/div/div[%s]/span'%self.antigen) # 默认抗原结果阴性
            print('选择抗原结果：%s'%self.detect_dict[self.antigen])
        except:
            print('抗原结果选择失败')
            raise RuntimeError('抗原结果选择失败')

        try:
            self.click_by_xpath('//*[@class="van-row iform-item iform-radiobox iform-item-DQXXZT"]/div/div/div[2]/div/div/div/div[1]/div/div[%s]/span'%self.learning_status) # 默认在校学习
            print('选择学习状态：%s'%self.learning_status_dict[self.learning_status])
        except:
            print('学习情况选择失败')
            raise RuntimeError('学习情况选择失败')

        try:
            self.click_by_xpath('//*[@id="iform"]/div[1]/div[4]/div/button') # 提交
            print('点击提交')
            self.click_by_xpath('/html/body/div[3]/div[3]/button[2]') # 确认提交
            print('确认提交')
            self.click_by_xpath('/html/body/div[3]/div[2]/button') # 提交成功
            print('提交成功')
        except:
            print('提交失败')
            raise RuntimeError('提交失败')

        self.close()
        
    def close(self):
        self.browser.close()
    
    def alert_handle(self):
        self.wait.until(EC.alert_is_present())
        alert = self.browser.switch_to.alert
        print('alert:', alert.text)
        alert.accept()

    def click_by_xpath(self, path):
        submit = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, path)))
        submit.click()
        sleep(1)
    
    def enter_by_xpath(self, word, path):
        input = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, path)))
        input.send_keys(word)
        sleep(1)
    
    def clear_by_xpath(self, path):
        input = self.wait.until(EC.presence_of_element_located((By.XPATH, path)))
        input.clear()
        sleep(1)

if __name__ == '__main__':
    client = ZSTU()
    try:
        client.run()
    except Exception as ex:
        try:
            notify(ex)
        except:
            print('未设置微信通知')
