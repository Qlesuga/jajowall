from PyQt6.QtWidgets import QVBoxLayout,QWidget,QLabel,QPushButton
from PyQt6.QtCore import Qt
from .imagePreview.imagePreview import ImagePreview

class WallpaperPreview(QPushButton):
    def __init__(self,name,path,controller):
        super().__init__()

        self.__layout = QVBoxLayout()
        self.setLayout(self.__layout)

        self.setFixedSize(128,112)
        self.path = path

        self.pixmap = ImagePreview(path).scaledToHeight(60)
        self.preview = QLabel()

        self.preview.setPixmap(self.pixmap)
        self.preview.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.__layout.addWidget(self.preview)
        
        self.name = QLabel(name)
        self.name.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.__layout.addWidget(self.name)

        self.clicked.connect(lambda: controller.setSelected(self.path))