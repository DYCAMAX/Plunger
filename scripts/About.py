import sys 
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt


class propos(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("About US")
        self.size(800, 700)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        label = QLabel("Plunger is a tool for modders, you can create mod for Rayman Raving Rabbids 1 (Wii) and coming for all Rabbids games ever released.")
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)