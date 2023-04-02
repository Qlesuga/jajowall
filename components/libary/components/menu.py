from PyQt6.QtWidgets import QMenu
from PyQt6.QtGui import QAction




class Menu(QMenu):
    def __init__(self):
        super().__init__()

        self.name = QAction("Change Name")
        self.path = QAction("Change Path")
        self.delete = QAction("Delete")

        self.addAction(self.name)
        self.addAction(self.path)
        self.addAction(self.delete)