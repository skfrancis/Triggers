from PyQt5.QtWidgets import QTreeWidgetItem
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from pathlib import Path


class TriggerItem(QTreeWidgetItem):
    def __init__(self, path, trigger_data):
        super().__init__()
        self._path = path / 'img'
        self.setData(0, self.UserType, trigger_data)
        self.create_gui()

    def create_gui(self):
        icon_path = self._path / 'trigger.png'
        icon = QIcon(str(icon_path.resolve()))
        self.setIcon(0, icon)
        self.setText(0, self.data(0, self.UserType).get('name'))
        self.setFlags(Qt.ItemIsEnabled | Qt.ItemIsUserCheckable | Qt.ItemIsSelectable)
        self.setCheckState(0, Qt.Unchecked)
