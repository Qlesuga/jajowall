from PyQt6.QtCore import pyqtSignal, QObject
from config import config

class Volume(QObject):
    signal = pyqtSignal(int)
    
    def __init__(self):
        super().__init__()
    

    @property
    def volume(self):
        return Volume.signal

    @volume.setter
    def volume(self,volumeValue):
        config.volumeValue = volumeValue
        self.signal.emit(config.volumeValue)
