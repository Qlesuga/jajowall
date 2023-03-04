from PyQt6.QtWidgets import QWidget, QVBoxLayout
from PyQt6.QtCore import Qt
from .components.title import Title
from .components.buttonList import ButtonList
from .components.addForm import AddForm


class Settings(QWidget):
    def __init__(self):
        super().__init__()
        self.__layout = QVBoxLayout()
        self.setLayout(self.__layout)
        self.setFixedSize(280,400)


        self.title = Title()
        self.__layout.addWidget(self.title)

        self.addForm = AddForm()
        self.__layout.addWidget(self.addForm)

        self.buttonList = ButtonList()
        self.__layout.addWidget(self.buttonList)

        