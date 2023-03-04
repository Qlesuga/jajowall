from PyQt6.QtWidgets import QWidget,QHBoxLayout
from .add import Add
from .fileExplorer import FileExplorer
from .path import Path

class AddForm(QWidget):
    def __init__(self):
        super().__init__()

        self.__layout = QHBoxLayout()
        self.setLayout(self.__layout)

        self.path = Path()
        self.__layout.addWidget(self.path)

        self.fileExplorer = FileExplorer()
        self.__layout.addWidget(self.fileExplorer)

        self.add = Add()
        self.__layout.addWidget(self.add)




