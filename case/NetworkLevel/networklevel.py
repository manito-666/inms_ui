# coding=utf-8
from common.Login import Login
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from common.img import screenshot
from common.raiseout import raiseout
from util.log.mylog import Log

class z_w():
    def __init__(self):
        L = Login()
        L.login()
        self.d = L.d
        self.d.maximize_window()
        Log().info("点击数据模版管理")
        WebDriverWait(self.d, 60, 1).until(lambda ele: self.d.find_element_by_css_selector('#index > div.second-container > div:nth-child(1) > div > div > ul > li:nth-child(3) > div'))
        self.d.find_element_by_css_selector('#index > div.second-container > div:nth-child(1) > div > div > ul > li:nth-child(3) > div').click()
        sleep(2)
        Log().info("点击专网等级模版")
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[1]/div/div/ul/li[3]/ul/li[1]').click()
        sleep(1)

    def add01(self,name,ip,port):
        Log().info("手动输入点击添加模版")
        WebDriverWait(self.d, 30, 0.5).until(lambda ele: self.d.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/div/div[2]/div[2]/div[1]/span'))
        self.d.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/div/div[2]/div[2]/div[1]/span').click()
        sleep(1)
        Log().info("输入模版名称")
        self.d.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/div[2]/form/div[1]/div/div/input').send_keys(name)
        sleep(1)
        Log().info("选择专网等级")
        self.d.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/div[2]/form/div[2]/div/div/label[1]/span[1]/span').click()
        Log().info("选择专网行业")
        self.d.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/div[2]/form/div[3]/div/div/div[1]/span/span/i').click()
        sleep(1)
        self.d.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[1]').click()
        sleep(1)
        Log().info("选择场景")
        self.d.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/div[2]/form/div[4]/div/div/div[1]/form/div[1]/div/div/div[1]/span/span/i').click()
        sleep(1)
        self.d.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/ul/li[1]').click()
        sleep(1)
        Log().info("选择业务")
        self.d.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/div[2]/form/div[4]/div/div/div[1]/form/div[2]/div/div/div/span/span/i').click()
        sleep(1)
        self.d.find_element_by_xpath('/html/body/div[5]/div[1]/div[1]/ul/li[1]').click()
        sleep(1)
        Log().info("选择协议")
        WebDriverWait(self.d, 30,1).until(lambda ele: self.d.find_element_by_xpath(
           '//*[contains(@id,"el-collapse-content")]/div/div[2]/div/div/div[1]/span/span/i'))
        self.d.find_element_by_xpath(
            '//*[contains(@id,"el-collapse-content")]/div/div[2]/div/div/div[1]/span/span/i').click()
        WebDriverWait(self.d, 10, 1).until(
            lambda ele: self.d.find_element_by_xpath('/html/body/div[6]/div[1]/div[1]/ul/li[1]'))
        self.d.find_element_by_xpath('/html/body/div[6]/div[1]/div[1]/ul/li[1]').click()

        Log().info("输入ip")
        WebDriverWait(self.d,60,1).until(lambda ele:self.d.find_element_by_xpath('//*[contains(@id,"el-collapse-content")]/div/div[3]/div/div/div/input'))
        self.d.find_element_by_xpath('//*[contains(@id,"el-collapse-content")]/div/div[3]/div/div/div/input').send_keys(ip)
        sleep(1)
        self.d.find_element_by_xpath('//*[contains(@id,"el-collapse-content")]/div/div[4]/div/div/input').send_keys(ip)
        sleep(1)
        Log().info("输入端口号")
        self.d.find_element_by_xpath('//*[contains(@id,"el-collapse-content")]/div/div[5]/div/div/input').send_keys(port)
        sleep(1)
        self.d.find_element_by_xpath('//*[contains(@id,"el-collapse-content")]/div/div[6]/div/div/input').send_keys(port)
        sleep(1)
        Log().info("输入参数")
        WebDriverWait(self.d,30,1).until(lambda ele:self.d.find_element_by_xpath('//*[contains(@id,"el-collapse-content")]/div/div[8]/div[1]/div/div/div/input'))
        self.d.find_element_by_xpath('//*[contains(@id,"el-collapse-content")]/div/div[8]/div[1]/div/div/div/input').send_keys('1')
        sleep(1)
        self.d.find_element_by_xpath('//*[contains(@id,"el-collapse-content")]/div/div[8]/div[2]/div/div/div/input').send_keys("1")
        sleep(1)
        self.d.find_element_by_xpath('//*[contains(@id,"el-collapse-content")]/div/div[9]/div[1]/div/div/div/input').send_keys("1")
        sleep(1)
        self.d.find_element_by_xpath('//*[contains(@id,"el-collapse-content")]/div/div[9]/div[2]/div/div/div/input').send_keys("1")
        sleep(1)
        Log().info("输入API_PCI")
        self.d.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/div[2]/form/div[4]/div/div/div[1]/form/div[3]/div[2]/div/div[10]/div[1]/div/div/span[3]/span').click()
        sleep(1)
        self.d.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/div[2]/form/div[4]/div/div/div[1]/form/div[3]/div[2]/div/div[10]/div[2]/div/div/span[3]/span').click()
        sleep(1)
        Log().info("输入APR_PL")
        self.d.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/div[2]/form/div[4]/div/div/div[1]/form/div[3]/div[2]/div/div[11]/div/div/div/input').send_keys("1")
        sleep(1)
        try:
            Log().info("点击提交")
            self.d.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/div[3]/div/button[1]').click()
            WebDriverWait(self.d, 10, 1).until(lambda ele: self.d.find_element_by_css_selector('body > div.el-message.el-message--success > p'))
            t = self.d.find_element_by_css_selector('body > div.el-message.el-message--success > p').text
            Log().info("添加成功")
            self.d.close()
            return t
        except Exception :
            Log().debug("异常原因:专网等级模版名称不能重复")
            screenshot(self.d, 'zhuanwang')
            raiseout()


    def add02(self,name):
        Log().info("引用模版点击添加模版")
        WebDriverWait(self.d, 30, 0.5).until(lambda ele: self.d.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/div/div[2]/div[2]/div[1]/span'))
        self.d.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/div/div[2]/div[2]/div[1]/span').click()

        Log().info("输入模版名称")
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[3]/div/div[2]/form/div[1]/div/div/input').send_keys(name)
        Log().info("选择专网等级")
        ele= self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[3]/div/div[2]/form/div[2]/div/div/label[1]/span[1]/span')
        self.d.execute_script("arguments[0].scrollIntoView(false);", ele)
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[3]/div/div[2]/form/div[2]/div/div/label[1]/span[1]/span').click()
        sleep(1)
        Log().info("选择专网行业")
        self.d.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/div[2]/form/div[3]/div/div/div[1]/span/span/i').click()
        sleep(1)
        self.d.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[1]').click()
        sleep(1)
        Log().info("点击引用模版")
        WebDriverWait(self.d,60,1).until(lambda ele:self.d.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/div[2]/form/div[4]/div/div/div[1]/form/div[3]/div[2]/div/button'))
        self.d.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/div[2]/form/div[4]/div/div/div[1]/form/div[3]/div[2]/div/button').click()
        sleep(1)
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[3]/div/div[2]/form/div[4]/div/div/div[2]/div/div[2]/div/div/div[1]/div[2]/div[3]/table/tbody/tr[1]/td[1]/div').click()
        sleep(1)
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[3]/div/div[2]/form/div[4]/div/div/div[2]/div/div[2]/div/div/div[3]/div[3]/button[1]').click()
        sleep(1)
        Log().info("选择场景")
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[3]/div/div[2]/form/div[4]/div/div/div[1]/form/div[1]/div/div[1]/div/span/span/i').click()
        sleep(1)
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[3]/div/div[2]/form/div[4]/div/div/div[1]/form/div[1]/div/div[1]/div/span/span/i').click()
        sleep(1)
        self.d.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/ul/li[2]').click()
        sleep(1)
        Log().info("选择业务")
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[3]/div/div[2]/form/div[4]/div/div/div[1]/form/div[2]/div/div[1]/div[1]/span/span/i').click()
        sleep(1)
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[3]/div/div[2]/form/div[4]/div/div/div[1]/form/div[2]/div/div[1]/div[1]/span/span/i').click()
        sleep(1)
        self.d.find_element_by_xpath('/html/body/div[5]/div[1]/div[1]/ul/li[1]').click()
        sleep(1)
        try:
            Log().info("点击提交")
            WebDriverWait(self.d,30,1).until(lambda ele:self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[3]/div/div[3]/div/button[1]'))
            self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[3]/div/div[3]/div/button[1]').click()
            WebDriverWait(self.d, 10, 1).until(lambda ele: self.d.find_element_by_css_selector('body > div.el-message.el-message--success > p'))
            t = self.d.find_element_by_css_selector('body > div.el-message.el-message--success > p').text
            Log().info("添加成功")
            self.d.close()
            return t
        except Exception :
            Log().debug("添加失败")
            screenshot(self.d, 'zhuanwang')
            raiseout()

    def select_1(self,name):
        Log().info("输入模版名称查找")
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[1]/form/div[1]/div/div/input').send_keys(name)
        sleep(1)
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[1]/form/div[4]/div/button[2]').click()
        sleep(1)
        try:
            m=self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div[3]/table/tbody/tr/td[6]/div/button[1]').text
            Log().info("查找成功")
            self.d.close()
            return m
        except Exception:
            Log().debug("查找失败")
            screenshot(self.d, 'zhuanwang')
            raiseout()

    def select_2(self):
        Log().info("选择行业为船舶--等级L1")
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[1]/form/div[2]/div/div/div/span/span/i').click()
        sleep(1)
        WebDriverWait(self.d,30,0.5).until(lambda ele:self.d.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/ul/li[3]'))
        self.d.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/ul/li[3]').click()
        sleep(1)
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[1]/form/div[3]/div/div/div/span/span/i').click()
        sleep(1)
        WebDriverWait(self.d,10,1).until(lambda ele:self.d.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[1]'))
        self.d.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[1]').click()
        sleep(1)
        try:
            Log().info("点击提交")
            self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[1]/form/div[4]/div/button[2]').click()
            sleep(1)
            m=self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div[3]/div/span').text
            Log().info("查找成功,该元素不存在")
            self.d.close()
            return m
        except Exception :
            Log().debug("异常原因:该元素存在")
            screenshot(self.d, 'zhuanwang')
            raiseout()

    def delete(self):
        Log().info("删除第3条数据")
        # WebDriverWait(self.d, 60, 1).until(lambda ele: self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[2]/ul/li[2]'))
        # self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[2]/ul/li[2]').click()
        # sleep(2)
        WebDriverWait(self.d, 60, 1).until(lambda ele: self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[3]/td[6]/div/button[3]'))
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[3]/td[6]/div/button[3]').click()
        sleep(1)
        try:
            Log().info("点击删除")
            self.d.find_element_by_css_selector('body > div.el-message-box__wrapper > div > div.el-message-box__btns > button.el-button.el-button--default.el-button--small.el-button--primary > span').click()
            WebDriverWait(self.d, 60, 1).until(lambda ele: self.d.find_element_by_css_selector('body > div.el-message.el-message--success'))
            m = self.d.find_element_by_css_selector("body > div.el-message.el-message--success").text
            Log().info("删除成功")
            self.d.close()
            return m
        except Exception :
            Log().debug("异常原因:专网等级模版正在被使用无法删除")
            screenshot(self.d, 'zhuanwang')
            raiseout()



