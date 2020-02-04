# coding=utf-8
from common.Login import Login
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from common.img import screenshot
from common.raiseout import raiseout
from util.log.mylog import Log

class qie_pian():
    def __init__(self):
        L = Login()
        L.login()
        self.d = L.d
        self.d.maximize_window()
        sleep(1)
        Log().info("点击数据模版管理")
        WebDriverWait(self.d, 60, 1).until(lambda ele: self.d.find_element_by_css_selector('#index > div.second-container > div:nth-child(1) > div > div > ul > li:nth-child(3) > div'))
        self.d.find_element_by_css_selector('#index > div.second-container > div:nth-child(1) > div > div > ul > li:nth-child(3) > div').click()
        sleep(2)
        Log().info("点击切片模版")
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[1]/div/div/ul/li[3]/ul/li[2]').click()
        sleep(1)

    def add(self,name,ip,port):
        self.d.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/div/div[2]/div[2]/div[1]/span').click()
        sleep(1)
        self.d.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/div[2]/form/div[1]/div/div/input').send_keys(name)
        sleep(2)
        Log().info("选择等级L4")
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[3]/div/div[2]/form/div[2]/div/div/label[4]/span[1]/span').click()
        sleep(1)
        Log().info("选择行业为医疗")
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[3]/div/div[2]/form/div[3]/div/div/div/span/span/i').click()
        sleep(1)
        self.d.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[1]').click()
        sleep(1)
        Log().info("选择场景")
        sleep(1)
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[3]/div/div[2]/form/div[4]/div/div/div/span/span/i').click()
        sleep(1)
        WebDriverWait(self.d,10,1).until(lambda ele:self.d.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/ul/li[1]'))
        self.d.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/ul/li[1]').click()
        sleep(1)
        Log().info("选择业务")
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[3]/div/div[2]/form/div[5]/div/div/div/span/span/i').click()
        sleep(1)
        self.d.find_element_by_xpath('/html/body/div[5]/div[1]/div[1]/ul/li').click()
        sleep(1)
        Log().info("选择协议")
        WebDriverWait(self.d,60,1).until(lambda ele:self.d.find_element_by_css_selector('#index > div.second-container > div.main-wrapper > div > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(7) > div > div > div.el-input.el-input--suffix > span > span > i'))
        self.d.find_element_by_css_selector('#index > div.second-container > div.main-wrapper > div > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(7) > div > div > div.el-input.el-input--suffix > span > span > i').click()
        sleep(1)
        WebDriverWait(self.d,10,1).until(lambda ele:self.d.find_element_by_xpath('/html/body/div[6]/div[1]/div[1]/ul/li[1]'))
        self.d.find_element_by_xpath('/html/body/div[6]/div[1]/div[1]/ul/li[1]').click()
        sleep(1)
        Log().info("输入ip")
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[3]/div/div[2]/form/div[8]/div/div/input').send_keys(ip)
        sleep(1)
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[3]/div/div[2]/form/div[9]/div/div/input').send_keys(ip)
        sleep(1)
        Log().info("输入端口号")
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[3]/div/div[2]/form/div[10]/div/div[1]/input').send_keys(port)
        sleep(1)
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[3]/div/div[2]/form/div[11]/div/div/input').send_keys(port)
        sleep(1)
        Log().info("输入参数")
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[3]/div/div[2]/form/div[13]/div[1]/div/div/div/input').send_keys('1')
        sleep(1)
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[3]/div/div[2]/form/div[13]/div[2]/div/div/div/input').send_keys("1")
        sleep(1)
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[3]/div/div[2]/form/div[14]/div[1]/div/div/div/input').send_keys("1")
        sleep(1)
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[3]/div/div[2]/form/div[14]/div[2]/div/div/div/input').send_keys("1")
        sleep(1)
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[3]/div/div[2]/form/div[15]/div[1]/div/div/span[3]/span').click()
        sleep(1)
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[3]/div/div[2]/form/div[15]/div[2]/div/div/span[3]/span').click()
        sleep(1)
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[3]/div/div[2]/form/div[16]/div/div/div/input').send_keys("1")
        sleep(1)
        try:
            self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[3]/div/div[3]/div/button[1]').click()
            WebDriverWait(self.d, 10, 1).until(lambda ele: self.d.find_element_by_css_selector('body > div.el-message.el-message--success > p'))
            t = self.d.find_element_by_css_selector('body > div.el-message.el-message--success > p').text
            Log().info("添加成功")
            self.d.close()
            return t
        except Exception :
            Log().debug("异常原因:切片模版名称不能重复")
            screenshot(self.d, 'qiepian')
            raiseout()

    def alter(self):
        Log().info("点击编辑")
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div[3]/table/tbody/tr/td[7]/div/button[2]').click()
        sleep(1)
        Log().info("修改模版名称")
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[3]/div/div[2]/form/div[1]/div/div/input').clear()
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[3]/div/div[2]/form/div[1]/div/div/input').send_keys("切片模版一")
        sleep(1)
        Log().info("修改等级")
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[3]/div/div[2]/form/div[2]/div/div/label[2]/span[1]/span').click()
        sleep(1)
        try:
            Log().info("点击确认")
            self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[3]/div/div[3]/div/button[1]').click()
            WebDriverWait(self.d, 10, 1).until(lambda ele: self.d.find_element_by_css_selector('body > div.el-message.el-message--success'))
            t = self.d.find_element_by_css_selector('body > div.el-message.el-message--success').text
            Log().info("修改成功")
            self.d.close()
            return t
        except Exception :
            Log().debug("修改失败")
            screenshot(self.d, 'qiepian')
            raiseout()

    def select1(self,name):
        Log().info("根据模版名称查询")
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[1]/form/div[1]/div/div/input').send_keys(name)
        sleep(1)
        try:
            self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[1]/form/div[6]/div/button[2]').click()
            m=self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div[3]/table/tbody/tr/td[7]/div/button[2]').text
            Log().info("查询成功")
            self.d.close()
            return m
        except Exception :
            Log().debug("异常原因:未找到该元素")
            screenshot(self.d, 'qiepian')
            raiseout()

    def select2(self):
        Log().info("根据行业等级场景查询")
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[1]/form/div[2]/div/div/div/span/span/i').click()
        sleep(1)
        Log().info("选择行业")
        self.d.find_element_by_css_selector('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(2)').click()
        sleep(1)
        Log().info("选择等级")
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[1]/form/div[3]/div/div/div[1]/span/span/i').click()
        sleep(1)
        self.d.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[1]').click()

        try:
            self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[1]/form/div[6]/div/button[2]').click()
            sleep(1)
            m=self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[7]/div/button[2]').text
            Log().info("查询成功")
            self.d.close()
            return m
        except Exception :
            Log().debug("异常原因:未找到该元素")
            screenshot(self.d, 'qiepian')
            raiseout()

    def delete(self):
        Log().info("删除首页第4个数据")
        # WebDriverWait(self.d, 10, 1).until(lambda ele: self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[2]/td[7]/div/button[3]/span'))
        # self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[7]/div/button[3]/span').click()
        WebDriverWait(self.d, 10, 1).until(lambda ele: self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[4]/td[7]/div/button[3]'))
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[4]/td[7]/div/button[3]').click()
        try:
            Log().info("点击确认")
            self.d.find_element_by_xpath('/html/body/div[6]/div/div[3]/button[2]').click()
            WebDriverWait(self.d, 60, 1).until(lambda ele: self.d.find_element_by_css_selector('body > div.el-message.el-message--success'))
            m = self.d.find_element_by_css_selector("body > div.el-message.el-message--success").text
            Log().info("删除成功")
            self.d.close()
            return m
        except Exception :
            Log().debug("异常原因:切片模版正在被使用无法删除")
            screenshot(self.d, 'qiepian')
            raiseout()
