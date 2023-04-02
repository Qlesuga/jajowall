from PyQt6.QtWidgets import QMenu,QInputDialog
from PyQt6.QtGui import QAction
from PyQt6.QtCore import pyqtSignal

class Menu(QMenu):

    changeName = pyqtSignal(str)

    def __init__(self):
        super().__init__()

        self.name = QAction("Change Name")
        self.name.triggered.connect(self.__changeName)

        self.path = QAction("Change Path")
        self.delete = QAction("Delete")

        self.addAction(self.name)
        self.addAction(self.path)
        self.addAction(self.delete)

    def __changeName(self):
        value, ok = QInputDialog.getText(self,"change name","name")
        if(ok!=True):
            return
        self.changeName.emit(value)
        
    

