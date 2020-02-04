# coding=utf-8
from common.Login import Login
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from common.img import screenshot
from common.raiseout import raiseout
from util.log.mylog import Log

class CJ():
    def __init__(self):
        L = Login()
        L.login()
        self.d = L.d
        self.d.maximize_window()
        Log().info("点击数据模版管理")
        WebDriverWait(self.d, 60, 1).until(lambda ele: self.d.find_element_by_css_selector('#index > div.second-container > div:nth-child(1) > div > div > ul > li:nth-child(3) > div'))
        self.d.find_element_by_css_selector('#index > div.second-container > div:nth-child(1) > div > div > ul > li:nth-child(3) > div').click()
        sleep(2)
        Log().info("点击场景")
        self.d.find_element_by_css_selector("#index > div.second-container > div:nth-child(1) > div > div > ul > li:nth-child(3) > ul > li:nth-child(3)").click()

    def add(self,name,beizhu):
        Log().info("添加场景")
        WebDriverWait(self.d,10,1).until(lambda ele:self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[2]/span'))
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[2]/span').click()
        Log().info("输入场景名字")
        self.d.find_element_by_xpath( '//*[@id="index"]/div[2]/div[2]/div/div[2]/div[4]/div/div[2]/form/div[1]/div/div/input').send_keys(name)
        sleep(1)
        Log().info("选择行业")
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[4]/div/div[2]/form/div[2]/div/div/div[1]/span/span/i').click()
        sleep(1)
        self.d.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[2]').click()
        sleep(1)
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[4]/div/div[2]/form/div[3]/div/div/textarea').send_keys(beizhu)
        Log().info("点击提交")
        try:
            self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[4]/div/div[3]/div/button[1]').click()
            WebDriverWait(self.d, 10, 1).until(lambda ele: self.d.find_element_by_css_selector('body > div.el-message.el-message--success > p'))
            t = self.d.find_element_by_css_selector('body > div.el-message.el-message--success > p').text
            Log().info("添加成功")
            self.d.close()
            return t
        except Exception :
            Log().debug("异常原因:场景名不能重复")
            screenshot(self.d,'changjing')
            raiseout()

    def alter(self,name):
        Log().info("点击编辑")
        WebDriverWait(self.d,10,1).until(lambda ele:self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[3]/div[1]/div[3]/table/tbody/tr[2]/td[5]/div/button[1]'))
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[3]/div[1]/div[3]/table/tbody/tr[2]/td[5]/div/button[1]').click()
        sleep(2)
        Log().info("修改场景名称")
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[4]/div/div[2]/form/div[1]/div/div/input').clear()
        sleep(1)
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[4]/div/div[2]/form/div[1]/div/div/input').send_keys(name)
        sleep(1)
        Log().info("修改备注")
        self.d.find_element_by_xpath(
            '//*[@id="index"]/div[2]/div[2]/div/div[2]/div[4]/div/div[2]/form/div[3]/div/div/textarea').clear()
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[4]/div/div[2]/form/div[3]/div/div/textarea').send_keys("自动化测试")
        sleep(1)
        try:
            Log().info("点击提交")
            self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[4]/div/div[3]/div/button[1]').click()
            WebDriverWait(self.d, 10, 1).until(lambda ele: self.d.find_element_by_css_selector('body > div.el-message.el-message--success'))
            t = self.d.find_element_by_css_selector('body > div.el-message.el-message--success').text
            Log().info("修改成功")
            self.d.close()
            return t
        except Exception :
            Log().debug("修改失败")
            screenshot(self.d, 'changjing')
            raiseout()

    def select_cj(self,name):
        Log().info("输入场景名称进行查找")
        WebDriverWait(self.d,10,1).until(lambda ele:self.d.find_element_by_css_selector("#index > div.second-container > div.main-wrapper > div > div:nth-child(2) > div.common-search > form > div:nth-child(1) > div > div > input"))
        self.d.find_element_by_css_selector("#index > div.second-container > div.main-wrapper > div > div:nth-child(2) > div.common-search > form > div:nth-child(1) > div > div > input").send_keys(name)
        sleep(1)
        try:
            self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[1]/form/div[3]/div/button[2]').click()
            sleep(1)
            m = self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[3]/div[1]/div[3]/table/tbody/tr[1]/td[5]/div/button[1]').text
            Log().info("查找成功")
            self.d.close()
            return m
        except Exception :
            Log().debug("异常原因:未找到该元素")
            screenshot(self.d,'changjing')
            raiseout()

    def select_hy(self):
        Log().info("选择行业进行查询")
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[1]/form/div[2]/div/div/div/span/span/i').click()
        sleep(2)
        self.d.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/ul/li[1]').click()
        sleep(1)
        try:
            self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[1]/form/div[3]/div/button[2]').click()
            sleep(1)
            m = self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[3]/div[1]/div[3]/table/tbody/tr[1]/td[5]/div/button[1]').text
            Log().info("查询成功")
            self.d.close()
            return m
        except Exception :
            Log().debug("异常原因:未找到该元素")
            screenshot(self.d, 'changjing')
            raiseout()

    def delete(self):
        Log().info("选择第3条数据删除")
        #第二页
        # WebDriverWait(self.d, 60, 1).until(lambda ele: self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[3]/div[2]/ul/li[2]'))
        # self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[3]/div[2]/ul/li[2]').click()
        # sleep(2)
        Log().info("点击删除")
        WebDriverWait(self.d, 60, 1).until(lambda ele:self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[3]/div[1]/div[3]/table/tbody/tr[3]/td[5]/div/button[2]'))
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[3]/div[1]/div[3]/table/tbody/tr[3]/td[5]/div/button[2]').click()
        sleep(1)
        try:
            Log().info("点击确认")
            self.d.find_element_by_xpath('/html/body/div[2]/div/div[3]/button[2]').click()
            WebDriverWait(self.d, 60, 1).until(lambda ele: self.d.find_element_by_css_selector('body > div.el-message.el-message--success'))
            m = self.d.find_element_by_css_selector("body > div.el-message.el-message--success").text
            Log().info("删除成功")
            self.d.close()
            return m
        except Exception :
            Log().debug("异常原因:场景正在被使用无法删除")
            screenshot(self.d, 'changjing')
            raiseout()
