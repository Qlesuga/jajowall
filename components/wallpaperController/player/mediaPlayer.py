from PyQt6.QtCore import QUrl
from PyQt6.QtMultimediaWidgets import QVideoWidget
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
from config import config
class MediaPlayer(QVideoWidget):
    audio = QAudioOutput()
    def __init__(self,path: QUrl):
        super().__init__()

        self.player = QMediaPlayer()
        self.player.setSource(path)
        self.player.setVideoOutput(self)
        self.player.setLoops(-1)

        self.player.setAudioOutput(MediaPlayer.audio)

        self.setVolume(config.volume)
        config.volume.signal.connect(self.setVolume)

        self.player.play()

    def setVolume(self,volume):
        self.audio.setVolume(config.volumeValue)
