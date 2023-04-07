from PyQt6.QtWidgets import QWidget, QVBoxLayout
from PyQt6.QtCore import Qt

from .autoStart import AutoStart

class ButtonList(QWidget):
    def __init__(self):
        super().__init__()

        self.__layout = QVBoxLayout()
        self.setLayout(self.__layout)
        self.__layout.setAlignment(Qt.AlignmentFlag.AlignBottom)
        
        self.autoStart = AutoStart()
        self.__layout.addWidget(self.autoStart)

