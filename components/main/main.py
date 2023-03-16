from PyQt6.QtWidgets import QApplication,QWidget,QHBoxLayout
from ..libary.libary import Libary
from ..settings.settings import Settings
from ..wallpaperController.wallpaperController import WallpaperController

class Main(QWidget):
    def __init__(self):
        super().__init__()

        self.__layout = QHBoxLayout()
        self.setLayout(self.__layout)

        self.settings = Settings()
        self.__layout.addWidget(self.settings)

        self.libary = Libary()
        self.__layout.addWidget(self.libary)

        self.wallpaperController = WallpaperController()

        self.libary.actions.apply.clicked.connect(lambda: self.wallpaperController.setMovie(self.libary.wallpaperList.selected))
        self.settings.addForm.add.clicked.connect(self.libary.wallpaperList.refresh)


        