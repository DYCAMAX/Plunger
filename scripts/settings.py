import sys 
from PyQt5.QtWidgets import QWidget, QPushButton


class Preference(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Preference")
        self.resize(600, 400)

        # Bouton: Activer Discord Rich presence
        self.btn = QPushButton("Activate Discord Rich Presence", self)
        self.btn.setCheckable(True)
        self.btn.move(50, 50)