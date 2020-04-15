import pyautogui
from PIL import Image

from test.Test import get_window_info
from util.Click import get_center
from util.KitPicture import hamming, get_hash

x_add = 5
y_add = 434

# win_info = get_window_info()
# img = pyautogui.screenshot(region=(496 + x_add, 520 + y_add, 545 + x_add - (496 + x_add), 545 + y_add - (520 + y_add)))
# img.save('G:/foo.png')

sImg = Image.open('G:/foo.png')
# 门1  496 520，545 545
img = pyautogui.screenshot(region=(496 + x_add, 520 + y_add, 545 + x_add - (496 + x_add), 545 + y_add - (520 + y_add)))
if hamming(get_hash(sImg), get_hash(img), 10):
    # x = 517 + x_add
    # y = 522 + y_add
    x, y = get_center(496, 520, 545, 545, x_add, y_add)  # 获得中心点
    pyautogui.click(x, y)
else:
    print('none')

# x, y = pyautogui.center((496 + x_add, 520 + y_add, 545 + x_add, 545 + y_add))  # 获得中心点
# pyautogui.click(x, y)


# duelbtn = pyautogui.locateOnScreen('G:/foo.png')
# if duelbtn:
#     x, y = pyautogui.center(duelbtn)  # 获得中心点
#     pyautogui.click(x, y)
# else:
#     print('none')
