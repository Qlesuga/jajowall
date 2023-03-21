from PyQt6.QtWidgets import QLabel,QWidget
from PyQt6.QtGui import QMovie
from PyQt6.QtCore import Qt

class GifPlayer(QWidget):
    def __init__(self,path):
        super().__init__()
        label = QLabel(self)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setScaledContents(True)
        movie = QMovie(path)
        label.setMovie(movie)
        movie.start()
        
    
