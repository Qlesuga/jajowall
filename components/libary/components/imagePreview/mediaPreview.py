import cv2
from PyQt6.QtGui import QPixmap, QImage

class MediaPreview(QPixmap):
    def __init__(self,path):
        cap = cv2.VideoCapture(path)
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        ret, frame = cap.read()

        height, width, channel = frame.shape
        bytes_per_line = 3 * width
        q_image = QImage(frame.data, width, height, bytes_per_line, QImage.Format.Format_RGB888)

        super().__init__(q_image)