import win32gui
import win32api


def get_window_info():  # 获取阴阳师窗口信息
    wdname = u'智选期管系统'
    # 取得窗口句柄
    handle = win32gui.FindWindow(0, wdname)
    if not handle:
        print("窗口找不到，请确认窗口句柄名称：【%s】" % wdname)
        exit()
    # 窗口显示最前面
    win32gui.SetForegroundWindow(handle)
    if handle == 0:
        # text.insert('end', '小轩提示：请打开PC端阴阳师\n')
        # text.see('end')  # 自动显示底部
        return None
    else:
        return win32gui.GetWindowRect(handle)


def resolution():  # 获取屏幕分辨率
    return win32api.GetSystemMetrics(0), win32api.GetSystemMetrics(1)


print(get_window_info())
print(resolution())
