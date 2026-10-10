import sys 

from PyQt5.QtWidgets import QWidget, QPushButton, QCheckBox


class Preference(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Preference")
        self.resize(600, 400)

        # Cocher: Activer Discord Rich presence
        self.checkbox = QCheckBox("Activate Discord Rich Presence", self)
        self.checkbox.stateChanged.connect(self.activate_discord)


    def activate_discord(self):
         self.weeb = RPC
         self.weeb.show()