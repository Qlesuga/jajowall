from PyQt6.QtWidgets import QVBoxLayout,QWidget,QScrollArea
from PyQt6.QtCore import Qt
from .components.actionsList import ActionList
from .components.title import Title
from .components.wallpaperList import WallpaperList


class Libary(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedWidth(320)
        
        self.scroll = QScrollArea()
        
        self.__layout = QVBoxLayout()
        self.setLayout(self.__layout)
        
        self.title = Title()
        self.__layout.addWidget(self.title)

        self.actions = ActionList()
        self.__layout.addWidget(self.actions)


        self.wallpaperList = WallpaperList()
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.wallpaperList)
        self.__layout.addWidget(self.scroll)

        

        