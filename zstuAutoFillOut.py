from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

def zstu1(browser):
    browser.get('http://stu2.zstu.edu.cn/webroot/decision/url/mobile?redirect=http%3A%2F%2Fstu2.zstu.edu.cn%2Fwebroot%2Fdecision%2Furl%2Fmobile%3Fjs_api_path%3DL2NvbS9mci9wbHVnaW4vd2VpeGluL2Rpc3QvanMvd2VpWGluQ3VzdG9tQXBpLm1pbi5qcw%3D%3D%26sb%3DEAFDC54C57AEBA462875C1B8671EDE33%23%2Fdirectory#/login')
    
def zstu2(browser):
    browser.get('http://e2.zstu.edu.cn/webroot/decision/url/mobile?redirect=http%3A%2F%2Fe2.zstu.edu.cn%2Fwebroot%2Fdecision%2Furl%2Fmobile%3Fjs_api_path%3DL2NvbS9mci9wbHVnaW4vd2VpeGluL2Rpc3QvanMvd2VpWGluQ3VzdG9tQXBpLm1pbi5qcw%3D%3D%26sb%3D6EB9B7D5AD576DA781CB9D476711295B%23%2Fdirectory#/login')
    
def click(wait,path):
        submit = wait.until(EC.presence_of_element_located(
            (By.XPATH, path)))
        submit.click()
    
def enter(wait,word,path):
    input = wait.until(EC.presence_of_element_located(
        (By.XPATH, path)))
    input.send_keys(word)
        
class zstu:

    #browser.set_page_load_timeout(10)
    #browser.set_script_timeout(10)
    def __init__(self,num):
        account=open('account.txt','r')
        self.number=account.readline().strip('\n')
        self.password=account.readline().strip('\n')
        account.close()
        opt = Options()
        opt.add_argument('--headless')
        opt.add_argument('--disable-gpu')
        #self.browser = webdriver.Chrome() #显示浏览器
        self.browser = webdriver.Chrome(chrome_options=opt) #不显示浏览器
        #self.browser.minimize_window()  # 最大化窗口
        self.wait = WebDriverWait(self.browser, 10) # 等待加载10s
        if num==1:
            zstu1(self.browser)
        elif num==2:
            zstu2(self.browser)

    def login1(self):
        zstu1(self.browser)
        enter(self.wait,'%s'%self.number,'//*[@id="app"]/div/div[1]/div/div/div/div/div/div/div/div[2]/div[2]/div[1]/div/input')
        enter(self.wait,'%s'%self.password,'//*[@id="app"]/div/div[1]/div/div/div/div/div/div/div/div[2]/div[2]/div[2]/div[1]/input')
        click(self.wait,'//*[@id="app"]/div/div[1]/div/div/div/div/div/div/div/div[2]/div[2]/div[4]')
    
    def login2(self):
        zstu2(self.browser)
        enter(self.wait,'%s'%self.number,'//*[@id="app"]/div/div[1]/div/div/div/div/div/div/div/div[2]/div[2]/div[1]/div/input')
        enter(self.wait,'%s'%self.password,'//*[@id="app"]/div/div[1]/div/div/div/div/div/div/div/div[2]/div[2]/div[2]/div[1]/input')
        click(self.wait,'//*[@id="app"]/div/div[1]/div/div/div/div/div/div/div/div[2]/div[2]/div[4]')

    def run(self):
        click(self.wait,'//*[@id="app"]/div/div[1]/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div[3]/div/div/div[5]/div/div/div[3]')
        click(self.wait,'//*[@id="col_0_row_8"]')
        click(self.wait,'//*[@id="col_2_row_14"]/div/div/div/div/div[1]/div/div[1]')
        click(self.wait,'//*[@id="col_2_row_15"]/div/div/div/div/div[1]/div/div[1]')
        click(self.wait,'//*[@id="col_4_row_17"]/div/div/div/div/div[1]/div/div[1]')
        click(self.wait,'//*[@id="col_4_row_18"]/div/div/div/div/div[2]/div/div[1]')
        click(self.wait,'//*[@id="col_4_row_19"]/div/div/div/div/div[2]/div/div[1]')
        click(self.wait,'//*[@id="col_4_row_20"]/div/div/div/div/div[2]/div/div[1]')
        click(self.wait,'//*[@id="col_4_row_22"]/div/div/div/div/div[2]/div/div[1]')
        click(self.wait,'//*[@id="col_4_row_24"]/div/div/div/div/div[1]/div/div[1]')
        click(self.wait,'//*[@id="col_4_row_26"]/div/div/div/div/div[2]/div/div[1]')
        click(self.wait,'//*[@id="col_4_row_29"]/div/div/div/div/div[2]/div/div[1]')
        click(self.wait,'//*[@id="col_0_row_33"]/div[2]/div/div/div')
        
    def close(self):
        self.browser.close()
    
    def get_b(self):
        return self.browser
        
try:
    zs=zstu(1)
    z1=zs.get_b()
    zs.login1()
    zs.run()
    z1.close()
except Exception:
    z1.close()
    zs=zstu(2)
    z2=zs.get_b()
    zs.login2()
    zs.run()
    z2.close()
finally:
    z2.close()
