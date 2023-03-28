from .wallpaper import Wallpaper
import screeninfo
class WallpaperController():
    def __init__(self):
        self.wallpapers = []
        for monitor in screeninfo.get_monitors():
            width = monitor.width
            height = monitor.height
            x=monitor.x
            y=monitor.y
            self.wallpapers.append(Wallpaper(x,y,width,height))

    def setMovie(self,path):
        for monitor in self.wallpapers:
            monitor.setMovie(path)
