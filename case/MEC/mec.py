from common.Login import Login
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from common.img import screenshot
from common.raiseout import raiseout
from util.log.mylog import Log

class M_ec():
    def __init__(self):
        L = Login()
        L.login()
        self.d = L.d
        Log().info("点击MEC管理")
        WebDriverWait(self.d, 60, 1).until(lambda ele: self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[1]/div/div/ul/li[1]/ul/li[3]'))
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[1]/div/div/ul/li[1]/ul/li[3]').click()
        sleep(1)

    def add(self,url):
        Log().info("点击添加mec")
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[2]/div[1]/span').click()
        sleep(1)
        try:
            Log().info("选择租户")
            self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/div[2]/form/div[1]/div/div/div/span/span/i').click()
            sleep(2)
            WebDriverWait(self.d,30,0.5).until(lambda ele:self.d.find_element_by_xpath('/html/body/div[5]/div[1]/div[1]/ul/li[2]'))
            self.d.find_element_by_xpath('/html/body/div[5]/div[1]/div[1]/ul/li[2]').click()
            sleep(1)
            Log().info("选择厂商")
            self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/div[2]/form/div[2]/div/div/div[1]/span/span/i').click()
            sleep(1)
            self.d.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/ul/li[4]').click()
            sleep(1)
            Log().info("输入url")
            self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/div[2]/form/div[3]/div/div[1]/input').send_keys(url)
            sleep(1)
            Log().info("点击确认")
            self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/div[3]/div/button[1]').click()
            WebDriverWait(self.d, 10, 1).until(lambda ele: self.d.find_element_by_css_selector('body > div.el-message.el-message--success'))
            t = self.d.find_element_by_css_selector('body > div.el-message.el-message--success').text
            Log().info("添加成功")
            self.d.close()
            return t
        except Exception as msg:
            Log().debug("异常原因:该租户已添加mec且租户只能添加一个")
            screenshot(self.d, 'mec')
            raiseout()


    def alter(self):
        Log().info("点击编辑")
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[2]/td[5]/div/button[1]').click()
        sleep(1)
        Log().info("修改url")
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/div[2]/form/div[3]/div/div/input').clear()
        sleep(1)
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/div[2]/form/div[3]/div/div/input').send_keys("10.7.154.12")
        sleep(1)
        try:
            self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/div[3]/div/button[1]').click()
            WebDriverWait(self.d, 10, 1).until(lambda ele: self.d.find_element_by_css_selector('body > div.el-message.el-message--success'))
            t = self.d.find_element_by_css_selector('body > div.el-message.el-message--success').text
            Log().info("修改成功")
            self.d.close()
            return t
        except Exception :
            Log().debug("修改失败")
            screenshot(self.d, 'mec')
            raiseout()

    def select(self):
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[1]/form/div[1]/div/div/div/span/span/i').click()
        sleep(1)
        Log().info("选取首个专网租户")
        WebDriverWait(self.d,30,1).until(lambda ele:self.d.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/ul/li[3]'))
        self.d.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/ul/li[3]').click()
        WebDriverWait(self.d,30,1).until(lambda ele:self.d.find_element_by_xpath(
           '/html/body/div[4]/div[1]/div[1]/ul/li[2]/span'))
        self.d.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/ul/li[2]/span').click()
        sleep(1)
        Log().info("选取厂商")
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[1]/form/div[2]/div/div/div/span/span/i').click()
        sleep(1)
        self.d.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[4]').click()
        try:
            m=self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div[3]/table/tbody/tr/td[5]/div/button[1]').text
            Log().info("查询成功")
            self.d.close()
            return m
        except Exception :
            Log().info("查询失败")
            screenshot(self.d, 'mec')
            raiseout()

    def delete(self):
        Log().info("删除第二页首个数据")
        WebDriverWait(self.d, 60, 1).until(lambda ele: self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[2]/ul/li[2]'))
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[2]/ul/li[2]').click()
        sleep(2)
        Log().info("点击删除")
        WebDriverWait(self.d, 60, 1).until(lambda ele: self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[5]/div/button[2]'))
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[5]/div/button[2]').click()
        sleep(1)
        try:
            self.d.find_element_by_css_selector('body > div.el-message-box__wrapper > div > div.el-message-box__btns > button.el-button.el-button--default.el-button--small.el-button--primary > span').click()
            WebDriverWait(self.d, 60, 1).until(lambda ele: self.d.find_element_by_css_selector('body > div.el-message.el-message--success'))
            m = self.d.find_element_by_css_selector("body > div.el-message.el-message--success").text
            Log().info("删除成功")
            self.d.close()
            return m
        except Exception :
            Log().debug("删除失败")
            screenshot(self.d, 'mec')
            raiseout()




