from PyQt6.QtWidgets import QWidget,QHBoxLayout, QPushButton, QLineEdit
from PyQt6.QtGui import QIcon

class AddForm(QWidget):
    def __init__(self):
        super().__init__()

        self.__layout = QHBoxLayout()
        self.setLayout(self.__layout)

        self.path = QLineEdit()
        self.__layout.addWidget(self.path)

        self.fileExplorer = QPushButton()
        self.fileExplorerIcon = QIcon("img/fileExplorer.png")
        self.fileExplorer.setIcon(self.fileExplorerIcon)
        self.fileExplorer.setFixedSize(24,24)
        self.__layout.addWidget(self.fileExplorer)

        self.add = QPushButton("add")
        self.__layout.addWidget(self.add)




