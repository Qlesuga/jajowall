from PyQt6.QtWidgets import QSlider, QWidget, QVBoxLayout,QLabel
from PyQt6.QtCore import Qt
from config import config

class SoundSlider(QWidget):
    def __init__(self):
        super().__init__()
        
        self.__layout = QVBoxLayout()
        self.setLayout(self.__layout)

        self.label = QLabel()
        self.__layout.addWidget(self.label)
        self.label.setText(f"Volume: {str(config.volumeValue)}")

        self.slider = QSlider()
        self.__layout.addWidget(self.slider)
        self.slider.setOrientation(Qt.Orientation.Horizontal) 
        self.slider.setRange(0, 100) 
        self.slider.setValue(config.volumeValue) 
        
        config.volume.signal.connect(self.volumeChanged)
        self.slider.sliderMoved.connect(self.changeVolume)
        

    def volumeChanged(self,volume):
        self.label.setText(f"Volume: {volume}")

    def changeVolume(self,volume):
        config.volume.volume = volume
        

