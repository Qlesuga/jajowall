from PyQt6.QtWidgets import QWidget
from .gifPlayer import GifPlayer
from .mediaPlayer import MediaPlayer

class Player():
    def __new__(cls,path,size):
        exst = path.split(".")[-1]
        if(exst=="gif"):
            player = GifPlayer(path,size)
        elif(exst=="mp4"):
            player = MediaPlayer(path)
            
        try:
            return player
        except:
            print("Couldnt find player for this file extension")