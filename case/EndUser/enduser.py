from common.Login import Login
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from common.img import screenshot
from common.raiseout import raiseout
from util.log.mylog import Log
class z_d():
    def __init__(self):
        L = Login()
        L.login()
        self.d = L.d
        self.d.maximize_window()
        Log().info("点击终端用户")
        WebDriverWait(self.d,30,0.5).until(lambda ele:self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[1]/div/div/ul/li[1]/ul/li[2]'))
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[1]/div/div/ul/li[1]/ul/li[2]').click()

    def add(self,phone,im,beizhu):
        Log().info("点击添加用户")
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[2]/div[1]/span').click()
        sleep(2)
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/div[2]/form/div[1]/div/div/input').send_keys(phone)
        sleep(2)
        Log().info("输入IMSI")
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/div[2]/form/div[2]/div/div/input').send_keys(im)
        sleep(1)
        Log().info("选择所属专网华西")
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/div[2]/form/div[3]/div/div/div[1]/span/span/i').click()
        sleep(1)
        self.d.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[1]').click()
        Log().info("选择场景手术")
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/div[2]/form/div[4]/div/div/div[1]/span/span/i').click()
        sleep(1)
        self.d.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/ul/li[1]').click()
        sleep(1)
        Log().info("选择业务")
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/div[2]/form/div[5]/div/div/div[1]/span/span/i').click()
        sleep(1)
        self.d.find_element_by_xpath('/html/body/div[5]/div[1]/div[1]/ul/li[1]').click()
        sleep(1)
        Log().info("输入备注")
        self.d.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/div[2]/form/div[6]/div/div/textarea').send_keys(beizhu)
        sleep(1)
        try:
            self.d.find_element_by_css_selector("#index > div.second-container > div.main-wrapper > div > div:nth-child(2) > div:nth-child(2) > div.el-dialog__wrapper > div > div.el-dialog__footer > div > button.el-button.el-button--primary > span").click()
            Log().info("点击提交")
            WebDriverWait(self.d, 10, 1).until(lambda ele: self.d.find_element_by_css_selector('body > div.el-message.el-message--success > p'))
            t = self.d.find_element_by_css_selector('body > div.el-message.el-message--success > p').text
            Log().info("添加成功")
            self.d.close()
            return t
        except Exception :
            Log().debug("异常原因:终端用户手机号不能重复")
            screenshot(self.d, 'zhongduan')
            raiseout()

    def alter(self):
        Log().info("点击编辑默认修改列表第一条数据")
        WebDriverWait(self.d,10,1).until(lambda ele:self.d.find_element_by_css_selector("#index > div.second-container > div.main-wrapper > div > div:nth-child(2) > div:nth-child(2) > div.table-pagination > div.el-table.el-table--fit.el-table--striped.el-table--enable-row-hover.el-table--enable-row-transition > div.el-table__body-wrapper.is-scrolling-none > table > tbody > tr:nth-child(1) > td.el-table_2_column_18 > div > button:nth-child(1)"))
        self.d.find_element_by_css_selector("#index > div.second-container > div.main-wrapper > div > div:nth-child(2) > div:nth-child(2) > div.table-pagination > div.el-table.el-table--fit.el-table--striped.el-table--enable-row-hover.el-table--enable-row-transition > div.el-table__body-wrapper.is-scrolling-none > table > tbody > tr:nth-child(1) > td.el-table_2_column_18 > div > button:nth-child(1)").click()
        sleep(1)
        Log().info("修改IMSI")
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/div[2]/form/div[2]/div/div/input').send_keys("1111")
        sleep(1)
        Log().info("修改备注")
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/div[2]/form/div[6]/div/div/textarea').send_keys("22")
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
            screenshot(self.d, 'zhongduan')
            raiseout()

    def select(self,sj):
        Log().info("查询终端用户[手机号]")
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[1]/form/div[1]/div/div/input').send_keys(sj)
        sleep(1)
        try:
            self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[1]/form/div[6]/div/button[2]').click()
            sleep(1)
            m=self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div[3]/table/tbody/tr/td[2]').text
            Log().info("查询成功")
            self.d.close()
            return m
        except Exception :
            Log().debug("异常原因:未找到该元素")
            screenshot(self.d, 'zhongduan')
            raiseout()

    def pladd(self):
        self.d.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/div/div[2]/div[2]/div[1]/div').click()
        sleep(1)
        Log().info("点击下载模版")
        try:
            m=self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/form/div[1]/a').text
            Log().info("下载成功")
            self.d.close()
        except Exception :
            Log().debug("下载失败")
            screenshot(self.d, 'zhongduan')
            raiseout()
        else:
            return m

    def pldaoru(self,wenjian):
        Log().info("点击批量导入")
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[2]/div[1]/div/span').click()
        sleep(1)
        Log().info("选择文件")
        self.d.find_element_by_name("file").send_keys(wenjian)
        sleep(1)
        try:
            self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[3]/div/div[3]/div/button[1]').click()
            sleep(2)
            WebDriverWait(self.d,10,1).until(lambda ele:self.d.find_element_by_css_selector("body > div.el-message.el-message--success"))
            m=self.d.find_element_by_css_selector('body > div.el-message.el-message--success').text
            Log().info(m)
            self.d.close()
            return m
        except Exception :
            Log().debug("异常原因:终端用户手机号不能重复")
            screenshot(self.d, 'zhongduan')
            raiseout()

    def delete(self):
        Log().info("删除第二页第一个元素")
        WebDriverWait(self.d, 30, 1).until(lambda ele: self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[9]/div/button[2]'))
        self.d.find_element_by_xpath('//*[@id="index"]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[9]/div/button[2]').click()
        WebDriverWait(self.d,30,1).until(lambda ele:self.d.find_element_by_xpath('/html/body/div[2]/div/div[3]/button[2]/span'))
        Log().info("确认删除")
        self.d.find_element_by_xpath('/html/body/div[2]/div/div[3]/button[2]/span').click()
        try:
            WebDriverWait(self.d, 60, 1).until(lambda ele: self.d.find_element_by_css_selector('body > div.el-message.el-message--success'))
            m = self.d.find_element_by_css_selector("body > div.el-message.el-message--success").text
            Log().info("删除成功")
            self.d.close()
            return m
        except Exception :
            Log().debug("异常原因:无法删除")
            screenshot(self.d, 'zhongduan')
            raiseout()

    def betch_delete(self):
        Log().info("选择批量删除元素")
        WebDriverWait(self.d,10,1).until(lambda ele:self.d.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[1]/div/label/span/span'))
        self.d.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[1]/div/label/span/span').click()
        sleep(1)
        self.d.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[2]/td[1]/div/label/span/span').click()
        sleep(1)
        self.d.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/div[1]/div/span[1]').click()
        sleep(1)
        Log().info("点击确认删除")
        try:
            self.d.find_element_by_xpath('/html/body/div[2]/div/div[3]/button[2]').click()
            WebDriverWait(self.d,30,1).until(lambda ele:self.d.find_element_by_css_selector('.el-message'))
            m=self.d.find_element_by_css_selector('.el-message').text
            Log().info("批量删除成功")
            self.d.close()
            return m
        except Exception:
            Log().debug("删除失败")
            screenshot(self.d, 'zhongduan')
            raiseout()
