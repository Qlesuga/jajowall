from PyQt6.QtWidgets import QListWidget

class WallpaperList(QListWidget):
    def __init__(self):
        super().__init__()

        self.setFixedSize(300,300)