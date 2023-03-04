from PyQt6.QtWidgets import QHBoxLayout,QWidget
from .monitorsList import MonitorsList
from .refresh import Refresh
from .apply import Apply

class ActionList(QWidget):
    def __init__(self):
        super().__init__()

        self.__layout = QHBoxLayout()
        self.setLayout(self.__layout)

        self.monitorList = MonitorsList()
        self.__layout.addWidget(self.monitorList)


        self.refresh = Refresh()
        self.__layout.addWidget(self.refresh)

        self.apply = Apply()
        self.__layout.addWidget(self.apply)

