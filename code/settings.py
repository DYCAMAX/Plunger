import sys 
from PyQt5.QtWidgets import QWidget


class Preference(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Preference")
        self.resize(600, 400)