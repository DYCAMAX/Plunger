import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, 
    QPushButton, QVBoxLayout,
    QFileDialog, QLabel, 
    QHBoxLayout, QSpacerItem, 
    QSizePolicy, QMainWindow, 
)
from settings import Preference
from About import propos
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

# Specification de la fénétre
class ModFramework (QMainWindow):
    def __init__(self):

        super().__init__()
        self.setWindowTitle("Rabbids Mod Framework")
        self.setGeometry(100, 100, 800, 600)
        self.setWindowIcon(
        QIcon("/images/Rabbids Mod Framework icon.png")
        )

        # Pour le texte centré
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        label = QLabel("Please select a file, you want to replace")
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)

        # Creation du menu bar 
        menu_bar = self.menuBar()

        # Création du menu "file"                          
        file_menu = menu_bar.addMenu("File")

        ouvrir_action = file_menu.addAction("Open folders")
        ouvrir_action.triggered.connect(self.open_file)

        ouvrir_action = file_menu.addAction("Compile")
        ouvrir_action.triggered.connect(self.open_file)

        ouvrir_action = file_menu.addAction("Save the project")
        ouvrir_action.triggered.connect(self.save_folders)

        ouvrir_action = file_menu.addAction("Load the project")
        ouvrir_action.triggered.connect(self.load_folders)

        ouvrir_action = file_menu.addAction("Project recents")
        ouvrir_action.triggered.connect(self.load_folders)

        ouvrir_action = file_menu.addAction("Convert File")
        ouvrir_action.triggered.connect(self.load_folders)

        quitter_action = file_menu.addAction("Quitter")
        quitter_action.triggered.connect(self.close)

        options_menu = menu_bar.addMenu("Settings")

        Pref_action = options_menu.addAction("Preference")
        Pref_action.triggered.connect(self.open_preference)

        fuck_menu = menu_bar.addMenu("Help")

        fuck_menu = fuck_menu.addAction("About")
        fuck_menu.triggered.connect(self.open_propos)
        
        central_widget.setLayout(layout)

    # Section definition 
    def open_file(self):
      file, _ = QFileDialog.getOpenFileName(self, "Choose a file", ".", "Big File and Bink Video  (*.bf *.bik*)", )

    def open_preference(self):
      self.preference = Preference()
      self.preference.show()

    def open_propos(self):
       self.open_propos = propos
       self.open_propos.show()

    def save_folders(self):
       folders, _ = QFileDialog.getOpenFileName(self, "Choose a file", ".", "Big File and Bink Video  (*.bf *.bik*)", )

    def load_folders(self):
       folders, _ = QFileDialog.getOpenFileName(self, "choose your folders")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ModFramework()
    window.show()
    sys.exit(app.exec_())
