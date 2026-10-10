import os
import shutil
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QVBoxLayout

class compiler(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Compile")
        self.setFixedSize(1000, 700)
        
class NameProject(QWidget):
    def __init__(self):
        layout = QVBoxLayout
        Bruh = QWidget()
        champ_texte = QLineEdit()
        champ_texte.setPlaceholderText("write here...")
        layout.addWidget(champ_texte)
        Bruh.setLayout(layout)
        Bruh.show()

    def running (self):
        os.mkdir("{NameProject}") # valeur donné par l'utilisateur
        os.makedirs("{NameProject}/riivolution")
        os.makedirs("{NameProject}/riivolution/config")
        os.makedirs("{NameProject}/contents")
        os.makedirs("{NameProject}/contents/TUTO") # si le mod en a besoin
        os.makedirs("{NameProject}/contents/sound") # si le mod en a besoin
        os.makedirs("{NameProject}/contents/HomeButton2") # si le mod en a besoin




            
