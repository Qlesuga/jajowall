from PyQt6.QtWidgets import QCheckBox
from config import config
class Mute(QCheckBox):
    def __init__(self):
        super().__init__()
        self.setText("mute")
        self.setChecked(True)
        if(config.volumeValue==0):
            self.setChecked(True)
        else:
            self.setChecked(False)
        self.stateChanged.connect(self.mute)

    def mute(self, status):
        if self.isChecked():
            config.volume.volume = 0
        else:
            config.volume.volume = 100