# coding=utf-8
from common.Login import Login
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from common.img import screenshot
from common.raiseout import raiseout
from util.log.mylog import Log

class zu_hu():
    def __init__(self):
        L = Login()
        L.login()
        self.d = L.d
        self.d.maximize_window()

    def add(self,name,xm,phone,beizhu):
        Log().info("点击添加租户")
        WebDriverWait(self.d, 30, 0.5).until(lambda ele: self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[2]/div[1]/span'))
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[2]/div[1]/span').click()
        sleep(1)
        Log().info("输入租户名称")
        WebDriverWait(self.d, 30, 0.5).until(lambda ele: self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/div[2]/form/div[1]/div/div/input'))
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/div[2]/form/div[1]/div/div/input').send_keys(name)
        sleep(1)
        Log().info("选择等级L3")
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/div[2]/form/div[2]/div/div/label[3]/span[1]/span').click()
        sleep(1)
        Log().info("选择行业教育")
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/div[2]/form/div[3]/div/div/div[1]/span/span/i').click()
        sleep(1)
        self.d.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[2]').click()
        sleep(1)
        Log().info("选择省份上海")
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/div[2]/form/div[4]/div/div/div[1]/input').click()
        sleep(1)
        self.d.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/ul/li[3]').click()
        sleep(1)
        Log().info("输入联系人")
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/div[2]/form/div[5]/div/div[1]/input').send_keys(xm)
        sleep(1)
        Log().info("输入联系电话")
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/div[2]/form/div[6]/div/div[1]/input').send_keys(phone)
        sleep(1)
        Log().info("输入备注")
        self.d.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/div[2]/form/div[7]/div/div/textarea').send_keys(beizhu)
        sleep(1)
        try:
            Log().info("点击提交")
            self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/div[3]/div/button[1]/span').click()
            sleep(1)
            WebDriverWait(self.d, 10, 1).until(lambda ele: self.d.find_element_by_css_selector('body > div.el-message.el-message--success > p'))
            t = self.d.find_element_by_css_selector('body > div.el-message.el-message--success > p').text
            Log().info("添加成功")
            self.d.quit()
            return t
        except Exception :
            Log().debug("异常原因:联系人手机号码不能重复")
            screenshot(self.d, 'zuhu')
            raiseout()

    def alter(self,name,xm,phone,beizhu):
        Log().info("点击编辑")
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[2]/td[9]/div/button[1]/i').click()
        sleep(1)
        Log().info("修改租户名称")
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/div[2]/form/div[1]/div/div/input').clear()
        sleep(1)
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/div[2]/form/div[1]/div/div/input').send_keys(name)
        sleep(1)
        Log().info("修改行业")
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/div[2]/form/div[3]/div/div/div/span/span/i').click()
        sleep(1)
        self.d.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[3]').click()
        sleep(1)
        Log().info("修改联系人姓名")
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/div[2]/form/div[5]/div/div/input').clear()
        sleep(1)
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/div[2]/form/div[5]/div/div/input').send_keys(xm)
        sleep(1)
        Log().info("修改电话")
        self.d.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/div[2]/form/div[6]/div/div/input').clear()
        sleep(1)
        self.d.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/div[2]/form/div[6]/div/div/input').send_keys(phone)
        sleep(1)
        Log().info("修改备注")
        self.d.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/div[2]/form/div[7]/div/div/textarea').send_keys(beizhu)
        sleep(1)
        try:
            self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/div[3]/div/button[1]').click()
            sleep(1)
            WebDriverWait(self.d, 10, 1).until(lambda ele: self.d.find_element_by_css_selector('body > div.el-message.el-message--success'))
            t = self.d.find_element_by_css_selector('body > div.el-message.el-message--success').text
            Log().info("修改成功")
            self.d.close()
            return t
        except Exception:
            Log().debug("修改失败")
            screenshot(self.d, 'zuhu')
            raiseout()

    def swith(self):
        Log().info("租户详情页跳转")
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[2]').click()
        sleep(1)
        try:
            m=self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div[2]/button[1]').text
            Log().info("跳转成功")
            self.d.close()
            return m
        except Exception:
            Log().debug("跳转失败")
            screenshot(self.d, 'zuhu')
            raiseout()

    def peizhi_1(self):
        Log().info("点击租户名称")
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[2]/div/a').click()
        sleep(1)
        Log().info("点击专网配置")
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div[2]/button[1]').click()
        sleep(1)
        Log().info("点击引用专网等级模版")
        WebDriverWait(self.d,30,1).until(lambda ele:self.d.find_element_by_css_selector('#index > div.second-container > div.main-wrapper > div > div.tenant-container > div.detail-content > div.content > div.topo > div.network-setting-dialog > div:nth-child(1) > div > div.el-dialog__body > form > div:nth-child(1) > div > button > span'))
        self.d.find_element_by_css_selector('#index > div.second-container > div.main-wrapper > div > div.tenant-container > div.detail-content > div.content > div.topo > div.network-setting-dialog > div:nth-child(1) > div > div.el-dialog__body > form > div:nth-child(1) > div > button > span').click()
        sleep(1)
        Log().info("选择模版")
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div[2]/div[5]/div[2]/div/div[2]/div/div/div[1]/div[2]/div[3]/table/tbody/tr/td[2]/div/label').click()
        sleep(1)
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div[2]/div[5]/div[2]/div/div[2]/div/div/div[3]/div[3]/button[1]').click()
        sleep(1)
        Log().info("添加更多基站ID")
        self.d.find_element_by_css_selector('#index > div.second-container > div.main-wrapper > div > div.tenant-container > div.detail-content > div.content > div.topo > div.network-setting-dialog > div:nth-child(1) > div > div.el-dialog__body > form > div.el-form-item.el-form-item--feedback.is-required > div > button > span').click()
        sleep(1)
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div[2]/div[5]/div[1]/div/div[2]/form/div[2]/div/div[3]/div/input').send_keys("11111")
        sleep(1)
        try:
            Log().info("点击提交")
            self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div[2]/div[5]/div[1]/div/div[3]/div/button[1]/span').click()
            sleep(1)
            WebDriverWait(self.d, 30,1).until(lambda ele: self.d.find_element_by_css_selector('body > div.el-message.el-message--success > p'))
            t = self.d.find_element_by_css_selector('body > div.el-message.el-message--success > p').text
            Log().info("配置成功")
            self.d.close()
            return t
        except Exception :
            Log().debug("配置失败")
            screenshot(self.d, 'zuhu')
            raiseout()

    def peizhi_2(self):
        Log().info("点击租户名称")
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[2]/div/a').click()
        sleep(1)
        Log().info("点击专网配置")
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div[2]/button[1]').click()
        sleep(1)
        Log().info("点击引用模版")
        WebDriverWait(self.d, 60,1).until(lambda ele:self.d.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[2]/div[2]/div[5]/div[1]/div/div[2]/form/div[3]/div/div/div[1]/form/div[3]/div[2]/div/button/span'))
        self.d.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[2]/div[2]/div[5]/div[1]/div/div[2]/form/div[3]/div/div/div[1]/form/div[3]/div[2]/div/button/span').click()
        sleep(1)
        try:
            Log().info("选择模版")
            self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div[2]/div[5]/div[1]/div/div[2]/form/div[3]/div/div/div[2]/div/div[2]/div/div/div[1]/div[2]/div[3]/table/tbody/tr/td[2]/div/label/span/span').click()
            sleep(1)
            self.d.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[2]/div[2]/div[5]/div[1]/div/div[2]/form/div[3]/div/div/div[2]/div/div[2]/div/div/div[3]/div[3]/button[1]').click()
            sleep(1)
            Log().info("选择场景")
            self.d.find_element_by_css_selector('div.el-dialog__footer:nth-child(3) > div:nth-child(1) > button:nth-child(1)').click()
            WebDriverWait(self.d, 30, 1).until(lambda ele: self.d.find_element_by_css_selector('body > div.el-message.el-message--success > p'))
            t = self.d.find_element_by_css_selector('body > div.el-message.el-message--success > p').text
            Log().info("配置成功")
            self.d.close()
            return t
        except Exception :
            Log().debug("配置失败")
            screenshot(self.d, 'zuhu')
            raiseout()

    def zuhu_login(self,name,phone):
        Log().info("租户登录")
        WebDriverWait(self.d, 30, 0.5).until(lambda ele: self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[2]/div[1]/span'))
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[2]/div[1]/span').click()
        sleep(1)
        Log().info("输入租户名称")
        WebDriverWait(self.d, 30, 0.5).until(lambda ele: self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/div[2]/form/div[1]/div/div/input'))
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/div[2]/form/div[1]/div/div/input').send_keys(name)
        sleep(1)
        Log().info("选择等级L3")
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/div[2]/form/div[2]/div/div/label[3]/span[1]/span').click()
        sleep(1)
        Log().info("选择行业教育")
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/div[2]/form/div[3]/div/div/div[1]/span/span/i').click()
        sleep(1)
        self.d.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[2]').click()
        sleep(1)
        Log().info("选择省份上海")
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/div[2]/form/div[4]/div/div/div[1]/input').click()
        sleep(1)
        self.d.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/ul/li[3]').click()
        sleep(1)
        Log().info("输入联系人")
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/div[2]/form/div[5]/div/div[1]/input').send_keys("张三")
        sleep(1)
        Log().info("输入联系电话")
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/div[2]/form/div[6]/div/div[1]/input').send_keys(phone)
        sleep(1)
        Log().info("点击提交")
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/div[3]/div/button[1]/span').click()
        sleep(1)
        ActionChains(self.d).move_to_element(self.d.find_element_by_xpath('/html/body/div[1]/div/div[1]/section/div[2]/div/span/span')).perform()
        sleep(1)
        WebDriverWait(self.d, 10, 1).until(lambda ele: self.d.find_element_by_xpath('/html/body/ul/li'))
        self.d.find_element_by_xpath('/html/body/ul/li').click()
        pwd = phone[-6:]
        Log().info("跳转到专网租户登录页面")
        self.d.get("http://192.168.12.205:9999/login")
        self.d.find_element_by_xpath('//*[@id="app"]/div/div[1]/form/div[1]/div/div/input').send_keys(phone)
        sleep(1)
        self.d.find_element_by_xpath('//*[@id="app"]/div/div[1]/form/div[2]/div/div/input').send_keys(pwd)
        sleep(1)
        try:
            self.d.find_element_by_xpath('//*[@id="app"]/div/div[1]/form/div[3]/div/button').click()
            sleep(1)
            WebDriverWait(self.d,30,1).until(lambda ele:self.d.find_element_by_xpath('//*[@id="index"]/div[1]/section/ul[1]/li'))
            m=self.d.find_element_by_xpath('//*[@id="index"]/div[1]/section/ul[1]/li').text
            Log().info("登录成功")
            self.d.close()
            return m
        except Exception:
            Log().debug("登陆失败")
            screenshot(self.d, 'zuhu')
            raise

    def delete(self):
        Log().info("删除第3个租户数据")
        # self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[2]/ul/li[2]').click()
        # WebDriverWait(self.d,60,1).until(lambda ele: self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[2]/ul/li[2]'))
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[3]/td[9]/div/button[2]').click()
        try:
            Log().info("点击确认")
            self.d.find_element_by_xpath('/html/body/div[2]/div/div[3]/button[2]').click()
            WebDriverWait(self.d, 60, 1).until(lambda ele: self.d.find_element_by_css_selector('body > div.el-message.el-message--success'))
            m = self.d.find_element_by_css_selector("body > div.el-message.el-message--success").text
            Log().info("删除成功")
            self.d.close()
            return m
        except Exception :
            Log().info("异常原因:无法删除")
            screenshot(self.d, 'zhongduan')
            raiseout()

    def state(self):
        Log().info("专网租户详情页跳转")
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[2]/div/a').click()
        sleep(1)
        try:
            WebDriverWait(self.d, 10, 1).until(lambda ele:self.d.find_element_by_css_selector('button.is-plain:nth-child(1)'))
            self.d.find_element_by_css_selector('button.is-plain:nth-child(1)').click()
            sleep(1)
            self.d.find_element_by_xpath('/html/body/div[2]/div/div[3]/button[2]').click()
            WebDriverWait(self.d,30,0.5).until(lambda ele:self.d.find_element_by_xpath('/html/body/div[3]/p'))
            m=self.d.find_element_by_xpath('/html/body/div[3]/p').text
            Log().info("专网配置成功")
            return m
        except Exception :
            Log().debug("专网配置失败")
            screenshot(self.d, 'zhongduan')
            raiseout()

    def download(self):
        Log().info("点击租户名称")
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[2]/div/a').click()
        sleep(1)
        Log().info("点击下载配置工单")
        self.d.find_element_by_css_selector('.el-icon-download').click()
        Log().info("下载成功")


