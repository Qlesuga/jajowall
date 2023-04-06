from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtGui import QIcon

class ErrorPopup(QMessageBox):
    def __init__(self,message):
        super().__init__()
        self.setIcon(QMessageBox.Icon.Critical)
        self.setWindowTitle("Error")
        self.setText(message)
        self.setStandardButtons(QMessageBox.StandardButton.Ok)
        self.setWindowIcon(QIcon("img/icon.png"))
        self.exec()
