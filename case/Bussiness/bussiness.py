# coding=utf-8
from common.Login import Login
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from common.img import screenshot
from common.raiseout import raiseout
from util.log.mylog import Log
class ye_wu():
    def __init__(self):
        L = Login()
        L.login()
        self.d = L.d
        self.d.maximize_window()
        Log().info("点击数据模版管理")
        WebDriverWait(self.d, 60, 1).until(lambda ele: self.d.find_element_by_css_selector('#index > div.second-container > div:nth-child(1) > div > div > ul > li:nth-child(3) > div'))
        self.d.find_element_by_css_selector('#index > div.second-container > div:nth-child(1) > div > div > ul > li:nth-child(3) > div').click()
        sleep(2)
        Log().info("点击业务管理")
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[1]/div/div/ul/li[3]/ul/li[4]').click()
        sleep(1)

    def add(self,name,beizhu):
        Log().info("添加业务")
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[2]/span').click()
        sleep(2)
        Log().info("输入业务名称")
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[4]/div/div[2]/form/div[1]/div/div/input').send_keys(name)
        sleep(2)
        Log().info("选择行业为教育")
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[4]/div/div[2]/form/div[2]/div/div/div[1]/span/span/i').click()
        sleep(1)
        self.d.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[1]').click()
        sleep(1)
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[4]/div/div[2]/form/div[3]/div/div/textarea').send_keys(beizhu)
        sleep(2)
        try:
            Log().info("点击提交")
            self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[4]/div/div[3]/div/button[1]').click()
            WebDriverWait(self.d, 10, 1).until(lambda ele: self.d.find_element_by_css_selector('body > div.el-message.el-message--success > p'))
            t = self.d.find_element_by_css_selector('body > div.el-message.el-message--success > p').text
            Log().info("添加成功")
            self.d.close()
            return t
        except Exception :
            Log().debug("异常原因:场景名不能重复")
            screenshot(self.d,'yewu')
            raiseout()

    def alter(self,name):
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[3]/div[1]/div[3]/table/tbody/tr[2]/td[5]/div/button[1]').click()
        sleep(1)
        Log().info("修改业务名称")
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[4]/div/div[2]/form/div[1]/div/div/input').clear()
        sleep(1)
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[4]/div/div[2]/form/div[1]/div/div/input').send_keys(name)
        sleep(1)
        Log().info("修改行业")
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[4]/div/div[2]/form/div[2]/div/div/div/span/span/i').click()
        sleep(1)
        self.d.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[1]').click()
        Log().info("修改备注")
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[4]/div/div[2]/form/div[3]/div/div/textarea').send_keys("111")
        sleep(1)
        try:
            self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[4]/div/div[3]/div/button[1]').click()
            WebDriverWait(self.d, 10, 1).until(lambda ele: self.d.find_element_by_css_selector('body > div.el-message.el-message--success'))
            t = self.d.find_element_by_css_selector('body > div.el-message.el-message--success').text
            Log().info("修改成功")
            self.d.close()
            return t
        except Exception :
            Log().debug("修改失败")
            screenshot(self.d, 'yewu')
            raiseout()
    def select(self):
        Log().info("输入业务名称")
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[1]/form/div[1]/div/div/input').send_keys(name)

        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[1]/form/div[3]/div/button[2]').click()
        try:
            Log().info("点击提交")
            WebDriverWait(self.d,10,1).until(lambda ele:self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[3]/div[1]/div[3]/table/tbody/tr/td[1]/div'))
            m = self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[3]/div[1]/div[3]/table/tbody/tr/td[1]/div').text
            Log().info("查找成功")
            self.d.close()
            return m
        except Exception :
            Log().debug("异常原因:未找到该元素")
            screenshot(self.d, 'yewu')
            raiseout()

    def delete(self):
        Log().info("点击删除第3条数据]")
        WebDriverWait(self.d, 60, 1).until(lambda ele:self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[3]/div[1]/div[3]/table/tbody/tr[3]/td[5]/div/button[2]'))
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[3]/div[1]/div[3]/table/tbody/tr[3]/td[5]/div/button[2]').click()
        sleep(1)
        Log().info("确认删除")
        try:
            self.d.find_element_by_xpath('/html/body/div[2]/div/div[3]/button[2]').click()
            WebDriverWait(self.d, 60, 1).until(lambda ele: self.d.find_element_by_css_selector('body > div.el-message.el-message--success'))
            m = self.d.find_element_by_css_selector("body > div.el-message.el-message--success").text
            Log().info("删除成功")
            self.d.close()
            return m
        except Exception :
            self.d.find_element_by_xpath('/html/body/div[2]/div/div[3]/button/span').click()
            Log().debug("异常原因:场景正在被使用无法删除")
            screenshot(self.d, 'yewu')
            raiseout()
            self.d.close()
