import win32api
import win32con

class AutoRun():
  def __init__(self):
    name = input('请输入要添加的项值名称(输入空格使用默认值: bookmapservice)：').strip()
    if name == '':
      name = 'bookmapservice'

    path = input('请输入要添加的项值路径(输入空格使用默认值: C:\\Program Files\\bookmap\\bookmap.exe)：').strip()
    if path == '':
      path = 'C:\\Program Files\\bookmap\\bookmap.exe'

    print("要注册的服务名为：{name}, 自启动应用路径：{path}".format(name=name, path=path))
    # 注册表项名
    KeyName = 'Software\\Microsoft\\Windows\\CurrentVersion\\Run'
    # 异常处理
    try:
      key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER, KeyName, 0, win32con.KEY_ALL_ACCESS)
      win32api.RegSetValueEx(key, name, 0, win32con.REG_SZ, path)
      win32api.RegCloseKey(key)
    except Exception as e:
      win32api.MessageBox(0, str(e), "Error",
                                win32con.MB_OK | win32con.MB_SYSTEMMODAL | win32con.MB_ICONERROR)
    info = '添加{name}至windows启动项成功！'.format(name=name)
    win32api.MessageBox(0, info, "Information",
                                win32con.MB_OK | win32con.MB_SYSTEMMODAL | win32con.MB_ICONINFORMATION)

if __name__=='__main__':
  auto=AutoRun()
