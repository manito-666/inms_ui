#coding=utf-8

import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from common.readconfig import ReadConfig
# 读取配置文件
config_file_path = os.path.split(os.path.realpath(__file__))[0]
read_config = ReadConfig(os.path.join(config_file_path,'config.ini'))

# 项目参数设置
prj_path = read_config.getValue('projectConfig','project_path')

# 日志路径
log_path = os.path.join(prj_path+'/util'+'/log')

# 截图文件路径
img_path = os.path.join(prj_path+'/run'+'/PrintScreen')

# 测试报告路径

report_path = os.path.join(prj_path+'/run'+'/report')


# 默认浏览器
browser = 'Chrome'

# 测试数据路径
data_path = os.path.join(prj_path+'/util'+'/data.xlsx')

impo_path=os.path.join(prj_path+'/util'+'/users-Template .xlsx')
