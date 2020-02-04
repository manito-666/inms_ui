# -*-coding:utf-8 -*-
import os
from datetime import datetime
from config import globalparam
"""
屏幕截图--出现异常
"""
def screenshot(driver, case_name):
    file_path =globalparam.img_path
    screenshotPath = os.path.join(file_path, case_name)
    time_now = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
    screen_shot_name = "CheckPoint_NG.png"
    screen_img = screenshotPath + '_' + time_now + '_' + screen_shot_name
    driver.get_screenshot_as_file(screen_img)
    m=globalparam.img_path
    print("截图已保存在:"+m)
    return screen_img
