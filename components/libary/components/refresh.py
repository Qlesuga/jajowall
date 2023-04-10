from PyQt6.QtWidgets import QPushButton
from PyQt6.QtGui import QIcon
from config import config

class Refresh(QPushButton):
    def __init__(self):
        super().__init__()
        self.icon = QIcon(config.basePath+"img/refresh.png")
        self.setIcon(self.icon)
        self.setFixedSize(24,24)

