import os
import shutil
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QVBoxLayout

layout = QVBoxLayout
Bruh = QWidget()

class compiler(QWidget):
    def __init__(self):
        super().__init__()
     
        self.setWindowTitle("Compile")
        self.setFixedSize(1000, 700)

class NameProject(QWidget):
    def __init__(self):
        champ_texte = QLineEdit()
        champ_texte.setPlaceholderText("write here...")
        layout.addWidget(champ_texte)
        Bruh.setLayout(layout)
        Bruh.show()




            
