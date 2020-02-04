from common.Login import Login
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait

class taishi:
    def __init__(self):
        L = Login()
        L.login()
        self.d = L.d
        WebDriverWait(self.d,30,1).until(lambda ele:self.d.find_element_by_xpath('/html/body/div/div/div[2]/div[1]/div/div/ul/li[2]/div'))
        self.d.find_element_by_xpath('/html/body/div/div/div[2]/div[1]/div/div/ul/li[2]/div').click()
        sleep(1)
        self.d.find_element_by_xpath('/html/body/div/div/div[2]/div[1]/div/div/ul/li[2]/ul/li').click()
        sleep(1)
        self.d.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/div/div/div[3]/div/div[2]/div/a').click()
        sleep(2)

    def zwdj(self):
        m=self.d.find_element_by_xpath('/html/body/div/div/div[3]/div[1]/div[1]/div[1]/div[1]').text
        self.d.close()
        return m

    def zwhy(self):
        m=self.d.find_element_by_xpath('/html/body/div/div/div[3]/div[1]/div[1]/div[2]/div[1]').text
        self.d.close()
        return m

    def zwzt(self):
        m=self.d.find_element_by_xpath('/html/body/div/div/div[3]/div[1]/div[2]/div/div[1]').text
        self.d.close()
        return m


