from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

class Login:
    def login(self):       
        self.options = Options()
        self.options.add_argument('--no-sandbox')
        self.options.add_argument('--disable-dev-shm-usage')
        self.options.add_argument('--headless')
        # 实例化浏览器
        self.d= webdriver.Chrome(chrome_options=self.options)
        # 打开登录界面
        self.d.get("http://localhost")
        # WebDriverWait(self.d,60.1).until(lambda ele:self.d.find_element_by_xpath('//*[@id="app"]/div/div[1]/form/div[1]/div/div/input'))
        # self.d.find_element_by_xpath('//*[@id="app"]/div/div[1]/form/div[1]/div/div/input').clear()
        # sleep(1)
        # self.d.find_element_by_xpath('//*[@id="app"]/div/div[1]/form/div[1]/div/div/input').send_keys("admin")
        # sleep(1)
        # self.d.find_element_by_xpath('//*[@id="app"]/div/div[1]/form/div[2]/div/div/input').clear()
        # sleep(1)
        # self.d.find_element_by_xpath('//*[@id="app"]/div/div[1]/form/div[2]/div/div/input').send_keys('admin')
        # sleep(1)
        #点击提交登录系统
        self.d.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/form/div[3]/div/button').click()
        sleep(2
)
