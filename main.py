import sys
from PyQt6.QtWidgets import QApplication,QMainWindow,QHBoxLayout
from PyQt6.QtGui import QIcon
from components.main import Main
from config import config
from config.settings import Settings
import winreg
import ctypes

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        config.parentDir = __file__
        self.main = Main()

        self.setCentralWidget(self.main)

        self.setFixedSize(600,400)
        self.setWindowIcon(QIcon(config.basePath+"img/icon.png"));
        self.setWindowTitle("JajoWall")

loader = Settings()
loader.loadSettings()
app = QApplication(sys.argv)
main = Window()
main.show()
ret = app.exec()
loader.saveSettings()
key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Control Panel\\Desktop")
wallpaper_path, _ = winreg.QueryValueEx(key, "Wallpaper")

SPI_SETDESKWALLPAPER = 20
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, wallpaper_path, 0)

sys.exit(ret)
