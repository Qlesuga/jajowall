from PyQt6.QtWidgets import QLabel
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

class Title(QLabel):
    def __init__(self):
        super().__init__()
        self.setText("LIBARY")
        self.setFont(QFont('Mona-Sans Black', 28))
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)