from common.Login import Login
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from common.img import screenshot
from common.raiseout import raiseout
from util.log.mylog import Log
class system():
    def __init__(self):
        L = Login()
        L.login()
        self.d = L.d
        Log().info("点击系统功能")
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[1]/div/div/ul/li[4]/div/i[2]').click()
        sleep(1)
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[1]/div/div/ul/li[4]/ul/li').click()
        sleep(1)

    def add(self,username,beizhu):
        Log().info("点击新建")
        self.d.find_element_by_css_selector("#index > div.second-container > div.main-wrapper > div > div:nth-child(2) > div.add-new > span").click()
        sleep(1)
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[4]/div/div[2]/form/div[1]/div/div/input').send_keys(username)
        sleep(1)
        Log().info("选择运维角色")
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[4]/div/div[2]/form/div[2]/div/div[1]/div/span/span/i').click()
        sleep(1)
        self.d.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[1]').click()
        sleep(1)
        Log().info("输入备注")
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[4]/div/div[2]/form/div[3]/div/div/textarea').send_keys(beizhu)
        sleep(1)
        try:
            Log().info("点击提交")
            self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[4]/div/div[3]/div/button[1]').click()
            WebDriverWait(self.d, 10, 1).until(lambda ele: self.d.find_element_by_css_selector('body > div.el-message.el-message--success > p'))
            t = self.d.find_element_by_css_selector('body > div.el-message.el-message--success > p').text
            Log().info("新建用户成功")
            self.d.close()
            return t
        except Exception :
            Log().debug("异常原因:用户已存在")
            screenshot(self.d, 'xitong')
            raiseout()


    def login_yw(self,name):
        Log().info("新建运维人员户登录系统")
        self.d.find_element_by_css_selector(
            "#index > div.second-container > div.main-wrapper > div > div:nth-child(2) > div.add-new > span").click()
        sleep(1)
        self.d.find_element_by_xpath(
            '//*[@id="index"]/div[2]/div[2]/div/div[2]/div[4]/div/div[2]/form/div[1]/div/div/input').send_keys(name)
        sleep(1)
        Log().info("选择运维角色")
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[4]/div/div[2]/form/div[2]/div/div[1]/div/span/span/i').click()
        sleep(1)
        self.d.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[1]').click()
        sleep(1)
        Log().info("输入备注")
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[4]/div/div[2]/form/div[3]/div/div/textarea').send_keys("运维人员")
        sleep(1)
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[4]/div/div[3]/div/button[1]').click()
        sleep(1)
        Log().info("退出系统")
        ActionChains(self.d).move_to_element(self.d.find_element_by_xpath('/html/body/div[1]/div/div[1]/section/div[2]/div/span/span')).perform()
        sleep(1)
        WebDriverWait(self.d,10,1).until(lambda ele:self.d.find_element_by_xpath('/html/body/ul/li'))
        self.d.find_element_by_xpath('/html/body/ul/li').click()
        pwd=name[-6:]
        Log().info("输入用户名")
        self.d.find_element_by_xpath('/html/body/div/div/div[1]/form/div[1]/div/div/input').clear()
        sleep(1)
        self.d.find_element_by_xpath('/html/body/div/div/div[1]/form/div[1]/div/div/input').send_keys(name)
        sleep(1)
        Log().info("输入密码")
        self.d.find_element_by_xpath('/html/body/div/div/div[1]/form/div[2]/div/div/input').clear()
        sleep(1)
        self.d.find_element_by_xpath('/html/body/div/div/div[1]/form/div[2]/div/div/input').send_keys(pwd)
        sleep(1)
        try:
            self.d.find_element_by_xpath('/html/body/div/div/div[1]/form/div[3]/div/button').click()
            sleep(2)
            m=self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[1]/div/div/ul/li[1]/div').text
            Log().info("登录成功")
            self.d.close()
            return m
        except Exception :
            Log().debug("异常原因:用户已存在")
            screenshot(self.d, 'xitong')
            raiseout()

    def login_yy(self,name):
        Log().info("新建运营人员登录")
        self.d.find_element_by_css_selector("#index > div.second-container > div.main-wrapper > div > div:nth-child(2) > div.add-new > span").click()
        sleep(1)
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[4]/div/div[2]/form/div[1]/div/div/input').send_keys(name)
        sleep(1)
        Log().info("选择运营角色")
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[4]/div/div[2]/form/div[2]/div/div[1]/div/span/span/i').click()
        sleep(1)
        self.d.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[2]').click()
        sleep(1)
        Log().info("输入备注")
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[4]/div/div[2]/form/div[3]/div/div/textarea').send_keys("运营人员")
        sleep(1)
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[4]/div/div[3]/div/button[1]').click()
        sleep(1)
        Log().info("退出系统")
        ActionChains(self.d).move_to_element(self.d.find_element_by_xpath('/html/body/div[1]/div/div[1]/section/div[2]/div/span/span')).perform()
        sleep(1)
        WebDriverWait(self.d,10,1).until(lambda ele:self.d.find_element_by_xpath('/html/body/ul/li'))
        self.d.find_element_by_xpath('/html/body/ul/li').click()
        pwd=name[-6:]
        Log().info("输入用户名")
        self.d.find_element_by_xpath('/html/body/div/div/div[1]/form/div[1]/div/div/input').clear()
        sleep(1)
        self.d.find_element_by_xpath('/html/body/div/div/div[1]/form/div[1]/div/div/input').send_keys(name)
        sleep(1)
        Log().info("输入密码")
        self.d.find_element_by_xpath('/html/body/div/div/div[1]/form/div[2]/div/div/input').clear()
        sleep(1)
        self.d.find_element_by_xpath('/html/body/div/div/div[1]/form/div[2]/div/div/input').send_keys(pwd)
        sleep(1)
        try:
            Log().info("点击确认")
            self.d.find_element_by_xpath('/html/body/div/div/div[1]/form/div[3]/div/button').click()
            sleep(2)
            m=self.d.find_element_by_xpath('/html/body/div/div/div[2]/div[1]/div/div/ul/li/ul/li').text
            Log().info("登录成功")
            self.d.close()
            return m
        except Exception :
            Log().debug("异常原因:用户已存在")
            screenshot(self.d, 'xitong')
            raiseout()

    def alter(self,name,beizhu):
        Log().info("选择首个元素")
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[3]/div[1]/div[3]/table/tbody/tr[1]/td[5]/div/button[1]').click()
        sleep(1)
        Log().info("修改用户名")
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[4]/div/div[2]/form/div[1]/div/div/input').clear()
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[4]/div/div[2]/form/div[1]/div/div/input').send_keys(name)
        sleep(1)
        Log().info("修改角色")
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[4]/div/div[2]/form/div[2]/div/div/div/span/span/i').click()
        sleep(1)
        self.d.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[2]').click()
        sleep(1)
        Log().info("修改备注")
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[4]/div/div[2]/form/div[3]/div/div/textarea').send_keys(beizhu)
        sleep(1)
        Log().info("点击提交")
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[4]/div/div[3]/div/button[1]').click()
        WebDriverWait(self.d, 10, 1).until(lambda ele: self.d.find_element_by_css_selector('body > div.el-message.el-message--success'))
        t = self.d.find_element_by_css_selector('body > div.el-message.el-message--success').text
        Log().info("修改成功")
        self.d.close()
        return t

    def select_name(self,name):
        Log().info("输入用户名称查询")
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[1]/form/div[1]/div/div/input').send_keys(name)
        sleep(1)
        try:
            Log().info("点击查询")
            self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[1]/form/div[3]/div/button[2]').click()
            sleep(1)
            m=self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[3]/div[1]/div[3]/table/tbody/tr[1]/td[5]/div/button[1]/span').text
            Log().info("查询成功")
            self.d.close()
            return m
        except Exception :
            Log().debug("异常原因:用户不存在")
            screenshot(self.d, 'xitong')
            raiseout()

    def select_juese(self,name):
        Log().info("选择角色名称查询")
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[1]/form/div[2]/div/div/div/input').send_keys(name)
        sleep(1)
        try:
            Log().info("点击查询")
            self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[1]/form/div[3]/div/button[2]').click()
            sleep(1)
            m=self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[3]/div[1]/div[3]/table/tbody/tr[1]/td[5]/div/button[1]/span').text
            Log().info("查询成功")
            self.d.close()
            return m
        except Exception :
            Log().debug("异常原因:用户不存在")
            screenshot(self.d, 'xitong')
            raiseout()

    def delete(self):
        Log().info("选择第二页数据删除")
        WebDriverWait(self.d,10,1).until(lambda ele:self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[3]/div[1]/div[3]/table/tbody/tr[3]/td[5]/div/button[2]'))
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[3]/div[1]/div[3]/table/tbody/tr[3]/td[5]/div/button[2]').click()
        try:
            Log().info("点击删除")
            self.d.find_element_by_xpath('/html/body/div[2]/div/div[3]/button[2]').click()
            WebDriverWait(self.d, 60,1).until(lambda ele: self.d.find_element_by_css_selector('body > div.el-message.el-message--success'))
            m = self.d.find_element_by_css_selector("body > div.el-message.el-message--success").text
            Log().info("删除成功")
            self.d.close()
            return m
        except Exception :
            Log().debug("删除失败")
            screenshot(self.d, 'yewu')
            raiseout()

