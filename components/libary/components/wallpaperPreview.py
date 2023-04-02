from PyQt6.QtWidgets import QVBoxLayout,QLabel,QPushButton
from PyQt6.QtCore import Qt
from .imagePreview.imagePreview import ImagePreview
from .menu import Menu
import json
class WallpaperPreview(QPushButton):
    def __init__(self,id,name,path,controller):
        super().__init__()
        self.id = id

        self.__layout = QVBoxLayout()
        self.setLayout(self.__layout)

        self.setFixedSize(128,112)
        self.path = path

        self.preview = QLabel()
        self.refreshPath()
        self.preview.setPixmap(self.pixmap)
        self.preview.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.__layout.addWidget(self.preview)
        
        self.name = QLabel(name)
        self.name.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.__layout.addWidget(self.name)

        self.clicked.connect(lambda: controller.setSelected(self.path))

        self.menu = Menu()
        self.menu.changeName.connect(self.changeName)
        self.menu.delete.connect(self.delete)
        self.menu.changePath.connect(self.changePath)


    def refreshPath(self):
        self.pixmap = ImagePreview(self.path).scaledToHeight(60)
        self.preview.setPixmap(self.pixmap)

    def contextMenuEvent(self, event):
        self.menu.exec(event.globalPos())

    def changeName(self,name):
        self.name.setText(name)
        with open("config/wallpapers.json","r+") as wallpapers:
            wallpapers_json = json.load(wallpapers)
            wallpapers_json[self.id]["name"] = name

            wallpapers.seek(0)
            wallpapers.truncate(0)
            json.dump(wallpapers_json, wallpapers,indent=4)

    def delete(self):
        with open("config/wallpapers.json","r+") as wallpapers:
            wallpapers_json = json.load(wallpapers)
            del wallpapers_json[self.id]

            wallpapers.seek(0)
            wallpapers.truncate(0)
            json.dump(wallpapers_json, wallpapers,indent=4)

    def changePath(self,path):
        self.path = path
        self.refreshPath()
        with open("config/wallpapers.json","r+") as wallpapers:
            wallpapers_json = json.load(wallpapers)
            wallpapers_json[self.id]["path"] = path

            wallpapers.seek(0)
            wallpapers.truncate(0)

            json.dump(wallpapers_json, wallpapers,indent=4)
