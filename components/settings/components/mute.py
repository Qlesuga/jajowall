from PyQt6.QtWidgets import QCheckBox

class Mute(QCheckBox):
    def __init__(self):
        super().__init__()
        self.setText("mute")