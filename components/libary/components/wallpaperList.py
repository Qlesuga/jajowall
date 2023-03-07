from PyQt6.QtWidgets import QWidget,QGridLayout
from PyQt6.QtCore import Qt
from .wallpaperPreview import WallpaperPreview
import json
class WallpaperList(QWidget):
    def __init__(self):
        super().__init__()

        self.__layout = QGridLayout()
        self.setLayout(self.__layout)
        self.__layout.setAlignment(Qt.AlignmentFlag.AlignTop)


        self.setFixedWidth(300)
        self.refresh()
    
    def refresh(self):
        for i in reversed(range(self.__layout.count())): 
            self.__layout.itemAt(i).widget().setParent(None)
        with open("config/wallpapers.json","r+") as wallpapers:
            wallpapers_json = json.load(wallpapers)
            i = 0
            j = 0
            for id in wallpapers_json:
                if(i%2==0):
                    i=0
                    j+=1
                name = wallpapers_json[id]["name"]
                path = wallpapers_json[id]["path"]
                self.__layout.addWidget(WallpaperPreview(name,path),j,i)
                i+=1