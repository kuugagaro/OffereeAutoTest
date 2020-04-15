import os
import time

import pyautogui as pag
import win32gui

wdname = u'智选期管系统'
# 取得窗口句柄
handle = win32gui.FindWindow(0, wdname)
# 窗口显示最前面
win32gui.SetForegroundWindow(handle)
win_info = win32gui.GetWindowRect(handle)
x_add = win_info[0]
y_add = win_info[1]
try:
    while True:
        print("按下Ctrl + C 结束程序")
        # pag.position()返回鼠标的坐标
        x, y = pag.position()
        x = x - x_add
        y = y - y_add
        posStr = "当前鼠标位置:" + str(x).rjust(4) + ',' + str(y).rjust(4)
        # 打印当前鼠标位置坐标
        print(posStr)
        time.sleep(1)
        # 清除屏幕
        os.system('cls')
# 捕获异常 KeyboardInterrupt:用户中断执行(通常是输入^C)
except KeyboardInterrupt:
    print('已退出')
