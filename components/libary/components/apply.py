from PyQt6.QtWidgets import QPushButton

class Apply(QPushButton):
    def __init__(self):
        super().__init__()
        self.setText("apply")