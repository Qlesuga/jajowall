from PyQt6.QtWidgets import QWidget, QVBoxLayout
from PyQt6.QtCore import Qt

from .autoStart import AutoStart
from .mute import Mute

class ButtonList(QWidget):
    def __init__(self):
        super().__init__()

        self.__layout = QVBoxLayout()
        self.setLayout(self.__layout)
        self.__layout.setAlignment(Qt.AlignmentFlag.AlignBottom)
        

        self.mute = Mute()
        self.__layout.addWidget(self.mute)

        self.autoStart = AutoStart()
        self.__layout.addWidget(self.autoStart)

