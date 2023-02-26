import wallpaper
import screeninfo

class WallpaperController():
    def __init__(self):
        self.wallpapers = []
        for monitor in screeninfo.get_monitors():
            width = monitor.width
            height = monitor.height
            x=monitor.x
            y=monitor.y
            self.wallpapers.append(wallpaper.Wallpaper(x,y,width,height))

if __name__=="__main__":
    import sys
    from PyQt6.QtWidgets import QApplication
    import workerw
    app = QApplication(sys.argv)
    wallpaper_controller = WallpaperController()
    sys.exit(app.exec())