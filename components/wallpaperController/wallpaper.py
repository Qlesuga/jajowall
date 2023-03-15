from PyQt6.QtWidgets import QApplication, QMainWindow,QLabel
from PyQt6.QtGui import QMovie
from PyQt6.QtCore import Qt
import sys
from .workerw import workerw
import win32gui

class Wallpaper(QMainWindow):
    def __init__(self,x,y,width,height):
        super().__init__()
        self.setMaximumWidth(width)
        self.setMaximumHeight(height)
        self.setGeometry(
            x,
            y,
            width,
            height)
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)

        self.label = QLabel(self)
        self.label.setGeometry(0,0,width,height)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setScaledContents(True)
        self.setCentralWidget(self.label)

        win32gui.SetParent(self.winId(),workerw)

        self.show()

    def setMovie(self,path):
        movie = QMovie(path)
        self.label.setMovie(movie)
        movie.start()