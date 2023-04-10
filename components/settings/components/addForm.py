from PyQt6.QtWidgets import QWidget,QHBoxLayout, QPushButton, QLineEdit,QFileDialog
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QStringListModel
import json
from components.error.errorPopup import ErrorPopup
from config import config

class AddForm(QWidget):
    def __init__(self):
        super().__init__()

        self.__layout = QHBoxLayout()
        self.setLayout(self.__layout)

        self.path = QLineEdit()
        self.__layout.addWidget(self.path)

        self.fileExplorer = QPushButton()
        self.fileExplorerIcon = QIcon(config.basePath+"img/fileExplorer.png")
        self.fileExplorer.setIcon(self.fileExplorerIcon)
        self.fileExplorer.setFixedSize(24,24)
        self.fileExplorer.clicked.connect(self.getFile)
        self.__layout.addWidget(self.fileExplorer)

        self.add = QPushButton("add")
        self.add.clicked.connect(self.addFileToJson)
        self.__layout.addWidget(self.add)

    def getFile(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.FileMode.AnyFile)
        filenames = QStringListModel()
		
        if dlg.exec():
            filenames = dlg.selectedFiles()
                
            self.path.setText(filenames[0])

    def addFileToJson(self):
        path = self.path.text()
        if(len(path)==0):
            ErrorPopup("Empty path")
            return
        with open("config/wallpapers.json", "r+") as wallpapers:
            wallpapers_json = json.load(wallpapers)
            keys = list(wallpapers_json.keys())
            if(len(keys)>0):
                id = int(keys[-1])+1
            elif(len(keys)==0):
                id="0"

            wallpapers.seek(0)
            wallpapers.truncate(0)
                    
            newWallpaper = {id: {"name":path.split('/')[-1],"path":path}}
            wallpapers_json.update(newWallpaper)
            json.dump(wallpapers_json, wallpapers,indent=4)                
        self.path.setText("")
        

        




