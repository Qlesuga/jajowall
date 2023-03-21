from PyQt6.QtWidgets import QWidget
from .gifPlayer import GifPlayer

class Player():
    def __new__(cls,path):
        exst = path.split(".")[-1]
        if(exst=="gif"):
            player = GifPlayer(path)
            
        try:
            return player
        except:
            print("Couldnt find player for this file extension")