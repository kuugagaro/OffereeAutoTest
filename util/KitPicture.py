import os

import pyautogui
from PIL import Image

from test.Test import get_window_info


def get_position(im1, im2):
    """
    传入需要获得坐标的小图路径
    返回值为空表示没找到
    """

    # im1 = Image.open(file_name1)
    # im2 = Image.open(file_name2)
    pix1 = im1.load()
    pix2 = im2.load()
    width1 = im1.size[0]
    height1 = im1.size[1]
    width2 = im2.size[0]
    height2 = im2.size[1]

    rgb2 = pix2[0, 0][:3]  # 左上角起始点
    for x in range(width1):
        for y in range(height1):
            rgb1 = pix1[x, y][:3]
            if rgb1 == rgb2:
                # 判断剩下的点是否相同
                status = 0
                # 图二的坐标是(s, j) --- (s-x, j-y)
                for s in range(x, x + width2):
                    for j in range(y, y + height2):
                        # 设置阈值范围
                        if abs(pix2[s - x, j - y][0] - pix1[s, j][0]) > 60 and abs(
                                pix2[s - x, j - y][1] - pix1[s, j][:3][1]) > 60 and abs(
                            pix2[s - x, j - y][1] - pix1[s, j][:3][1]) > 60:
                            status = 1
                if status:
                    continue
                else:
                    return x + round(0.5 * width2), y + round(0.5 * height2)


def get_hash(img):
    img = img.resize((16, 16), Image.ANTIALIAS).convert('L')  # 抗锯齿 灰度
    avg = sum(list(img.getdata())) / 256  # 计算像素平均值
    s = ''.join(map(lambda i: '0' if i < avg else '1', img.getdata()))  # 每个像素进行比对,大于avg为1,反之为0
    return ''.join(map(lambda j: '%x' % int(s[j:j + 4], 2), range(0, 256, 4)))


def get_img_hash(pic_name):
    sImg = Image.open(pic_name)
    return get_hash(sImg)


def hamming(hash1, hash2, n=20):
    b = False
    assert len(hash1) == len(hash2)
    if sum(ch1 != ch2 for ch1, ch2 in zip(hash1, hash2)) < n:
        b = True
    return b


# x1,y1:左上角 x2,y2:右下角
def kitPictureAsFile(locXY, pic_name, x_add, y_add):
    img = kitPictureAsImg(locXY, x_add, y_add)
    img.save(pic_name)


def kitPictureAsImg(locXY, x_add, y_add):
    x1 = locXY[0]
    y1 = locXY[1]
    x2 = locXY[2]
    y2 = locXY[3]
    img = pyautogui.screenshot(
        region=(x1 + x_add, y1 + y_add, x2 + x_add - (x1 + x_add), y2 + y_add - (y1 + y_add)))
    # print(x1 + x_add, y1 + y_add, x2 + x_add - (x1 + x_add), y2 + y_add - (y1 + y_add))
    return img


def kitPictureAsHash(locXY, x_add, y_add):
    img = kitPictureAsImg(locXY, x_add, y_add)
    return get_hash(img)


def compareImg(locXY, x_add, y_add, tImgHash):
    sHash = kitPictureAsHash(locXY, x_add, y_add)
    return hamming(sHash, tImgHash, 10)


# 选中的传送门图标 346, 573, 406, 603
win_info = get_window_info()
x_add = win_info[0]
y_add = win_info[1]
locXY = (487, 212, 549, 228)
kitPictureAsFile(locXY, 'D:/battle_stats_title_pic.png', x_add, y_add)

# simg = Image.open(os.path.abspath('../kitpic/p_ok_btn.png'))
# timg = pyautogui.screenshot()
# print(get_position(timg, simg))
