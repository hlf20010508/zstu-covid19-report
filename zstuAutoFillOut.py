from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
 
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
    def __init__(self):
        account=open('account.txt','r')
        self.number=account.readline().strip('\n')
        self.password=account.readline().strip('\n')
        option=account.readline().strip('\n')
        account.close()
        opt = Options()
        opt.add_argument('--headless')
        opt.add_argument('--disable-gpu')
        opt.add_argument('--no-sandbox')
        
        if option=='0':
            self.browser = webdriver.Chrome(options=opt) #不显示浏览器
        elif option=='1':
            self.browser = webdriver.Chrome() #显示浏览器
        #self.browser.minimize_window()  # 最大化窗口
        self.wait = WebDriverWait(self.browser, 60) # 等待加载60s
        self.browser.get('http://e2.zstu.edu.cn/webroot/decision/url/mobile?redirect=http%3A%2F%2Fe2.zstu.edu.cn%2Fwebroot%2Fdecision%2Furl%2Fmobile%3Fjs_api_path%3DL2NvbS9mci9wbHVnaW4vd2VpeGluL2Rpc3QvanMvd2VpWGluQ3VzdG9tQXBpLm1pbi5qcw%3D%3D%26sb%3D6EB9B7D5AD576DA781CB9D476711295B%23%2Fdirectory#/login')

    def login(self):
        print('正在登录 E浙理')
        enter(self.wait,'%s'%self.number,'//*[@id="app"]/div/div[1]/div/div/div/div/div/div/div/div[2]/div[2]/div[1]/div/input')
        enter(self.wait,'%s'%self.password,'//*[@id="app"]/div/div[1]/div/div/div/div/div/div/div/div[2]/div[2]/div[2]/div[1]/input')
        click(self.wait,'//*[@id="app"]/div/div[1]/div/div/div/div/div/div/div/div[2]/div[2]/div[4]')

    def run(self):
        print('登录成功')
        click(self.wait,'//*[@id="app"]/div/div[1]/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div[3]/div/div/div[5]/div/div/div[3]')
        print('进入健康申报')
        click(self.wait,'//*[@id="col_0_row_8"]')
        print('进入健康申报主界面，正在尝试填表')
        click(self.wait,'//*[@id="col_2_row_14"]/div/div/div/div/div[1]/div/div[1]')
        print('完成 今日上午测量温度')
        click(self.wait,'//*[@id="col_2_row_15"]/div/div/div/div/div[1]/div/div[1]')
        print('完成 今日下午测量温度')
        click(self.wait,'//*[@id="col_4_row_17"]/div/div/div/div/div[1]/div/div[1]')
        print('完成 学生健康码颜色')
        click(self.wait,'//*[@id="col_4_row_18"]/div/div/div/div/div[2]/div/div[1]')
        print('完成 是否属于28天境外返回人员')
        click(self.wait,'//*[@id="col_4_row_19"]/div/div/div/div/div[2]/div/div[1]')
        print('完成 学生及同住家庭成员是否存在确诊/一丝病例')
        click(self.wait,'//*[@id="col_4_row_20"]/div/div/div/div/div[2]/div/div[1]')
        print('完成 学生及同住家庭成员：近14天是否到过中高风险地区')
        click(self.wait,'//*[@id="col_4_row_22"]/div/div/div/div/div[2]/div/div[1]')
        print('完成 学生及同住家庭成员：近14天是否接触中高风险地区返回人员')
        click(self.wait,'//*[@id="col_4_row_24"]/div/div/div/div/div[1]/div/div[1]')
        print('完成 近14天内是否做过核酸检测')
        click(self.wait,'//*[@id="col_4_row_26"]/div/div/div/div/div[2]/div/div[1]')
        print('完成 家人/同住人员是否有出现发热、干咳等症状')
        click(self.wait,'//*[@id="col_4_row_29"]/div/div/div/div/div[2]/div/div[1]')
        print('完成 是否曾离开所居住城市')
        click(self.wait,'//*[@id="col_4_row_32"]/div/div/div/div/div[2]/div/div[1]')
        print('完成 是否有意愿接种新冠疫苗')
        click(self.wait,'//*[@id="col_0_row_35"]/div[2]/div/div/div')
        print('点击提交')
        click(self.wait,'//*[@id="col_0_row_8"]/div[3]')
        print('显示打卡成功界面')
        
    def close(self):
        self.browser.close()
    
    def get_b(self):
        return self.browser
        
try:
    zs=zstu()
    z=zs.get_b()
    zs.login()
    zs.run()
    print('E浙理 打卡成功！')
    z.close()
finally:
    z.close()
    print('E浙理 打卡失败')
    print('请稍后再试，或更新源代码')