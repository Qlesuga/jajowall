from PyQt6.QtWidgets import QLabel,QWidget
from PyQt6.QtGui import QMovie
from PyQt6.QtCore import Qt

class GifPlayer(QWidget):
    def __init__(self,path,size):
        super().__init__()
        label = QLabel(self)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setScaledContents(True)
        label.setFixedSize(size)
        movie = QMovie(path)
        label.setMovie(movie)
        movie.start()
        
    
