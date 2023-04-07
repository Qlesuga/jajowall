from PyQt6.QtWidgets import QHBoxLayout,QWidget
from .refresh import Refresh
from .apply import Apply
from .soundSlider import SoundSlider

class ActionList(QWidget):
    def __init__(self):
        super().__init__()

        self.__layout = QHBoxLayout()
        self.setLayout(self.__layout)

        self.soundSlider = SoundSlider()
        self.__layout.addWidget(self.soundSlider)

        self.refresh = Refresh()
        self.__layout.addWidget(self.refresh)

        self.apply = Apply()
        self.__layout.addWidget(self.apply)

