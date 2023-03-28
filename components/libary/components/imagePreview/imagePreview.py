from PyQt6.QtGui import QPixmap, QImage
from .mediaPreview import MediaPreview

class ImagePreview:
    def __new__(cls,path) -> QPixmap:
        exst = path.split(".")[-1]
        if(exst=="mp4"):
            pixmap = MediaPreview(path)
        else:
            pixmap = QPixmap(path)
        
        return pixmap
        
        