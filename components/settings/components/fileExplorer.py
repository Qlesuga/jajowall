from PyQt6.QtWidgets import QPushButton
from PyQt6.QtGui import QIcon

class FileExplorer(QPushButton):
    def __init__(self):
        super().__init__()
        self.icon = QIcon("img/fileExplorer.png")
        self.setIcon(self.icon)
        self.setFixedSize(24,24)

