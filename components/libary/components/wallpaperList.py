from PyQt6.QtWidgets import QWidget,QGridLayout
from PyQt6.QtCore import Qt
from .wallpaperPreview import WallpaperPreview
import json
import os
class WallpaperList(QWidget):
    def __init__(self):
        super().__init__()
        self.selected = None

        self.__layout = QGridLayout()
        self.setLayout(self.__layout)
        self.__layout.setAlignment(Qt.AlignmentFlag.AlignTop)


        self.setFixedWidth(300)
        self.refresh()
    
    def refresh(self):
        for i in reversed(range(self.__layout.count())): 
            self.__layout.itemAt(i).widget().setParent(None)
        try:
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
                    preview = WallpaperPreview(id,name,path,self)
                    self.__layout.addWidget(preview,j,i)
                    i+=1
        except FileNotFoundError:
            try:
                os.makedirs("./config")
            except FileExistsError:
                pass
            with open("config/wallpapers.json","w") as wallpapers:
                wallpapers.write("{}")
        

        

    def setSelected(self,path):
        self.selected = path
        print(path)