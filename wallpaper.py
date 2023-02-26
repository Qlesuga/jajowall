from PyQt6.QtWidgets import QApplication, QMainWindow,QLabel
from PyQt6.QtGui import QMovie
from PyQt6.QtCore import Qt
import sys
import config
import win32gui

class Wallpaper(QMainWindow,):
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

        self.movie = QMovie("test.gif")
        self.label.setMovie(self.movie)
        self.movie.start()

        win32gui.SetParent(self.winId(),config.workerw)

        self.show()

if __name__=="__main__":
    import workerw
    app = QApplication(sys.argv)

    wallpaper = Wallpaper(1920,1080)

    sys.exit(app.exec())