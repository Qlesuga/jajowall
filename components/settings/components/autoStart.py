from PyQt6.QtWidgets import QCheckBox

class AutoStart(QCheckBox):
    def __init__(self):
        super().__init__()
        self.setText("autostart")