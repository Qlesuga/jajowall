import urllib.parse
from PyQt6.QtWidgets import QWidget
from .gifPlayer import GifPlayer
from .mediaPlayer import MediaPlayer
from PyQt6.QtCore import QUrl
from components.error.errorPopup import ErrorPopup

class Player():
    def __new__(cls,path,size):
        
        parsed_url = urllib.parse.urlparse(path)
        exst = path.split(".")[-1]
        if parsed_url.scheme and parsed_url.netloc:
            player = MediaPlayer(QUrl(path))
        elif(exst=="gif"):
            player = GifPlayer(path,size)
        elif(exst=="mp4"):
            player = MediaPlayer(QUrl.fromLocalFile(path))
            
        try:
            return player
        except UnboundLocalError:
            ErrorPopup("Couldnt find player for this extension")