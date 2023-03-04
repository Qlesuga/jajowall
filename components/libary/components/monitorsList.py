from PyQt6.QtWidgets import QComboBox
import screeninfo

class MonitorsList(QComboBox):
    def __init__(self):
        super().__init__()
        self.refresh()

    def refresh(self):
        self.clear()
        self.addItem("Every",0)
        for monitor in screeninfo.get_monitors():
            self.addItem(f"{monitor.name} {monitor.width}x{monitor.height}",monitor)
