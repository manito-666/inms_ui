from common.Login import Login
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains

#验证各种角色的退出
class quit():
    def Logout(self):#管理员登录退出
        L = Login()
        L.login()
        self.d = L.d
        ActionChains(self.d).move_to_element(self.d.find_element_by_xpath('/html/body/div[1]/div/div[1]/section/div[2]/div/span/span')).perform()
        sleep(1)
        WebDriverWait(self.d, 10, 1).until(lambda ele: self.d.find_element_by_xpath('/html/body/ul/li'))
        self.d.find_element_by_xpath('/html/body/ul/li').click()
        sleep(1)
        t= self.d.find_element_by_xpath('/html/body/div/div/div[1]/div').text
        print(t)
        if "登录Login" in t:
            print("测试成功")

        # return t

    def Logout_(self,username):#运维运营登录退出
        d = webdriver.Chrome()
        # 打开主界面
        d.maximize_window()
        d.get("http://192.168.12.205/login")
        WebDriverWait(d,60.1).until(lambda ele:d.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/form/div[1]/div/div/input'))
        d.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/form/div[1]/div/div/input').clear()
        sleep(1)
        d.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/form/div[1]/div/div/input').send_keys(username)
        sleep(1)
        d.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/form/div[2]/div/div/input').clear()
        sleep(1)
        pwd=username[-6:]
        d.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/form/div[2]/div/div/input').send_keys(pwd)
        sleep(1)
        # 点击提交登录系统
        d.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/form/div[3]/div/button').click()
        sleep(2)
        ActionChains(d).move_to_element(d.find_element_by_xpath('/html/body/div[1]/div/div[1]/section/div[2]/div/span/span')).perform()
        sleep(1)
        WebDriverWait(d,10,1).until(lambda ele:d.find_element_by_xpath('/html/body/ul/li'))
        d.find_element_by_xpath('/html/body/ul/li').click()
        sleep(1)
        m=d.find_element_by_xpath('/html/body/div/div/div[1]/div').text
        return m

if __name__ == '__main__':
    quit().Logout_("username")