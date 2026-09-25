import os
import sys

from PyQt5.QtWidgets import (
    QApplication, QWidget, 
    QPushButton, QVBoxLayout,
    QFileDialog, QLabel, 
    QHBoxLayout, QSpacerItem, 
    QSizePolicy, QMainWindow,
    QTreeWidgetItem, QTreeView,
    QFileSystemModel, QFileIconProvider, 
    QAction, QActionGroup
)
from settings import Preference
from explorer import ExplorerFolders
from About import propos
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QDir

# Specification de la fénétre
class ModFramework (QMainWindow):
    def __init__(self):

        super().__init__()
        self.setWindowTitle("Plunger")
        self.setGeometry(100, 100, 1280, 800)
        self.setWindowIcon(
        QIcon("/images/Plunger icon.png")
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
        ouvrir_action.triggered.connect(self.open_folders)

        ouvrir_action = file_menu.addAction("Compile")
        ouvrir_action.triggered.connect(self.open_folders)

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

        fuck_menu = fuck_menu.addAction("Report a Bug")
        fuck_menu.triggered.connect(self.report)
        
        central_widget.setLayout(layout)

    # Section definition 
    def open_folders(self):
      dir_ = QtWidgets.QFileDialog.getExistingDirectory(None, 'Select project folder:', 'F:\\', QtWidgets.QFileDialog.ShowDirsOnly)
      self.merde = ExplorerFolders
      self.merde.show()

    def open_preference(self):
      self.preference = Preference()
      self.preference.show()

    def open_propos(self):
       self.open_propos = propos
       self.open_propos.show()

    def save_folders(self):
       folders, _ = QFileDialog.getOpenFileName(self, "Choose a file", ".", "Big File and Bink Video  (*.bf *.bik*)", )
       self.merde = ExplorerFolders
       self.merde.show()

    def load_folders(self):
       folders, _ = QFileDialog.getOpenFileName(self, "choose your folders")
       self.merde = ExplorerFolders
       self.merde.show()

    def report(self):
       open 
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ModFramework()
    window.show()
    sys.exit(app.exec_())
