from icoextract import IconExtractor
import io
from PyQt6.QtGui import QPixmap, QImage

class ExePreview(QPixmap):
    def __init__(self,path):
        icon = IconExtractor(path).get_icon()
        image_data = icon.getvalue()
        image = QImage.fromData(image_data)
        super().__init__(image)



