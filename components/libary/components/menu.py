from PyQt6.QtWidgets import QMenu,QInputDialog
from PyQt6.QtGui import QAction
from PyQt6.QtCore import pyqtSignal

class Menu(QMenu):

    changeName = pyqtSignal(str)
    delete = pyqtSignal()

    def __init__(self):
        super().__init__()

        self.__name = QAction("Change Name")
        self.__name.triggered.connect(self.__changeName)

        self.__path = QAction("Change Path")
        self.__delete = QAction("Delete")
        self.__delete.triggered.connect(self.delete.emit)

        self.addAction(self.__name)
        self.addAction(self.__path)
        self.addAction(self.__delete)

    def __changeName(self):
        value, ok = QInputDialog.getText(self,"change name","name")
        if(ok!=True):
            return
        self.changeName.emit(value)
        
    

