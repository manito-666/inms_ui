# coding=utf-8
import smtplib, time, os
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from util.log.mylog import Log
from config import globalparam

# 测试报告的路径
dir = globalparam.report_path
logger = Log()
def send_mail_html(file):
    '''发送html内容邮件'''
    # 发送邮箱
    sender = '983338654@qq.com'
    # 接收邮箱
    receiver = '983338654@qq.com'
    # 发送邮件主题
    t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    subject = '自动化测试报告结果' + t
    # 发送邮箱服务器
    smtpserver = 'smtp.qq.com'
    # 发送邮箱用户/密码
    username = '983338654@qq.com'
    password = 'azdcjpgvdwnebcfh'

    # 读取html文件内容
    f = open(file, 'rb')
    mail_body = f.read()
    f.close()

    email_text = '自动化测试报告'
    t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    subject = '自动化测试报告结果_' + t
    msg = MIMEMultipart()
    msg['Subject'] =subject   # 主题
    msg['From'] = sender  # 发件人
    msg['To'] =receiver
    part_text = MIMEText(email_text)
    msg.attach(part_text)
    file=file
    part_attach = MIMEApplication(open(file, 'rb').read())  # 打开附件
    part_attach.add_header('Content-Disposition', 'attachment', filename='测试报告.html')
    msg.attach(part_attach)
    # 登录并发送邮件
    try:
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver)
        smtp.login(username, password)
        smtp.sendmail(sender, [receiver,'1311691850@qq.com'], msg.as_string())
    except:
        logger.error('发送邮件失败')
    else:
        logger.info("发送邮件成功")
        smtp.quit()


def find_new_file(dir):
    '''查找目录下最新的文件'''
    file_lists = os.listdir(dir)
    file_lists.sort(key=lambda fn: os.path.getmtime(dir + "\\" + fn))
    file = os.path.join(dir, file_lists[-1])
    print('文件生成路径：', file)
    return file

if __name__ == '__main__':
    file = find_new_file(dir)  # 查找最新的html文件
    send_mail_html(file)  # 发送html内容邮件