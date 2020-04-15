import wmi
import subprocess

c = wmi.WMI()

for sys in c.Win32_OperatingSystem():
    # 系统信息
    print(sys.Caption)
    # 系统版本号
    print(sys.BuildNumber)
    # 32/64位
    print(sys.OSArchitecture)
    # 当前系统进程数
    print(sys.NumberOfProcesses)

# 处理器信息
for pro in c.win32_Processor():
    print(pro.DeviceID)
    print(pro.Name.strip())

p = subprocess.Popen(['sudo', 'cat', '/sys/class/dmi/id/product_uuid'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, err = p.communicate()
print(out.strip('\n'))
