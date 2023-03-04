from PyQt6.QtWidgets import QPushButton
from PyQt6.QtGui import QIcon

class Refresh(QPushButton):
    def __init__(self):
        super().__init__()
        self.icon = QIcon("img/refresh.png")
        self.setIcon(self.icon)
        self.setFixedSize(24,24)

