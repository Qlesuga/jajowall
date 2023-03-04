from PyQt6.QtWidgets import QVBoxLayout,QWidget,QLabel
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from pathlib import Path

class WallpaperPreview(QWidget):
    def __init__(self,name,path):
        super().__init__()

        self.__layout = QVBoxLayout()
        self.setLayout(self.__layout)

        self.setFixedSize(128,112)
        print(path)
        self.pixmap = QPixmap(str(path)).scaledToHeight(72)
        self.preview = QLabel()
        self.preview.setPixmap(self.pixmap)
        self.preview.setFixedSize(128,72)
        self.__layout.addWidget(self.preview)
        self.name = QLabel(name)
        self.name.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.__layout.addWidget(self.name)