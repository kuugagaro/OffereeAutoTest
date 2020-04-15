import random
import time

import pyautogui
import win32api

from test.Test import get_window_info

win_info = get_window_info()
x_add = win_info[0]
y_add = win_info[1]
print(x_add, y_add)

# 点击行情
market_select_x = 220
# 点击行情y
market_select_y = (110, 135, 160, 185)
# 买
buy_xy = (128, 781)
# 卖
sell_xy = (280, 781)

# 数量输入点击
input_amount_click_xy = (190, 690)
# 键盘码
keypress_mark = (0, 97, 98, 99)


def auto_buy_sell():
    click_count = 0
    while True:
        # 点击行情
        sel_market_y = random.randint(0, 3)
        x = market_select_x + x_add
        y = market_select_y[sel_market_y] + y_add
        pyautogui.click(x, y)
        time.sleep(0.5)
        # 点击数量输入框
        x = input_amount_click_xy[0] + x_add
        y = input_amount_click_xy[1] + y_add
        pyautogui.click(x, y)
        time.sleep(0.5)
        # 按backspace 删除数量
        win32api.keybd_event(8, 0, 0, 0)  # Backspace    8
        time.sleep(0.5)
        # 输入数量
        sel_input_num = random.randint(1, 3)
        win32api.keybd_event(keypress_mark[sel_input_num], 0, 0, 0)
        time.sleep(0.5)
        # 买入/卖出
        sel_buy_sell = random.randint(0, 1)
        if sel_buy_sell == 0:
            x = buy_xy[0] + x_add
            y = buy_xy[1] + y_add
            pyautogui.click(x, y)
        else:
            x = sell_xy[0] + x_add
            y = sell_xy[1] + y_add
            pyautogui.click(x, y)
        time.sleep(0.5)
        # 按键盘左箭头
        win32api.keybd_event(37, 0, 0, 0)
        time.sleep(0.5)
        # 按enter键
        win32api.keybd_event(13, 0, 0, 0)
        # 暂停时间
        stop_time = random.randint(1, 120)
        click_count += 1
        print('click count:' + str(click_count))
        time.sleep(stop_time)
        # win32api.keybd_event(37, 0, 0, 0)  # Left Arrow   37
        # win32api.keybd_event(13, 0, 0, 0)  # Enter      13
        # win32api.keybd_event(8, 0, 0, 0)  # Backspace    8
        # win32api.keybd_event(97, 0, 0, 0)  # 1   97,2   98,3   99


# use in Offeree.exe 1920*1080
# cmd main/BuyOrSell.py
# pyinstaller -F -n Offeree_Auto_Test -i G:\python\OffereeAutoTest\tmp.ico BuyOrSell.py
if __name__ == "__main__":
    # 刷传送门
    auto_buy_sell()
