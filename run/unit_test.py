# coding=utf-8
import unittest,os,time
import HTMLTestRunner3
from common.unit_email import find_new_file
from util.log.mylog import Log
from config import globalparam
from common.unit_email import send_mail_html
dir = globalparam.report_path

if __name__ == '__main__':
    Log().__init__()
    now = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))
    report_title = '专网管理测试报告' + now + ".html"
    suite = unittest.defaultTestLoader.discover(".",pattern="test*.py",top_level_dir=None)
    #"."表示当前目录，"*tests.py"匹配当前目录下所有test.py结尾的用例
    report_Path=os.path.join(globalparam.report_path+'\\'+report_title)
    fp=open(report_Path,"wb")
    runner=HTMLTestRunner3.HTMLTestRunner(stream=fp,title=report_title,description=u'专网管理用例测试')
    runner.run(suite)
    fp.close()
    file = find_new_file(dir)  # 查找最新的html文件
    send_mail_html(file)  # 发送html内容邮件