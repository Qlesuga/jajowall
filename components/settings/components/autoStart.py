from PyQt6.QtWidgets import QCheckBox
from config import config
import winreg
import os
class AutoStart(QCheckBox):
    def __init__(self):
        super().__init__()
        self.setText("autostart")

        self.setChecked(config.autostart)
        print(__file__)
        self.clicked.connect(self.changeAutostart)

    def changeAutostart(self):
        python_exe = os.path.join(os.environ['LOCALAPPDATA'], 'Programs', 'Python', 'Python39', 'python.exe')

        key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run")
        winreg.SetValueEx(key, 'jajowall', 0, winreg.REG_SZ, f'{";"*config.autostart}"{python_exe}" "{os.path.abspath(config.parentDir)}"')
        key.Close()
        config.autostart = not config.autostart



