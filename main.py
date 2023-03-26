import sys
from PyQt6.QtWidgets import QApplication,QMainWindow,QHBoxLayout
from PyQt6.QtGui import QIcon
from components.main.main import Main
from config import config
from config.settings import Settings

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.main = Main()

        self.setCentralWidget(self.main)

        self.setFixedSize(600,400)
        self.setWindowIcon(QIcon("./img/icon.png"));
        self.setWindowTitle("JajoWall")

loader = Settings()
loader.loadSettings()
print(config.volumeValue)
app = QApplication(sys.argv)
main = Window()
main.show()
ret = app.exec()
loader.saveSettings()
sys.exit(ret)
