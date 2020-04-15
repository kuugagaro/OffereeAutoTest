import pyautogui

# 获取屏幕尺寸
screenWidth, screenHeight = pyautogui.size()
print(screenWidth, screenHeight)

# 获取鼠标当前位置
currentMouseX, currentMouseY = pyautogui.position()
print(currentMouseX, currentMouseY)
