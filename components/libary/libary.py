from PyQt6.QtWidgets import QVBoxLayout,QWidget,QLabel
from .components.actionsList import ActionList
from .components.title import Title
from .components.wallpaperList import WallpaperList


class Libary(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(320,400)
        
        self.__layout = QVBoxLayout()
        self.setLayout(self.__layout)
        
        self.title = Title()
        self.__layout.addWidget(self.title)

        self.actions = ActionList()
        self.__layout.addWidget(self.actions)

        self.wallpaperList = WallpaperList()
        self.__layout.addWidget(self.wallpaperList)

        

        