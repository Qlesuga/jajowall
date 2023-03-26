from PyQt6.QtCore import QUrl
from PyQt6.QtMultimediaWidgets import QVideoWidget
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
from config import config
class MediaPlayer(QVideoWidget):
    def __init__(self,path):
        super().__init__()

        self.player = QMediaPlayer()
        self.player.setSource(QUrl.fromLocalFile(path))
        self.player.setVideoOutput(self)
        self.player.setLoops(-1)

        self.audio = QAudioOutput()
        self.player.setAudioOutput(self.audio)

        self.setVolume(config.volume)
        config.volume.signal.connect(self.setVolume)

        self.player.play()

    def setVolume(self,volume):
        self.audio.setVolume(config.volumeValue)
