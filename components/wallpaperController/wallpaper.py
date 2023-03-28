from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtCore import Qt,QSize
from .player.player import Player
from .workerw import workerw
import win32gui

class Wallpaper(QMainWindow):
    def __init__(self,x,y,width,height):
        super().__init__()
        self.setWindowOpacity(0)
        self.setMaximumWidth(width)
        self.setMaximumHeight(height)
        self.setGeometry(
            x,
            y,
            width,
            height)
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)

        win32gui.SetParent(self.winId(),workerw)
        self.show()

    def setMovie(self,path):
        self.setWindowOpacity(100)
        self.player = Player(path,QSize(self.width(),self.height()))
        self.setCentralWidget(self.player)