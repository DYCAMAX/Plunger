import os
import sys 
os.environ["QT_QPA_PLATFORM"] = "xcb"

from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


class propos(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("About US")
        self.setFixedSize(900, 400)

        #Pour le Logo
        FUCKINGLOGO = QLabel()
        FUCKINGLOGO.setPixmap(QPixmap("images/Plunger_Logo.png").scaled(700, 600, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        FUCKINGLOGO.setAlignment(Qt.AlignCenter)
        layout = QVBoxLayout()
        self.setLayout(layout)
        layout.addWidget(FUCKINGLOGO)
        layout.addStretch()

        # Pour le Text en bas du logo expliquant a quoi sert le logiciel
        central_widget = QWidget()
        label = QLabel("Plunger is a tool for modders made by DYCAMAX, you can create mod for Rayman Raving Rabbids 1 (Wii) and coming for all Rabbids games ever released.")
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)
        layout.addLayout(layout)
       